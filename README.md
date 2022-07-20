# Jamsin highschool web game server

---

## 서버 실행하기

<br>

1. 클론

```
git clone https://github.com/RODELA5/jamsin-web-game.git
cd jamsin-web-game
```

<br>

2. redis 설치하기

[Redis for windwos](https://github.com/tporadowski/redis/releases)

<br>

3. requirements 설치하기

```
pip install -r requirements.txt
```

4. migrate

```
python manage.py migrate
```

5. 서버 실행

```
python manage.py runserver
```
