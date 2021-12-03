<b>Приложение по определению расстояние от заданного адреса до ближайшего съезда МКАД</b>

Приложение доступно по адрессу https://neuronet-test-task.herokuapp.com/<br>
Пример ссылки [https://neuronet-test-task.herokuapp.com/distance/Варшавское шоссе,160к2]

Полигон МКАД представлен в виде точек (координат) определяющих съезд с автодороги. Приложение рассчитывает геометрическое расстояния от заданной точки до ближайшей точки полигона МКАД.

Запрос вводится в точке http://127.0.0.1:5000/distance/<адрес>, где <адрес>  состоит из названия города и фактического адреса, разделенные запятой.<br>
Пример запроса: http://127.0.0.1:5000/distance/красногорск, посёлок Новый, с3

Результат записывается в два лог-файла: flask_test.log и test.log

Используемые библиотеки: flask, shapely, geopy

Docker<br>
docker build . – создание image<br>
docker run -d -p 5000:5000 <image_ID> - запуск образа

