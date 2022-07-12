# Deploy python (3.8) script on linux

****

Пример разворота python проекта (скрипта) на сервер. Доствка обновлений может осуществляться с помощью *git pull* 

****

## Подготовка к установке

https://github.com/Vivchy/example-python-requirements-deploy/edit/master/README.md

До пункта  [**`Создание папки venv в проекте`**](https://github.com/Vivchy/example-python-requirements-deploy/blob/master/README.md#%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B0%D0%BF%D0%BA%D0%B8-venv-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B5)

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


