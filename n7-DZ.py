var0 = [5, '10', -3, 9, 0, 11, '0', 48, 1]
res = int


def calc(num, dgr):
    if num != int:
        num = int(num)
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else:
        global res
        i = 1
        for _ in range(dgr):
            yield num ** i
            i += 1


var1 = iter(var0)
print(var1)
for el in var1:
    print(f'element {el}')
    res = calc(el, 5)
    for _ in res:
        print(_)
