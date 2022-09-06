# Домашка 22
### Проверка на “запахи плохого кода”



#### request.py:
- В ините упростил инициализацию info, убрал ненужный метод _split_info,
добавил self.info = info.split(" ")



#### shop.py, storage.py, store.py
- по pep8 добавил в конце кода пару пустых строк
#### application.py
1. в 19 строке убрал скобки вокруг True
2. после объявления переменной request в 25 строке убрал три строки
закомменченного мертвого кода
3. убрал большой сегмент дублирующего кода, зависящий от того, откуда и куда запрос на доставку.
Вместо этого добавил две переменные req_from и req_to, зависящие от запроса пользователя
и применил их в логике перемещений товара.





*А вообще, код изначально был написан красиво. Аккуратно, структурно, логично*

