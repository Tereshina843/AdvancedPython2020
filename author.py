def author(author):
    def wrap(function):
        function._author = author
        return function
    return wrap

@author("Captain Friedrich Von Schoenvorts")
def add2(num: int) -> int:
    return num + 2

print(add2._author)