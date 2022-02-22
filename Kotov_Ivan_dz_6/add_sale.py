import sys




def add_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as fw:
        fw.write(f'{argv[1]}\n')
    return 0


if __name__ == '__main__':
    sys.exit(add_sale(sys.argv))