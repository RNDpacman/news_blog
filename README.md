Небольшой блог-сайт на django

### Установка

```
git clone https://github.com/RNDpacman/news_blog.git
```

```
cd ./news_blog/
```

```
python -m venv ./venv
```

```
source ./venv/bin/activate
```

```
pip install --upgrade pip
```

```
pip install -r ./requirements.txt
```

Создайте файл `.env` заполните по необходимости:
```
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
FROM_EMAIL=
RECIPIENT_LIST=
```

### Запуск
```
python ./main.py
```

Откройте в браузере
```
http://127.0.0.1:8000/
```

Панель администратора
```
http://127.0.0.1:8000/admin
login: admin
password: admin
```

