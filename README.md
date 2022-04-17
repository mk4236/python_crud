 python_crud
Python CRUD Blog Source

기술블로그 예제 파일을 위해 작성된 소스입니다.
https://advdev.tistory.com/51

Python Django를 이용하여 MVT 모델을 이용한 활용방법에 대해 정리하였습니다.

user모델은 함수형 view를 이용하여 작성
board 모델은 class형 view를 이용하여 작성하였습니다

# 초기 설정
sqlite3로 작업되어있으며 데이터베이스 파일은 제외되어있으므로 마이그레이션을 진행합니다.

python3 manage.py makemigrations
python3 manage.py migrate
