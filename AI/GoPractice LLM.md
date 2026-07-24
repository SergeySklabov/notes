# Links
#GoPractice 
# Description

- Шаг 1: Сформулируйте стартовый промпт.
- Шаг 2: Возьмите примеры данных и вычислите для них результаты.
- Шаг 3: Сделайте анализ ошибок.
- Шаг 4: Улучшите промпт на основе анализа ошибок и вернитесь к шагу 2.

В таком цикле стоит подбирать промпт до тех пор, пока он не даст необходимого качества.

Давайте попробуем применить алгоритм к нашей задаче.
![[Pasted image 20250712230627.png]]
Примеры
	V2
		```
		You are a product manager who has to research user experience of your app.
		
		Your task is to analyze a review and extract main topics (maximum 3 topics).
		
		For each topic extract related sentiment – positive/negative/neutral.
		
		Here is a text of a review.
		   
		===
		{{Review text}}
		===
		
		Output a RAW json with format
		{
		"topic_name": "sentiment", ...
		}
		```
	V2
		```
		You are a product manager who has to research user experience of your app.
		
		Your task is to analyze a review and extract main topics (maximum 3 topics).
		
		Each topic has to describe an exact feature or issue of the app.
		
		It should be actionable for a product manager.
		
		For each topic extract related sentiment – positive/negative/neutral.
		
		Sentiment has to be related to the user’s current sentiment; words such as "now" could describe the current sentiment.
		
		Here is a text of a review.
		===
		Review text
		===
		   
		Solve this task step by step.
		Output a RAW json array with format
		[{
		"explanation": "explain your decision here",
		"topic_name": "extracted_name",
		"sentiment": "extracted_sentiment"
		}, ...]
		```
	V3
		```
		You are a product manager who has to research user experience of your app.
		
		You must analyze the following review and extract the main topics about the app (maximum 3 topics, minimum – 0 topics).
		   
		Each topic has to describe an exact feature or issue of the app. It should be actionable for a product manager.
		   
		If there are no exact topics about the app in the review, then return "No topics".
		   
		Step 1: Extract the first main topic about the app.
		
		Step 2: Extract the second main topic about the app. Compare this topic with the first one. If they are similar, then only use the first topic.
		
		Step 3: Extract the third main topic about the app. Compare this topic with the first and the second ones. If they are similar, then use only previous topics.
		
		Step 4: Check if extracted topics are really about exact features or issues of the app.  
		If not, then return "No topics".
		
		Step 5: If you extracted topics, then for each extracted topic, define the sentiment in the review 
		   – positive/negative/neutral. 
		
		Sentiment has to be related to user’s perception in the present, words such as "now" could describe current sentiment. 
		
		Here is a text of a review.
		
		=== 
		{{Review text}}
		===
		
		Solve this task step by step.
		
		Output a RAW json array with format
		[{
		"explanation": "explain your decision here",
		"topic_name": "extracted_name",
		"sentiment": "extracted_sentiment"
		}, ...]
		```

- Используйте четкие и подробные инструкции
    - Указывайте, в какой роли выступает модель, когда она должна формировать ответ. Например, вы можете поручить ей выступать в роли продакт-менеджера или аналитика, который проводит исследование и анализирует фидбек пользователей.
    - Используйте разделители смысловых блоков, такие как “”, ===, < >, <tag> </tag>. При этом формальных рекомендаций того, в каких случаях какие разделители использовать, нет; главное, чтобы разные смысловые блоки были явным образом разделены.
    - Задавайте формат ответа: JSON, HTML, таблица или другой.
    - Давайте примеры правильных и неправильных ответов для решаемой задачи (это называется few-shot learning).
    - Просите модель перепроверять, удовлетворяются ли все необходимые условия.
- Дайте модели «время подумать»
    - Перечисляйте инструкции для исполнения задачи как четкую последовательность шагов. Пример: Шаг 1: сделай X , Шаг 2: сделай Y , …., Шаг N: сделай Q. 
    - Добавляйте в промпт инструкцию «Решай задачу шаг за шагом» ('Solve the problem step by step').
    - Просите модель дать объяснение для ее ответов. Это поможет с идеями для улучшений в следующей итерации.

### Промпт V2 для определения важных категорий тем

У нас получился такой улучшенный промпт:

```
You are a product manager who has to research the user experience of your app.

Your task is to categorize a list of topics mentioned in user reviews.

Each category should be related to a single product feature related to the topic.

Categories must not intersect.

Here is a list of topics
===
{{Topics}}
===

Include each topic in a single category.

Solve this problem step by step:
- First extract major categories
- Map each topic to the best matching category
   
Please output only a RAW json of following structure:
{
"$topic_category_name": one-sentence summary of the category
}
```

Промпт для отнесения конкретной темы к категории можно сформулировать так:

```
You are a product manager who has to research the user experience of your app.

Your task is to map a topic into one most suitable category from given categories. 

Use only the given list of categories.
   
Here is a json with category names and their explanations 

===
{{Categories}}
===

Here is a topic
===
{{Topic}}
===

Solve this problem step by step.

Please output only a RAW json of following structure:
{{
"$topic": "$category_from_list_above" 
}}
```

https://github.com/gopracticeio/gen-ai-mini-simulator

Давайте еще раз вспомним основные аспекты работы с генеративным AI, которые мы изучили.

**Задача генеративного AI** — создавать новый высококачественный контент (текст / изображения / звук / видео) на основе запроса к модели. Модели генеративного AI обучаются на огромных объемах сырых данных: текстов, изображений, звука, видео.

#### Принцип работы больших языковых моделей для генерации текста

- Модель получает на вход строку текста.
- Задача модели — подобрать наиболее подходящее следующее слово.
- После этого обновленная строка текста вновь подается на вход модели и она вновь подбирает наиболее подходящее следующее слово.
- И так далее.

#### Алгоритм подбора промптов для решения прикладных задач с помощью LLM 

- Шаг 1: Сформулируйте стартовый промпт.
- Шаг 2: Возьмите несколько примеров данных и вычислите для них результаты. 
- Шаг 3: Сделайте анализ ошибок.
- Шаг 4: Улучшите промпт на основе анализа ошибок и вернитесь к шагу 2.

В таком цикле стоит подбирать промпт до тех пор, пока он не станет давать необходимое качество.

#### Базовые рекомендации для подбора промптов

- **Используйте четкие и подробные инструкции**
    - Указывайте, в какой роли выступает модель, когда она должна формировать ответ. Например, вы можете поручить ей выступать в роли продакт-менеджера или аналитика, который проводит исследование и анализирует фидбек пользователей.
    - Используйте разделители смысловых блоков, такие как “”, ===, < >, <tag> </tag>. При этом формальных рекомендаций того, в каких случаях какие разделители использовать, нет; главное, чтобы разные смысловые блоки были явным образом разделены.
    - Задавайте формат ответа: JSON, HTML, таблица или другой.
    - Давайте примеры правильных и неправильных ответов для решаемой задачи (это называется few-shot learning).
    - Просите модель перепроверять, удовлетворяются ли все необходимые условия.
- **Дайте модели «время подумать»**
    - Перечисляйте инструкции для исполнения задачи как четкую последовательность шагов. Пример: Шаг 1: сделай X , Шаг 2: сделай Y , …., Шаг N: сделай Q. 
    - Добавляйте в промпт инструкцию «Решай задачу шаг за шагом» ('Solve the problem step by step').
    - Просите модель дать объяснение для ее ответов. Это поможет с идеями для улучшений в следующей итерации.

Полезность рекомендаций следует проверять для каждой конкретной задачи; универсальных правил нет.

#### Всегда оценивайте качество промптов

Типовой подход для оценки — использовать обучающий и тестовый датасеты:

- на обучающем датасете нужно подбирать промпты;
- на тестовом датасете — проводить финальную оценку качества. 

Важная зона ответственности AI-продакта — решать, где необходимо действовать на основе измерения бизнес-метрик, а где достаточно субъективных решений на основе измерения метрик качества.

#### Общий подход к решению задач с большими языковыми моделями

- Понять постановку задачи и пайплайн.
- Для каждого элемента пайплайна необходимо
    - определить метрики качества;
    - найти или сформировать нужные данные;
    - подобрать промпты на основе итеративного улучшения и анализа ошибок, чтобы добиться хорошего качества решения.
- Научиться превращать результаты работы пайплайна в полезный инструмент.

#### AI-системы

Создание AI-пайплайна для решения вашей задачи — это лишь первый шаг на пути к созданию продакшн-решения. Полноценная AI-система содержит много технологических частей, необходимых для ее предсказуемой и надежной работы.

Аспекты, которые важно предусмотреть при внедрении AI-систем:

- Мониторинг качества данных и ответов моделей.
- Регулярный скрининг изменений облачных сервисов.

![](https://gopractice.ru/s3/public.gopractice.ru/course/8ba06efa-f267-4003-b112-f4d003ecfa26.png)

Вопросы оценки и менеджмента стоимости решений на основе GenAI — это область ответственности AI-продакта, а именно:

- оценка стоимости использования моделей;
- выбор модели для вашего проекта;
- оценка перспективности внедрения решения.

В кейсе мы показали, как за короткое время реализовать AI-пайплайн обработки отзывов, обладающий качеством на уровне лидирующих решений в индустрии. В прошлом для создания такого продукта потребовалась бы дорогая команда ML-инженеров. Современные технологии позволяют построить ядро такого сервиса силами одного человека за несколько часов.

### Даже если вы все забудете, помните это

Ранее для решения AI-задач требовались AI-специалисты с глубокими знаниями технологий машинного обучения, математики и программирования. 

Современные инструменты генеративного AI позволяют решать многие задачи без такой команды. Но для этого все равно необходимо освоить фундаментальные подходы к созданию AI-продуктов, а также учитывать специфику бизнес-задач.
# Backlinks
```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```
#reference/document

