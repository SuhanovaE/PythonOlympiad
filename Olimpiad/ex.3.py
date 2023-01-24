n = int(input())
for i1 in ['', '-', '+']:
    for i2 in ['', '-', '+']:
        for i3 in ['', '-', '+']:
            for i4 in ['', '-', '+']:
                for i5 in ['', '-', '+']:
                    for i6 in ['', '-', '+']:
                        for i7 in ['', '-', '+']:
                            for i8 in ['', '-', '+']:
                                s = '1' + i1 + '2' + i2 + '3' + i3 + '4' + i4 + '5' + i5 + '6' + i6 + '7' + i7 + '8' + i8 + '9'
                                if eval(s) == n:
                                    print(s)
                                    exit()
print('Нет решения')
