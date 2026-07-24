# Links

# Description
Как работает  [[Работа2/Astra/Astra Cloud Platform/Компоненты/IAM (UIDM)/Identity and Access Managment/IAM]] в MS Azure
Директори (включает в себя несколько тенантов)
	Microsoft Entra tenant
		   Management Group (пользователи / группы / service principals)
		       Azure subscription
		            биллинг и квоты
		            RBAC роли на уровне subscription
		            Resource Groups
			            RBAC роли на уровне RG
			            Policies / Locks / Tags
			            Resources
			                Virtual Machines
			                Storage Accounts
			                Databases
			                App Services
			                Kubernetes / Container Services
			                RBAC роли на уровне RG
			                Policies / Locks / Tags
			                и другие Azure services

**Policies** задают стандарты, **Locks** защищают критичные среды, **Tags** помогают учёту и управлению.

Tenant → кто мы
Management Group → как управляются несколько subscriptions
Subscription → где считаются деньги и лимиты
Resource Group → как объединены связанные ресурсы
Resource → что именно работает

1. **Identity**
    - Azure: **Tenant**.
    - OpenStack: **Domain/Identity layer**.
2. **Billing / граница учёта**
    - Azure: **Subscription**.
    - OpenStack: чаще **project/tenant**.
3. **Логическая группировка ресурсов**
    - Azure: **Resource Group**.
    - OpenStack: обычно **Project** или набор ресурсов внутри него.
4. **Ресурсы**
    - Azure: VM, DB, Storage, App Service и т.д.
    - OpenStack: Compute instances, volumes, networks и т.д.
5. **Доступ и управление**
    - Azure: RBAC на tenant/subscription/resource group/resource.
    - OpenStack: роли и политики на domain/project/resource.

Azure:
Entra Tenant
   ↓
Subscription
   ↓
Resource Group
   ↓
Resources (VM, DB, Storage, App)

OpenStack:
Identity / Domain
   ↓
Project
   ↓
Resource grouping / namespaces
   ↓
Resources (Compute, Volume, Network)

- **User account** = мы как конкретный пользователь.
- **Tenant** = организация/директория, где управляют этими пользователями.
- **Subscription** = область, где дают доступ к ресурсам и считают потребление.

Если вам нужно добавлять других пользователей и назначать им доступ, обычно вам нужны **права администратора в tenant** и/или **права на назначение ролей** в нужной subscription, resource group или ресурсе

В BillManager базовые сущности — это **клиенты, услуги, тарифные планы, финансовые операции, скидки и прочие бизнес-объекты**, потому что система автоматизирует продажу и сопровождение услуг.  
В Azure базовые сущности — это **identity, subscription, resource group, resource, RBAC, policies и billing scope**, потому что платформа управляет доступом к облачным ресурсам и их потреблением

[[BillManager]]:
Customer → Contract/Service → Tariff → Invoice/Payment → Provisioning action
Azure:
Tenant → Subscription → Resource Group → Resource → RBAC/Policy/Billing

В BillManager одна запись обычно отражает **коммерческие отношения**: кто клиент, что купил, когда платить, что отключить при просрочке.  
В Azure одна запись чаще отражает **инфраструктурные отношения**: кому можно доступ, где размещён ресурс, как его ограничить и как учесть потребление.
Если очень грубо, то BillManager отвечает на вопрос **“кому и какую услугу я продал?”**, а Azure — **“кто и к чему получил доступ в облаке?”**.  
Поэтому в BillManager сильнее выражены сущности **заказа, тарифа, счёта, продления, приостановки**

| BILLManager          | Ближайший аналог в cloud billing                | Смысл                                                                                                       |
| -------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **client**           | **customer organization / billing account**     | Юрлицо или заказчик, вокруг которого живут услуги, счета и платежи.                                         |
| **payer**            | **billing owner / invoicing entity**            | Тот, кто оплачивает и получает счета; иногда совпадает с client, иногда нет.                                |
| **user**             | **end user / admin user inside customer org**   | Человек, который действует от имени клиента, но не является самим коммерческим контуром.                    |
| **service**          | **subscription / provisioned service instance** | Конкретная потребляемая услуга, которую нужно учитывать, продлевать и, возможно, автоматически провиженить. |
| **tariff plan**      | **plan / SKU / offer**                          | Коммерческое предложение с набором параметров и ценой.                                                      |
| **invoice / charge** | **billing document / usage charge**             | Документ начисления или выставления счета за использование.                                                 |


Billing plane:
Customer organization / Billing account
  → billing profile
  → invoice section
  → invoices / payments / billing roles

Cloud plane:
Tenant
  → Management Group
  → Subscription
  → Resource Group
  → Resource

- **cloud hierarchy**: Tenant → Management Group → Subscription → Resource Group → Resource;
- **billing hierarchy**: Customer organization / Billing account → billing profile → invoice sections → invoices/payments
Пересечение происходит на уровне **subscription** - subscription имеет связь и с **tenant** через trust relationship, и с **billing account / contract** через billing relationship
Взаимосвязь между billing и tenant/subscription как **association**, а не как жёсткое вложенное дерево.  
У billing account могут быть связанные tenants, а subscriptions могут быть перенесены между billing contract’ами при соблюдении условий, не меняя при этом сами ресурсы и RBAC в tenant



## GCP-модель
`Organization   → Folder  → Project  → Resources`

В GCP **Organization** — это верхний контейнер для ресурсов и политики компании, обычно связанный с корпоративной identity-системой.  
**Folder** — промежуточный уровень для группировки проектов и применения наследуемых политик.[](https://learn.microsoft.com/ru-ru/azure/architecture/gcp-professional/services)  
**Project** — основная единица изоляции, IAM, квот, API enablement и billing association.  
**Resources** — реальные сервисы: VM, GKE clusters, buckets, databases и т.д.[](https://learn.microsoft.com/ru-ru/azure/architecture/gcp-professional/services)

## Сопоставление с Azure

|GCP|Azure|Смысл|
|---|---|---|
|**Organization**|**Tenant**|Identity / org root.|
|**Folder**|**Management Group**|Иерархическая группировка и наследование политик.|
|**Project**|**Subscription**|Основная единица изоляции, доступа и billing linkage.|
|**Resources**|**Resource Group → Resource**|В GCP project чаще уже содержит resources напрямую; в Azure есть дополнительный слой resource group.|

## Чем похожи

- И там, и там есть верхний **identity/org root**: Organization в GCP и Tenant в Azure.
- И там, и там есть промежуточный уровень для **governance над несколькими рабочими единицами**: Folder в GCP и Management Group в Azure.
- И там, и там есть рабочая единица, где сидят **IAM, quota, billing linkage и API/service enablement**: Project в GCP и Subscription в Azure.

## Чем отличаются

- В **Azure** есть явный дополнительный слой **Resource Group** между subscription и ресурсом; в **GCP** такой универсальный слой не так выражен, и project чаще является более “плотной” единицей управления.
- В **GCP** project очень часто играет роль сразу и billing scope, и IAM scope, и service container; в **Azure** эти функции более разнесены между tenant, management group, subscription и resource group.
- В **Azure** billing и cloud hierarchy лучше воспринимать как две связанные плоскости; в **GCP** billing account тоже отдельная сущность, но на практике project обычно сильнее воспринимается как базовая рабочая единица.

## Короткий вывод

Если в Azure логика была **Tenant → Management Group → Subscription → Resource Group → Resource**, то в GCP она обычно короче: **Organization → Folder → Project → Resource**.  
По смыслу они похожи, но Azure более многоуровневый в resource governance, а GCP сильнее опирается на **project** как на главный operational boundary.

AZURE                              GCP                               OPENSTACK
-----                              ---                               ----------
Tenant                             Organization                      Identity / Domain
  ↓                                  ↓                                 ↓
Management Group                   Folder                            Project
  ↓                                  ↓                                 ↓
Subscription                       Project                           Resource grouping / namespaces
  ↓                                  ↓                                 ↓
Resource Group                     Resources                         Resources
  ↓
Resource

Identity / org root
  Azure: Tenant
  GCP: Organization
  OpenStack: Identity / Domain

Governance over multiple work units
  Azure: Management Group
  GCP: Folder
  OpenStack: usually project-level / operator-defined governance

Main unit of isolation / billing / IAM
  Azure: Subscription
  GCP: Project
  OpenStack: Project

Logical grouping of related resources
  Azure: Resource Group
  GCP: less explicit; often project contains resources directly
  OpenStack: namespaces / grouping inside project

Actual resources
  Azure: VM / DB / Storage / App / etc.
  GCP: Compute / GKE / Storage / DB / etc.
  OpenStack: Compute / Volume / Network / etc.
# Backlinks
```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```
#reference/document

