"""
ООП в Python-е, разумеется, есть.
Более того, все концепции в нём ровно такие же, как были в прошлом году для C++.
Поэтому заново обсуждать базовые принципы не будем.
Вместо этого сверхсжато посмотрим, "а как это будет в Python-е".
"""

# Это класс. Пока что пустой. Но уже технически корректный.
class MyClass:
    pass


# Это тоже класс. Уже не совсем пустой.
class Alpha:
    # Это *не* конструктор.
    # Его обычно воспринимают как конструктор.
    # И это даже обычно разумно.
    # Но всё-таки это *не* конструктор.
    # Это инициализатор экземпляра, уже созданного ранее "настоящим" конструктором.
    # Лезть внутрь "настоящего" конструктора обычно не надо, поэтому есть __init__
    # Но если однажды потребуется залезть в "настоящий" конструктор, то он называется __new__
    def __init__(self):
        print("Alpha: __init__ called")

    # Это деструктор.
    # Тут всё честно, это "настоящий" деструктор.
    # Из этого следует интересный момент - __del__ отработает, даже если __init__ упадёт.
    # И вот этот момент стоит на всякий случай иметь в виду.
    def __del__(self):
        print("Alpha: __del__ called")

    # А это просто некий метод
    def do_smth(self):
        print("Alpha: method called")


a = Alpha()
a.do_smth()

"""
Как вы, наверное, помните из курса C++ в прошлом году, 
при использовании правильных конструкций языка деструктор для прикладных классов почти всегда получается пустой.
Здесь в целом то же самое. Вам часто нужен __init__, это штатно и ожидаемо.
А если вдруг обнаружите себя в ситуации, когда правда обоснованно нужен __del__,
почитайте сразу ещё про __enter__ и __exit__ - это логически родственные конструкции,
которые придуманы для классов, внутри которых происходит захват и освобождение ресурсов.   
"""
