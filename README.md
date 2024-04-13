<h4>Реализованная функциональность</h4>
<ul>
    <li>Гибкая настройка режима киоска;</li>
    <li>Разграничение прав для пользователей;</li>
    <li>Юзер-френдли интерфейс;</li>
    <li>Реализованны все функции консольной версии;</li>
    <li>Краткое и доступное описание возможностей;</li>
</ul>
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Возможность добавления программы в менеджер пакетов;</li>
 <li>Возможность выбора пользователя и приложений из списка;</li>
 <li>Оптимизированная работа приложения</li>
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python 3.11;</li>
    <li>tkinter, Bash;</li>
	<li>Git, Github;</li>
	<li>Figma;</li>
 </ul>
<h4>Демо</h4>
<p>Демо сервиса доступно по адресу: https://disk.yandex.ru/d/hrocbn1Iy9v6vA </p>


СРЕДА ЗАПУСКА
------------
1) Операционная система РЕД ОС;
2) Требуется установленный пакет redos-kiosk-utils для работы с киоск менеджером:
~~~
sudo dnf install redos-kiosk-utils
~~~
3) Так же имеется возможность установить приложение через RPM пакет:
~~~
sudo yum install package/hackathon-redos-1.0-1.red80.noarch.rpm
python3 -m hackathon-redos.main
~~~


УСТАНОВКА
------------
### Установка пакета redos-kiosk-utils

Обновление пакетов:
~~~
sudo dnf update
sudo dnf upgrade
~~~
Установка пакета РЕД ОС для работы с режимом киоска:
~~~
sudo dnf install redos-kiosk-utils
~~~
Установка проекта:
~~~
git clone https://github.com/Slonik231/redos.gt
python3 -m venv .venv
~~~
Установка необходимых библиотек и запуск:
~~~
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
~~~

<h4>Разработчики:</h4>
<ul>
    <li>Ткаченко Вадим -  Fullstack Developer / Teamlead || https://t.me/data_ptr</li>
    <li>Бабушкин Владислав - Backend Developer || https://t.me/slay_meow</li>
    <li>Швецов Игорь - Backend Developer || https://t.me/bu1101</li>
    <li>Дмитриев Виталий - Frontend Developer / Designer || https://t.me/Asperithea</li>
    <li>Хлевовой Владимир - Frontend Developer || https://t.me/edinstvennbiN </li>
</ul>



