# Links
[[Astra/Команда/Команда Платформы AC/Виталий Козловский]]
[Единый SSO для Платформы](obsidian://open?vault=Sergey's%20Vault&file=Astra%2FAstra%20Cloud%20Platform%2F%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D1%8B%2FIdentity%20and%20Access%20Managment%2F%D0%95%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9%20SSO%20%D0%B4%D0%BB%D1%8F%20%D0%9F%D0%BB%D0%B0%D1%82%D1%84%D0%BE%D1%80%D0%BC%D1%8B.canvas)
#project 
# Description
https://jira.astralinux.ru/browse/AIC-1793 Админка UIDM вместо AdminUI ALD Pro для управления пользователями - реализация - **будет в августе** 
https://jira.astralinux.ru/browse/AIC-2134 Использование Postgres в качестве CTS - **будет в августе** 
https://jira.astralinux.ru/browse/AIC-1872 MFA — повышение уровня защищённости. учётных записей - **будет в августе** 

https://jira.astralinux.ru/browse/AIC-2056 Single Logout / Backchannel Logout — доработки на стороне RooX (группирующая) - **будет в августе** 
	https://jira.astralinux.ru/browse/AIC-2063 IAM single logout. Поддержка на стороне Brest 
	https://jira.astralinux.ru/browse/AIC-2066 IAM single logout. Поддержка на стороне BillManager 
	https://jira.astralinux.ru/browse/AIC-2072 IAM single logout. Поддержка на стороне Bootsman
	https://jira.astralinux.ru/browse/AIC-2069 IAM single logout. Поддержка на стороне Astra Monitoring
	https://jira.astralinux.ru/browse/AIC-2060 IAM single logout. Поддержка на стороне XaaS
	И еще SDN?	

Единый SSO:
	https://jira.astralinux.ru/browse/AIC-1949 AstraMonitoring (UIDM RooX делает конфигурацию для перехода с КК на Dex) - **будет в августе** 
	https://jira.astralinux.ru/browse/AIC-1869 IAM интеграция с Bootsman - **будет в августе т.к. аналогичен задаче по Astra Monitoring** 
	https://jira.astralinux.ru/browse/AIC-1796  IAM интеграция с BillManager (SSO) - **будет в августе. решено плагином, который предоставил BillManager**. Нужно добавить в ACCM (написать инструкцию)
	https://jira.astralinux.ru/browse/AIC-1795 Портал Бреста поддерживает сценарий SSO через UIDM. **НУЖНА ВСТРЕЧА С АЛЕКСАНДРОМ ЛЕЩЕВЫМ после ответа от Максима**

**Что осталось**
https://jira.astralinux.ru/browse/AIC-1791 IAM мультитенантность **Нужно проработка требований**
	https://jira.astralinux.ru/browse/AIC-179 IAM управление жизненным циклом учетной записи (Админка). **Нужно проработка требований**
	https://jira.astralinux.ru/browse/AIC-1792 IAM подключение к LDAP синхронизация **Нужно проработка требований - вообще не подступались**
https://jira.astralinux.ru/browse/AIC-2035 Переход с каталога ALD Pro на FreeIPA
	https://jira.astralinux.ru/browse/AIC-2489  Провести ревью требований по подсистеме - VIR
	На стороне других компонентов (в т.ч. на стороне BillManager, AM)

Резервное копирование
	https://jira.astralinux.ru/browse/AIC-607 - Управление резервным копированием ВМ через Портал самообслуживания
	https://jira.astralinux.ru/browse/AIC-1089 Резервное копирование IAM (UIDM)
	А у нас SDN также бэкапится?

https://jira.astralinux.ru/browse/AIC-1798 Интеграция XaaS и Astra Cloud Platform

https://jira.astralinux.ru/browse/AIC-1816 Тенант менеджмент облачной платформы ACP (MVP) - кому передаем?

https://jira.astralinux.ru/browse/AIC-2035 Переход с каталога ALD Pro на FreeIPA
Бреста проверить 

Что понимаем под отрывом от ALD Pro
	1 - Заменить на FreeIPA чтобы она БД для нашего IAM
	2 - Заменим FreeIPA на собственную БД в IAM 
		тут нужно отдельно пересертифицировать IAM

Roox
- Нужно получить от них исходники

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


