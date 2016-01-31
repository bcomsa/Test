a = '12344321'


def doixung(a):
    a1 = ''
    a2 = ''
    if len(a) % 2 == 0:
        a1 = a[0:len(a) / 2]
        a2 = a[len(a) / 2:len(a)]
    else:
        a1 = a[0:len(a) / 2]
        a2 = a[len(a) / 2 + 1:len(a)]
    if a1 == a2[::-1]:
        print 'chuoi %s doi xung' % a
    else:
        print 'chuoi %s sida' % a
doixung(a)
