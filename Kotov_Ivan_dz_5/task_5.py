def get_uniq_numbers(src: list):
    final_set = set()
    tmp = set()
    for n in src:
        if n not in tmp:
            final_set.add(n)
        else:
            final_set.discard(n)
        tmp.add(n)
    return [n for n in src if n in final_set]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
