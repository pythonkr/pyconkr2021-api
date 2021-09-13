# PyCon Korea 2021 Api

## 개요
* 파이콘 한국 2021 서비스 운영을 위한 웹서버

## 실행
```shell
$ git clone https://github.com/pythonkr/pyconkr2021-api.git
$ cd pyconkr
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```