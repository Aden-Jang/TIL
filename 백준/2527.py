for _ in range(4):
    ax, ay, ap, aq, bx, by, bp, bq = map(int, input().split())
    if ap < bx or ax > bp or ay > bq or aq < by:
        print('d')
    elif ap == bx or ax == bp:
        if aq == by or bq == ay:
            print('c')
        else:
            print('b')
    elif aq == by or bq == ay:
        print('b')
    else:
        print('a')