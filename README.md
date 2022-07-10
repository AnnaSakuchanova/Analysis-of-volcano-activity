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

## I
Существует, как минимум, два класса алгоритмов для решения задач помощи водителю, использующих оптические сенсоры: нейросетевые алгоритмы
и алгоритмы на основе методов классического компьютерного зрения. В данной работе было решено использовать алгоритмы на основе классического
компьютерного зрения. Связано это со следующими проблемами нейросетевых алгоритмов:

-Сложность модификации нейросетевых алгоритмов.

-Неуниверсальность нейросетевых алгоритмов.

-Сложность интерпретации решений нейросетевых алгоритмов.

Для решения задачи обнаружения препятсвий рассматривалось для способа:

1.На роботе установлена одна камера.

Алгоритм Canny для поиска границ объектов

https://user-images.githubusercontent.com/106249844/177347276-cce17dc5-8668-4377-b93c-ea8b679ee213.mp4

Оперделение границ через функцию findContours

https://user-images.githubusercontent.com/106249844/177341981-cc0247d3-ca99-40fa-bbb9-ee8dfdc8b763.mp4

2. На роботе установлена стереокамера.

Стереокамера это система из двух камер, расположенных на небольшом расстоянии друг от друга, взаимное расположение и калибровка которых известны в любой момент времени. Ключевым свойством такой системы является возможность оценки расстояния до объектов на изображении за счёт параллакса.

С использованием стереокамеры становится возможным вычислить карту глубины – отображение, сопоставляющее пикселю исходного изображения расстояние от оптического центра камеры до точки в пространстве, которая была спроецирована в данный пиксель. Карта глубины может быть плотной, в таком случае подразумевается, что большинству пикселей сопоставлено значение глубины, либо неплотной – значение глубины сопоставлено лишь некоторым пикселям. В случае неплотной карты глубины, как правило,значения глубины сопоставлены так называемым ключевым точкам – точкам, в которых на изображении имеется выраженный перепад яркостей.

Есть несколько способов построения карты глубины. Расммотрим некоторые из них:

Алгоритм Semi-global Matching  (SGM). 
SGM широко применяется для вычисления карты глубины.
В целях предобработки пары изображений, полученных с помощью стереокамеры, была использована общедоступная реализация алгоритма SGM
из открытой библиотеки OpenCV. 

Исходное изображение местности

![11](https://user-images.githubusercontent.com/106249844/178152063-7b3e0734-b556-4686-b3d2-d46d685e6171.PNG)


Применение алгоритма Semi-global Matching для построения карты глубины

![22](https://user-images.githubusercontent.com/106249844/178152092-ffd1cc60-62cd-4954-b09a-3311e20df614.PNG)

Данный алгоритм применим только в ситуациях с небольшим количеством препятствий на изображении, в случае перемещения робота по каменистой местности карта глубины будет иметь неточности.

Подход Stixel World


В модели Stixel World препятствия описываются упрощённой моделью:
Предполагается, что любое препятствие может быть хорошо приближено параллелепипедом. В таком случае на изображении препятствия могут быть хорошо приближены набором вертикальных прямоугольников с сопоставленными им значениями глубины. На рис. 4 изображена схема упрощённой модели препятствий, принятой в модели Stixel World.

Таким образом, модель Stixel World предполагает сегментацию изображения на стиксели – прямоугольники фиксированной ширины. Каждому стикселю соответствует 4 следующих значения.

1. Индекс стикселя.

2. Координата строки изображения – нижняя граница стикселя.

3. Координата строки изображения – верхняя граница стикселя.

4. Значение расстояния. При этом предполагается, что расстояние одинаково до всех пикселей, принадлежащих стикселю.

![33](https://user-images.githubusercontent.com/106249844/178152312-d6e18b4c-a395-45b4-8b42-cb6706c3616c.PNG)

Данный подход требует значительно больше вычислительных ресурсов, в отличие от предыдущего, однако известно, что алгоритм может быть оптимизирован для работы в реальном времени. 

Сегментация изображения согласно модели Stixel World. Цветом закодировано расстояние

![44](https://user-images.githubusercontent.com/106249844/178152402-f104b70b-eed7-4ed3-9905-b0584bc2b5f3.PNG)

Выделение области, безопасной для движения, с помощью сегментации согласно модели Stixel World.

![55](https://user-images.githubusercontent.com/106249844/178152416-4495878d-a88b-4a02-bccd-2399d5ce32a2.PNG)




