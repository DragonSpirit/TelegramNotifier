# Web notification telegram repeater

Бот с поддержкой получения входящих POST запросов с целью транслирования всем заинтересованным подписчикам.

Список поддерживаемых команд:
  - /subscribe - подписывает пользователя на получение входящих уведомлений
  - /unsubscribe - отписка от уведомлений
  - /last - вывод последнего информационного сообщения, вне зависимости от подписки

# Конфигурирование

Конфигурирование параметров бота производится в cfg/config.py.

Конфигурирование параметров flask сервера производится в функции init файла src/server.py

# Запуск
```sh
$ python app.py
```

# Отправка сообщений

При запуске приложения поднимается HTTP сервер на 80 порту (по умолчанию).
Отправка сообщения производится путем POST запроса на URL: http://${IP}:{PORT}/fire, где IP - адрес хоста, PORT - порт сервера, например:

```json
{
  "message" : "Сборка #57 провалилась. Smoke тест #2 провалился"
}
```

При этом необходимо не забыть про заголовок Content-Type: application/json

# TODO
  - Поддержка различных уровней уведомлений
  - Аутентификация по ключу для отсеивания спама