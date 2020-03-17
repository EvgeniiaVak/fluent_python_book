import functools


@functools.singledispatch
def base_function(obj):
    print('Object')


@base_function.register(str)
def _(text):
    print('Str')


@base_function.register(tuple)
def tuple_first(t):
    print('tuple_first')


@base_function.register(tuple)
def tuple_second(t):
    print('tuple_second')


if __name__ == '__main__':
    base_function('some string')
    base_function((1, 3, 4))
