# initialize_django_saJH

[블로그 글 정리 링크](https://velog.io/@wogur981208/posts)

## 📌 프로젝트 개요
- Django 스터디에서 주어진 기능을 수행하기 위한 프로젝트입니다.
- 2024-04-24 ~ 2024-05-01 (1주) 기간동안 진행합니다.

## ⚙ 구현 기능 리스트
- **Auth**
- **Board**
- **자신만의 Custom 된 기능**
    - Pagination
    - Exception
    - Reponse
- **swagger**
    1. drf-yasg
- **view는 각자 (APIView, generic view, viewSet 등등)**
    - 장단점 리뷰

## ⛓ Tech Stack
- Backend : Python 3.11, Django 5.0, DRF 3.15.1
- Server : Docker
- Management : Discord, Git, Notion
- Database : SQLite3

## Run Server
```bash
# 가상환경 생성
python -m venv .venv

# 패키치 설치
poetry install

# 서버 실행 (로컬)
poetry run python manage.py runserver --settings=config.django.local
```

## 기능에 대한 설명
- **Auth**
    - 회원가입, 로그인

- **Board**
    - 게시글 작성, 수정, 삭제, 조회

- **자신만의 Custom 된 기능**
    - Pagination
    - Exception
    - Response

- **swagger**
    - drf-yasg

- **view는 각자 (APIView, generic view, viewSet 등등)**
    - APIView
      - 장점
      - 단점
    - Generic View
      - 장점
      - 단점
    - ViewSet
      - 장점
      - 단점
