Необходимо выбрать любой сайт интернет-магазина и написать для него 50-70 автоматизированных тестов с использованием PyTest и Selenium.
Сайт - https://edusnab.ru
Бразуер - Google Chrome, OS - Windows 10
Запуск тестов - python -m pytest -v --driver Chrome --driver-path chromedriver.exe
У каждого теста есть свой путь запуска в файле
test_main_page - проверить видимость кнопок на главной странице сайта
test_cart_page - проверка товаров, добавление в корзину, в сравнение
test_tech - проверка технических возможнойсте, увелечение, уменьшение масштаба, прокрутка страницы
test_auth_page - проверка авторизации на сайте
test_contacts - проверка полноты контактов компании
test_catalog - проверка полного каталога сайта
