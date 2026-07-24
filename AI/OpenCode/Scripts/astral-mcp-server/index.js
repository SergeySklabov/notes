#!/usr/bin/env node
const https = require("https");
const http = require("http");

const JIRA_URL = process.env.JIRA_URL || "https://jira.astralinux.ru";
const JIRA_TOKEN = process.env.JIRA_API_TOKEN || "";
const CONFLUENCE_URL = process.env.CONFLUENCE_URL || "https://life.astralinux.ru";
const CONFLUENCE_TOKEN = process.env.CONFLUENCE_API_TOKEN || "";

function apiRequest(baseUrl, path, token, redirects = 5) {
  return new Promise((resolve, reject) => {
    const url = new URL(path, baseUrl);
    const transport = url.protocol === "https:" ? https : http;
    const options = {
      hostname: url.hostname,
      port: url.port,
      path: url.pathname + url.search,
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/json",
      },
      rejectUnauthorized: process.env.IGNORE_TLS_ERRORS !== "true",
    };
    const req = transport.request(options, (res) => {
      if ((res.statusCode === 301 || res.statusCode === 302) && redirects > 0 && res.headers.location) {
        const redirectUrl = new URL(res.headers.location, baseUrl);
        return apiRequest(redirectUrl.origin, redirectUrl.pathname + redirectUrl.search, token, redirects - 1)
          .then(resolve).catch(reject);
      }
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(data) });
        } catch {
          resolve({ status: res.statusCode, body: data });
        }
      });
    });
    req.on("error", reject);
    req.end();
  });
}

const TOOLS = [
  {
    name: "jira_search",
    description: "Search Jira issues using JQL query",
    inputSchema: {
      type: "object",
      properties: {
        jql: { type: "string", description: "JQL query string" },
        limit: { type: "number", description: "Max results (1-100)", default: 25 },
      },
      required: ["jql"],
    },
  },
  {
    name: "jira_get_issue",
    description: "Get Jira issue details by key",
    inputSchema: {
      type: "object",
      properties: {
        issueKey: { type: "string", description: "Issue key (e.g. PROJ-123)" },
      },
      required: ["issueKey"],
    },
  },
  {
    name: "confluence_search",
    description: "Search Confluence pages using CQL query",
    inputSchema: {
      type: "object",
      properties: {
        cql: { type: "string", description: "CQL query string" },
        limit: { type: "number", description: "Max results (1-100)", default: 25 },
      },
      required: ["cql"],
    },
  },
  {
    name: "confluence_get_page",
    description: "Get Confluence page content by ID",
    inputSchema: {
      type: "object",
      properties: {
        pageId: { type: "string", description: "Confluence page ID" },
      },
      required: ["pageId"],
    },
  },
  {
    name: "check_jira_access",
    description: "Check Jira authentication and access status",
    inputSchema: { type: "object", properties: {}, required: [] },
  },
  {
    name: "check_confluence_access",
    description: "Check Confluence authentication and access status",
    inputSchema: { type: "object", properties: {}, required: [] },
  },
];

async function handleToolCall(name, args) {
  switch (name) {
    case "jira_search": {
      const { jql, limit = 25 } = args;
      const res = await apiRequest(JIRA_URL, `/rest/api/2/search?jql=${encodeURIComponent(jql)}&maxResults=${limit}`, JIRA_TOKEN);
      return formatResult(res);
    }
    case "jira_get_issue": {
      const { issueKey } = args;
      const res = await apiRequest(JIRA_URL, `/rest/api/2/issue/${encodeURIComponent(issueKey)}`, JIRA_TOKEN);
      return formatResult(res);
    }
    case "confluence_search": {
      const { cql, limit = 25 } = args;
      const res = await apiRequest(CONFLUENCE_URL, `/rest/api/content/search?cql=${encodeURIComponent(cql)}&limit=${limit}`, CONFLUENCE_TOKEN);
      return formatResult(res);
    }
    case "confluence_get_page": {
      const { pageId } = args;
      const res = await apiRequest(CONFLUENCE_URL, `/rest/api/content/${encodeURIComponent(pageId)}?expand=body.storage,version,space`, CONFLUENCE_TOKEN);
      return formatResult(res);
    }
    case "check_jira_access": {
      const res = await apiRequest(JIRA_URL, "/rest/api/2/myself", JIRA_TOKEN);
      return formatResult(res);
    }
    case "check_confluence_access": {
      const res = await apiRequest(CONFLUENCE_URL, "/rest/api/user/current", CONFLUENCE_TOKEN);
      return formatResult(res);
    }
    default:
      return { content: [{ type: "text", text: `Unknown tool: ${name}` }], isError: true };
  }
}

function formatResult(res) {
  if (res.status >= 200 && res.status < 300) {
    return { content: [{ type: "text", text: JSON.stringify(res.body, null, 2) }] };
  }
  return { content: [{ type: "text", text: `HTTP ${res.status}: ${JSON.stringify(res.body)}` }], isError: true };
}

let requestId = 0;
let isInitialized = false;

function sendMessage(msg) {
  process.stdout.write(JSON.stringify(msg) + "\n");
}

function handleMessage(msg) {
  if (msg.method === "initialize") {
    isInitialized = true;
    sendMessage({
      id: msg.id,
      result: {
        protocolVersion: "2024-11-05",
        capabilities: { tools: {} },
        serverInfo: { name: "astral-jira-confluence", version: "1.0.0" },
      },
    });
  } else if (msg.method === "notifications/initialized") {
    return;
  } else if (msg.method === "tools/list") {
    sendMessage({ id: msg.id, result: { tools: TOOLS } });
  } else if (msg.method === "tools/call") {
    const { name, arguments: args } = msg.params;
    handleToolCall(name, args || {}).then((result) => {
      sendMessage({ id: msg.id, result });
    }).catch((err) => {
      sendMessage({ id: msg.id, result: { content: [{ type: "text", text: `Error: ${err.message}` }], isError: true } });
    });
  }
}

let buffer = "";
process.stdin.on("data", (chunk) => {
  buffer += chunk.toString();
  const lines = buffer.split("\n");
  buffer = lines.pop() || "";
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed) {
      try {
        handleMessage(JSON.parse(trimmed));
      } catch (err) {
        sendMessage({ id: null, result: { content: [{ type: "text", text: `Parse error: ${err.message}` }], isError: true } });
      }
    }
  }
});

process.stdin.on("end", () => process.exit(0));
