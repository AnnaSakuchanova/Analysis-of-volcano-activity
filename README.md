# Analysis-of-volcano-activity
Цель данного проекта- используя методы машинного обучения в области компьютерного зрения разработать алгоритм перемещения робота по поверхности вулкана для дальнейшей установки датчиков активности.

# Введение

На сегодняшний день в мире насчитывается около 800 действующих вулканов. Большинство из них расположены вокруг Тихоокеанского «Огненного кольца». Однако существует множество заметных исключений, включая некоторые из самых опасных действующих вулканов на земле. Даже со всеми современными технологиями, человечество бессильно предотвратить извержения, имеется возможность только анализировать активность вулканов и предсказывать дальнейшее извержение и последующей эвакуацией населения возле опасной зоны, если это возможно.

Для примера, В Мексике, штат Пуэбланаходится вулкан Попокатепетль, состояние нестабильное и непредсказуемое, у подножья вулкана расположены поселения 10 млн. человек, переселить их на другую территорию для постоянного проживания не представляется возможным. Для более точного и долгосрочного прогнозирования состояния активности вулкана необходимо собрать аналитические данные с помощью датчиков, которые устанавливаются на высоте 6000 м возле жерла вулкана.

Общий вид вулкана схематично:

![вулкан](https://user-images.githubusercontent.com/106249844/176167437-1539c047-5f57-4642-ba29-e3c40ef2596f.JPG)

Установить их вручную не представляется возможным, поэтому необходимо разработать устройство, которое будет в автоматическом режиме устанавливать датчики.
В данном проекта представлена разработка устройства, которое в беспилотном режиме будет подниматься на высоту 6000 м и устанавливать датчики для сбора информации вокруг жерла вулкана.

Общий вид кратера вулкана:

![вулкан 22](https://user-images.githubusercontent.com/106249844/176174742-0c03419a-4b04-497c-ade8-f3a2cc930a45.JPG)

Точки для установки датчиков:

![вулка 33](https://user-images.githubusercontent.com/106249844/176174523-e725106d-f8e9-415d-9192-9b8ebfe6b7b4.JPG)

Для выполнения задания вездеход под управлением персонала доставляет робота на высоту 4000 м. 

Вездеход для траспортировки робота:

![22](https://user-images.githubusercontent.com/106249844/176174824-6cfd1dd6-a3e3-47bb-a9d9-fba2c292fea8.JPG)

Далее робот, выполняет подъем к жерлу вулкана со скоростью до 5 км/ч на высоты до 6000 м.
Робот несёт на борту до 10 датчиков , размещаемых во внутреннем  защищённом от внешних агрессивных воздействий отсеке.

Внешний вид робота:

![11](https://user-images.githubusercontent.com/106249844/176174777-ce95cc12-0cb4-4413-a4a6-e448e7900497.JPG)

# Описание задачи

Используя методы машинного обучения необходимо решить следующие задачи:

I. Анализ поверхности, по которой движется робот, для последующего обнаружения препятсвий.
II. Следование по маршруту к точке установки датчиков
III. Определение наклона поверхности

# Описание решения

I
Для решения задачи обнаружения препятсвий рассматривалось для способа:

1.На роботе установлена одна камера.

Алгоритм Canny для поиска границ объектов

https://user-images.githubusercontent.com/106249844/177347276-cce17dc5-8668-4377-b93c-ea8b679ee213.mp4

Оперделение границ через функцию findContours

https://user-images.githubusercontent.com/106249844/177341981-cc0247d3-ca99-40fa-bbb9-ee8dfdc8b763.mp4

2. На роботе установлены две стереокамеры


