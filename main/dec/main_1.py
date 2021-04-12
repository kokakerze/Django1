"""Working with decorators."""
# from datetime import datetime
#
#
# def counter_decorate(func):
#     """Count decorates."""
#     cnt = 0
#
#     def wrapper():
#         """ """
#         nonlocal cnt
#         cnt += 1
#         print(cnt)
#
#         res = func()
#         return res
#
#     return wrapper
#
#
# def foo():
#     print(datetime.now())
#
#
# foo = counter_decorate(foo)
# foo()
# foo()
