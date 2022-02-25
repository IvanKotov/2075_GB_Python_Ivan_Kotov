import sys




with open('bakery.csv', 'r+', encoding='utf-8') as fr:
    for i, line in enumerate(fr, 1):
        if len(sys.argv) == 2 and i < int(sys.argv[1]):
            continue
        elif len(sys.argv) == 3 and (i < int(sys.argv[1]) or int(sys.argv[2]) < i):
            continue
        print(line.rstrip())


