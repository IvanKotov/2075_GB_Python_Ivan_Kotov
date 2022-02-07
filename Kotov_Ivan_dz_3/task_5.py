from random import choice, shuffle


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""

    list_out = []
    for n in range(count):
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_out


#print(get_jokes(2))
#print(get_jokes(10))



def get_jokes_adv(count, uq_jokes = False) -> list:
    """Возвращает список уникальных шуток без повторений"""
    list_out = []
    max_uq_jokes = min(len(nouns), len(adverbs), len(adjectives))
    if uq_jokes:

        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)

        for i in range(count):
            if count > max_uq_jokes:
                print(
                    f'Вы указали слишком большое количество уникальных шуток! Мы покажем Вам максимум уникальных шуток')
                count = max_uq_jokes

        list_out = []
        for i in range(count):
            joke = [str(nouns.pop()) + ' ' + str(adverbs.pop()) + ' ' + str(adjectives.pop())]
            list_out.append(joke)
    else:
        list_out = get_jokes(count)
    return list_out

print(get_jokes_adv(5, True))


