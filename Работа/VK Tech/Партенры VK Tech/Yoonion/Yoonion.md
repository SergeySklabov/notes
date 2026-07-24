---
status: To Do
due:
---
# Description
**TeamStorm**
Михаил Устинов mike.ustinov@teamstorm.io
Михаил Рябов mikhail.ryabov@teamstorm.io

**TestIT**
Артем Костриков artem.kostriukov@testit.software
# Todo List
> [!todo] Active
> ```dataview
>  task
>  from [[]]
>  where !completed
> sort file.ctime desc
> ```

> [!todo] Completed
> ```dataview
>  task
> from [[]]
>  where completed
>   sort file.ctime desc
>   limit 10
> ```
# Links
#partners 
#project 

# Backlinks 
```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```


