"""

Ejercicio practicando con los warpper.

def login(func):
    print("01")
    def auth(*args, **kwargs):
        print("02")
        tmp = func(*args, **kwargs)
        if tmp == 42:
            print("Precio OK")
        return tmp
    print("03")
    return auth

@login
def test(numero):
    print("Hello")
    return 42

if __name__ == '__main__':
    test(-1)
"""
