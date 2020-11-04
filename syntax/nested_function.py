def outer_function(a: [int]):
    b: [int] = a
    print(id(b), b)

    def inner_function():
        b.append(4)
        print(id(b), b)

    def inner_function2():
        print(id(b), b)

    inner_function()
    inner_function2()


outer_function([1, 2, 3])


def outer_function2(t: str):
    text: str = t
    print(id(text), text)

    def inner_function1():
        text = 'World!'
        print(id(text), text)

    def inner_function2():
        print(id(text), text)

    inner_function1()
    inner_function2()


outer_function2('Hello! ')
