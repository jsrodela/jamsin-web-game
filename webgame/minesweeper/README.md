# 지뢰찾기
## 통신 구조

- 웹소켓 주소: `ws://example.com/ws/minesweeper`

### 클라이언트 -> 서버

- 게임판 생성 (set)
```
{
  "command" : "set",
  "size" : 게임판 크기 (정사각형 한 변의 길이),
  "num" : 지뢰 개수
}
```

- 칸 공개 요청 (uncover)
```
{
  "command" : "uncover",
  "pos" : [ x좌표, y좌표 ]
}
```

- 깃발 설치 (flag)
```
{
  "command" : "flag",
  "pos" : [ x좌표, y좌표 ]
}
```

- 깃발 회수 (unflag)
```
{
  "command" : "unflag",
  "pos" : [ x좌표, y좌표 ]
}
```

### 서버 -> 클라이언트

- 칸 공개 응답 (uncover)
```
{
  "command" : "uncover",
  "cells" : [
    {
      "x" : x좌표,
      "y" : y좌표,
      "value" : 근처 3x3의 지뢰 개수 (-1 = 현재 칸이 지뢰)
    },
    ...
  ]
}
```
