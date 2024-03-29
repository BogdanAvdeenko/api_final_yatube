# «API для Yatube» 

В проекте «API для Yatube» реализованы API для моделей приложений.

У неаутентифицированных пользователей доступ к API только на чтение. 
К некоторым эндпоинтам доступ предоставляться только аутентифицированным пользователям.
Аутентифицированным пользователям разрешено изменение и удаление своего контента.

Для аутентификации используются JWT-токены.
Работа с JWT-токенами организована при помощи библиотеки Djoser.

Пременена пагинация на уровне view-классов с помощью LimitOffsetPagination.
Это даёт возможность клиенту самостоятельно определять, какое число объектов вернётся и с какого по счёту объекта начать отсчёт.

## Как запустить проект:

- [x] 1) Клонировать репозиторий и перейти в него в командной строке.
- [x] 2) Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
source venv/Scripts/activate
```

```
py -m pip install --upgrade pip
```

- [x] 3) Установить все необходимые пакеты из requirements.txt:

```
pip install -r requirements.txt
```

- [x] 4) Выполнить миграции:

```
python manage.py migrate
```

- [x] 5) Запустить проект:

```
python manage.py runserver
```

### Аутентификация по JWT-токену:

Для получения токена: отправьте POST-запрос на эндпоинт localhost:8000/api/v1/jwt/create/, передав действующий логин и пароль в полях username и password. 

Токен вернётся в поле access.

Этот токен также надо будет передавать в заголовке каждого запроса, в поле Authorization. Перед самим токеном должно стоять ключевое слово Bearer и пробел.

Так вы получите доступ к методам.

## Примеры:

Когда вы запустите проект, по адресу localhost:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как работает API. Документация представлена в формате Redoc.

Пример GET запроса для получения публикации по id:

```
/api/v1/posts/1 
```

Ответ:


```
{
    "id": 1,
    "author": "Example_author",
    "text": "Example_text",
    "pub_date": "Example_pub_date",
    "image": "Example_image",
    "group": "Example_group"
}
```

## Используемые технологии:

- Python
- Django 
- Djangorestframework
- PyJWT
- Pillow
- Djoser

## Автор:

Богдан Авдеенко.
Студент факультета Бэкенд. Когорта №33.
Яндекс Практикум.
