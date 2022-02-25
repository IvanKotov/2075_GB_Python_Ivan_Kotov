import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^(\w+)@(\w+\.\w+)$')
    mail = RE_MAIL.findall(email)
    try:
        return {'username': mail[0][0], 'domain': mail[0][1]}
    except:
        pass

    raise ValueError('Wrong e-mail')

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse("someone@geekbrainsru")