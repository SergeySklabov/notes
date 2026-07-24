### Gitaly Node(x3)
- - -
```toml
bin_dir = "/opt/gitaly/bin"  
runtime_dir = "/opt/gitaly/run"  
listen_addr ="0.0.0.0:8075"  
prometheus_listen_addr = "0.0.0.0:9236"  
  
[auth]  
token = 'gitaly2'  

[git]  
ignore_gitconfig = true  
  
[[storage]]  
name = "default"  
path = "/opt/gitaly/repositories/default"  
  
[logging]  
dir = "/opt/gitaly/log"  
format = "json"
```

### Praefect
- - -
```toml
listen_addr = "0.0.0.0:2305"  
prometheus_listen_addr = "0.0.0.0:9652"  

[logging]  
format = "json"  

[auth]  
transitioning = false  
token = "praefect2"  

[failover]  
enabled = true  

[database]  
host = "host_db"  
port = 5432  
user = "praefect_lt_user"  
password =  
dbname = "praefect_lt_db"  
sslmode = "disable"  

[[virtual_storage]]  
name = "default"
  
[[virtual_storage.node]] # каждую ноду указать
storage = "default"  
address = "tcp://address:8075"  
token = "gitaly2"  

```
