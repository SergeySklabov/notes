---
aliases:
  - Интерфейсы/APIM
  - Интерфейсы/APIM
Внутр/Внешн: Внутренний
---
# Links
#project 
[[Astra/Команда/Команда Платформы AC/Шадрин Александр]] - технический менеджер продукта
# Description

# Todo List
```tasks
not done
tags include #Брест
sort by due
```

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

