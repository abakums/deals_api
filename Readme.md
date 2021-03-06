# Deals API Project
## Описание сервиса
Данный сервис создан для загрузки и обработки типовых .csv файлов и вывода результатов обработки в виде .csv файла или 
с помощью соответствующего API

## Приступая к работе
1. Чтобы приступить к работе с сервисом загрузить его в .zip формате из 
[git-репозитория](https://github.com/abakums/deals_api), распакуйте скачанный файл в удобную для вас папку 
2. Откройте командную строку и перейдите в папку, в которую произвели распаковку. 
3. Выполните запуск сервиса, предварительно загрузив docker на свой локальный компьютер, с помощью единственной команды в командной строке из папки, содержащей файлы проекта:

```console
    docker-compose up
```


## Работа с сервисом
1. После запуска сервиса перейдите в браузере на [начальную страницу](http://127.0.0.1:8000/)
2. Это направит Вас на начальную страницу сервиса, где можно ознакомиться с 
интерфейсом и увидеть [ссылку](http://127.0.0.1:8000/upload_file/) для перехода к загрузке.csv файла <br>
3. На данной странице предлагается прикрепить .csv файл для обработки, указать имя загрузки, а также комментарий,
после чего получить список из 5 клиентов, потративших наибольшую сумму за весь период, содержайщийся в файле.
4. После загрузки файла Вы можете ознакомиться с результатом (рекомендуется запомнить 'id' загрзуки), перейдя 
по начению поля 'url', или скачать файл, содержайщий результат обработки в .csv формате, нажав на значение 
'file' и загрузив файл. После перехода по 'url'
Вы увидете список из 5 клиентов, каждый из которых имеет следующие поля:
    - username - логин клиента
    - spent_money - сумма потраченных средств за весь период
    - gems - список из названий камней, которые купили как минимум двое из списка 
"5 клиентов, потративших наибольшую сумму за весь период", и данный клиент является одним из этих покупателей
5. Для того, чтобы получить результат обработки файла, который загружен в систему ранее и не загружать его в систему 
очередной раз, на странице загрузки файла (Upload File) нажмите на "Фильтр" и введите идентификатор 'id' некогда 
загруженного файла. Вы получите результат его обработки и Вам не придется отправлять форму с данными загрузки 
второй раз
6. В системе в левом верхнем углу для удобства имеется панель навигации, по которой можно перемещаться с помщью нажатия 
на соответствующие названия страниц.

## Контакты
По всем вопросам можно написать на почту abakumovs882@gmail.com
