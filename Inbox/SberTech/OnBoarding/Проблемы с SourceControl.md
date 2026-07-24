# Links
#project 
# Description
Что из этого сделано?
![[Pasted image 20250605115237.png]]
![[Pasted image 20250605115307.png]]
![[Pasted image 20250605115412.png]]
![[Pasted image 20250605115324.png]]
Как оказывается тех поддержка? Где документация? Какие специфические требования банка?



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

```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```

