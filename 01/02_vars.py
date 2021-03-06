"""
Python-е переменные не такие строгие, как в C++.
Их не требуется объявлять заранее.
И у них вообще нет строгих типов.
(Кстати, вот так можно делать блоки многострочных комментариев.)
"""

# Например, сейчас у меня есть переменная а, которая равна целому числу 42
a = 42

# Могу её напечатать
print(a)

# А потом могу внезапно сказать, что теперь a содержит строку
a = "Test string"

# Ну и снова напечатать, да.
print(a)

"""
В C++ компилятор за такое убил бы на месте.
А вот в Python так можно.
За всё, конечно, приходится чем-то платить. Но об этом мы поговорим позже.
"""