# Links
#Stepic 
# Description
Разработать Long Polling HTTP API для управления чат-комнатами и сообщениями в них.
**Сущности**:
- Чат-комната: ID, название, список участников
- Сообщение: ID, текст, автор, время отправки
**Операции и запросы:**
1. Создание новой чат-комнаты.
2. Добавление участника в чат-комнату.
3. Удаление участника из чат-комнаты.
4. Отправка сообщения в чат-комнату.
5. Получение новых сообщений в чат-комнате через Long Polling.
**Дополнительно:**
- Реализовать аутентификацию участников (например, через API ключ).
- Реализовать возможность фильтрации сообщений по времени.
**Бонус:**
- Добавить поддержку нескольких типов сообщений (например, текст, изображение).
```
openapi: "3.0.0"  
info:  
  title: "Chat Room Long Polling API"  
  version: "1.0.0"

paths:  
  /rooms:  
    post:  
      summary: Create a new chat room  
      requestBody:  
        required: true  
        content:  
          application/json:  
            schema:  
              type: object  
              properties:  
                name:  
                  type: string  
      responses:  
        '201':  
          description: Room created  
        '400':  
          description: Bad Request

  /rooms/{roomId}/join:  
    post:  
      summary: Join a chat room  
      parameters:  
        - in: path  
          name: roomId  
          required: true  
          schema:  
            type: string  
      requestBody:  
        required: true  
        content:  
          application/json:  
            schema:  
              type: object  
              properties:  
                apiKey:  
                  type: string  
      responses:  
        '200':  
          description: Joined successfully  
        '404':  
          description: Room not found

  /rooms/{roomId}/leave:  
    post:  
      summary: Leave a chat room  
      parameters:  
        - in: path  
          name: roomId  
          required: true  
          schema:  
            type: string  
      requestBody:  
        required: true  
        content:  
          application/json:  
            schema:  
              type: object  
              properties:  
                apiKey:  
                  type: string  
      responses:  
        '200':  
          description: Left successfully  
        '404':  
          description: Room not found

  /rooms/{roomId}/messages:  
    post:  
      summary: Send a message  
      parameters:  
        - in: path  
          name: roomId  
          required: true  
          schema:  
            type: string  
      requestBody:  
        required: true  
        content:  
          application/json:  
            schema:  
              type: object  
              properties:  
                apiKey:  
                  type: string  
                message:  
                  type: string  
      responses:  
        '201':  
          description: Message sent  
        '400':  
          description: Bad Request

  /rooms/{roomId}/poll:  
    get:  
      summary: Long poll for new messages  
      parameters:  
        - in: path  
          name: roomId  
          required: true  
          schema:  
            type: string  
        - in: header  
          name: Last-Message-Time  
          required: false  
          schema:  
            type: string  
      responses:  
        '200':  
          description: New messages  
          content:  
            application/json:  
              schema:  
                type: array  
                items:  
                  type: object  
                  properties:  
                    id:  
                      type: string  
                    message:  
                      type: string  
                    time:  
                      type: string  
                    type:  
                      type: string  
        '204':  
          description: No new messages  
        '404':  
          description: Room not found

components:  
  securitySchemes:  
    ApiKeyAuth:  
      type: apiKey  
      in: header  
      name: X-API-KEY  
``` 
**Объяснение спецификации**
1. **Создание комнаты**: POST запрос на `/rooms` с JSON, содержащим название комнаты.
2. **Присоединение к комнате**: POST запрос на `/rooms/{roomId}/join` с JSON, содержащим API ключ пользователя.
3. **Выход из комнаты**: POST запрос на `/rooms/{roomId}/leave` с JSON, содержащим API ключ пользователя.
4. **Отправка сообщения**: POST запрос на `/rooms/{roomId}/messages` с JSON, содержащим API ключ и сообщение.
5. **Long Polling для сообщений**: GET запрос на `/rooms/{roomId}/poll`. Если есть новые сообщения, вернет 200 с массивом новых сообщений. Если нет — вернет 204.
Эта спецификация также включает фильтрацию сообщений по времени через заголовок `Last-Message-Time`.
Бонус: В сообщениях добавлен тип сообщения (`type`), который может быть, например, "text" или "image".
# Backlinks
```dataview 
	TABLE without id
	file.outlinks AS "OUTGOING", 
	file.inlinks AS "BACKLINKS"
	WHERE file.name = this.file.name 
```
#reference/document

