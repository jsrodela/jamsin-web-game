# Jamsin highschool web game server

---

## 서버 실행하기

<br>

0. 준비물

아래 과정을 진행하기 위해 python과 git을 설치해야 합니다.  
Python 3.10 환경 기준으로 작성되었습니다.

<br>

1. 클론

```
git clone https://github.com/RODELA5/jamsin-web-game.git
cd jamsin-web-game
```

<br>

2. Redis 실행하기

   1. [Redis for windwos](https://github.com/tporadowski/redis/releases) 설치

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

---

### 설치 에러 및 해결법

pip install channels 에서 cryptography build 에러 (Linux 환경)

- ffi.h: No such file or directory

  ```
  sudo apt install libffi-dev
  ```

- Can't find Rust compiler

  ```
  curl https://sh.rustup.rs -sSf | sh
  ```

- opensslv.h: No such file or directory

  ```
  sudo apt install libssl-dev
  ```

---

## 테스트한 환경

- Windos 10
- Raspberry Pi OS Lite
