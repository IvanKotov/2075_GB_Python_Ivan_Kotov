tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):

    if len(tutors) == len(klasses):
        return ((name, klass) for name, klass in zip(tutors, klasses))
    else:
        len_klass = len(klasses)
        i = 0
        for name in tutors:
            if i < len_klass:
                yield name, klasses[i]
                i += 1
            else:
                yield name, None


generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration