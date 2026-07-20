def super_sum(*args, **kwargs):
    if kwargs.get('bonus') == 5:
        return sum(args+kwargs)
    return sum(args)
print(super_sum(1, 2, 3))            # Должно быть 6
print(super_sum(10, 10, bonus=5))    # Должно быть 25 (10+10+5)