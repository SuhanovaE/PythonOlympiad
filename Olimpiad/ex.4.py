ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def toBASEint(num, base, b=''):
    if num < base:
        return ALPHA[num % base] + b[::-1]
    else:
        return toBASEint(num // base, base, b + ALPHA[num % base])


def toBaseFrac(frac, base, n=16, b=''):
    if not n:
        return b.rstrip('0')
    else:
        frac *= base
        return toBaseFrac(frac - int(frac), base, n - 1, b + ALPHA[int(frac)])


number = input()
basein = int(input())
baseout = int(input())
f = 4
if number.startswith('-'):
    sign = '-'
    number = number[1:]
else:
    sign = ''

if '.' in number:
    num, frac = map(str, number.split('.'))
    a = toBASEint(int(num, basein), baseout)
    b = 0
    k = basein
    for i in frac:
        b += ALPHA.index(i) / k
        k *= basein
    b = toBaseFrac(b, baseout, f)
    print(sign + a + '.' + b)
else:
    print(sign + toBASEint(int(number, basein), baseout))