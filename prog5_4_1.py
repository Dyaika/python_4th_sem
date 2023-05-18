from deal import pre, post, ensure, raises, reason, has
import pytest


@pre(lambda a, b: b != 0)
@post(lambda result: result * b == a)
@raises(ZeroDivisionError)
@reason(ZeroDivisionError, lambda a, b: b != 0)
@ensure(lambda a, b, result: isinstance(result, float))
@has('stdout')
def divide(a, b):
    print("a and b")
    return a / b


a = 20
b = 10
print(divide(a, b))
