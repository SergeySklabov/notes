# Links
 #Claude #Claude_code #vibecoding 
# Description
[Claude Code: полный гайд по AI-кодингу (хаки, техники и секреты)](https://www.youtube.com/watch?v=6NK4Pona2fY)
![[Pasted image 20260124232625.png]]
#MCP (Model Context Protocol) - открытый стандарт, который запустил #anthropic  
![[Pasted image 20260125224438.png]]
Плюс можно погуглить любые конфиги для MCP
Плюс есть репозитории
- https://github.com/modelcontextprotocol/servers
- https://github.com/punkpeye/awesome-mcp-servers

Какие MCP рекомендуется использовать
- Sequential Thninking - делает из обычной модели думающую
- Context7 - дает документацию библиотек по котором нейронка будет проходить и сверять свое решение
- PostgresSQL MCP - для вайб-аналитики баз данных
- TestSprite - аутсорс тестировщик
- Supabase MCP - быстра настройка БД (opensource обветка над PostgresSQL). Похож на
- PostgresSQL MCP, но при этом создавать и изменять таблицы, натсрвиать все что у угодно в своей и supabase базе
- Playwright - управляемый браузер. Открывать любые сайты, переходить по ссылкам, заполнять формы. Цель: 
	- тестирование фронтет/дебажить, проверять что нет ошибок в консоле
	- поиск информации в интернете
-  Filesystem - (только для Claude Desktop) позволяет создавать/изменять/удалять файлы. Позволяет ограничить доступ к файлам в определенной директории.
- WCGV - (только для Claude Desktop) позволяет запускать команды в терминале, отслеживать статус выполнения, собирать проекты

Codex CLI - аналог от ChatGPT (если уже сидишь на ChatGPT) 
Gemini CLI - бесплатный аналог от Google
Qwen Code - также бесплатный аналог

Пример простого MCP для управления Telegram ботом:
- https://github.com/coderroleggg/telegram-bot-mcp
# Backlinks
```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```
#reference/document

