# Электронный магазин "Дом немецкой посуды"
E-commerce сайт для магазина товаров для дома "Дом немецкой посуды"
## About
Интернет-магазин для компании "Дом немецкой посуды”. На сайте представлена продукция различных брендов, которыми торгует компания. Пользователь сайта может просматривать описание товаров и добавлять их в корзину. После этого, пользователь может оплачивать товары на сайте, или выбирать удобный способ оплаты в магазине. Администратор сайта имеет возможность пополнять каталог товаров и менять цены.
## Как запустить проект:
- Склонировать репозиторий и перейти в папку проекта через командную строку:
```
git@github.com/N1ghtmarus/dom_posudi
cd dom_posudi/
```
- Создать и активировать вируальное окружение (если вы работаете не в Pycharm):
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Создать миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```
## Пример работы сайта
Посмотреть на функционирование сайта можно [здесь](http://domposudi.herokuapp.com "здесь")

## Команда разработчиков:
[Илья Воронков](https://github.com/ifize) | [Архип Петин](https://github.com/N1ghtmarus "Архип Петин")

![](https://img.shields.io/pypi/pyversions/p5?logo=python&logoColor=yellow&style=for-the-badge)
![](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)
![](https://img.shields.io/badge/DRF-3.12.4-lightblue)
