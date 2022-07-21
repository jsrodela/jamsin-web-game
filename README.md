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

2. Redis 실행하기

    1. [Redis for windwos](https://github.com/tporadowski/redis/release) 설치

        또는 

    2. [Docker](https://www.docker.com/)에서 redis 실행
    ```
    docker run -p 6379:6379 -d redis:5
    ```

<br>

3. Requirements 설치하기

```
pip install -r requirements.txt
```

4. Migrate

```
python manage.py migrate
```

5. 서버 실행

```
python manage.py runserver
```
