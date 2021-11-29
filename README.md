# Deploy python (3.8) script on linux

****

## Подготовка к установке

https://github.com/Vivchy/example-python-requirements-deploy/edit/master/README.md

****

## Загрузка на сервер

Клонировать репозиторий

> git clone https://github.com/Vivchy/linuxdeployexample.git

Перейти в каталог

> cd linuxdeployexample/

Создать *venv* в каталоге

> /usr/bin/python3 -m venv venv

Запустить venv

> source ./venv/bin/activate

Установить зависимости pip

> pip install -r requirements.txt

Запустить  скрипт

> python3 main.py


