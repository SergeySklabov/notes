---
Внутр/Внешн: Внутренний
---
# Links
#project 
[[Крюков Андрей]] - архитектор/и.о. продакта
[[Милащенко Ольга]] - системный аналитик
# Description

# Todo List
> [!todo] Active
>  ```dataview
> task
> from ""
> where !completed
> 	and (
> 		contains(text, "[[" + this.file.name + "]]")
> 		or contains(text, "[[" + this.file.name + "|")
> 		or contains(text, "[[" + this.file.name + "#")
> 	)
sort file.ctime desc
> ```

> [!todo] Completed
>  ```dataview
> task
> from ""
> where completed
> 	and (
> 		contains(text, "[[" + this.file.name + "]]")
> 		or contains(text, "[[" + this.file.name + "|")
> 		or contains(text, "[[" + this.file.name + "#")
> 	)
sort file.ctime desc
> ```





```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```

