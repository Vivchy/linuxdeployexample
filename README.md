# Deploy python (3.8) script on linux

****

Пример разворота python проекта (скрипта) на сервер. Доствка обновлений может осуществляться с помощью *git pull* 

****

## Подготовка к установке

https://github.com/Vivchy/example-python-requirements-deploy/edit/master/README.md

До пункта  **`Создание папки venv в проекте`**

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


