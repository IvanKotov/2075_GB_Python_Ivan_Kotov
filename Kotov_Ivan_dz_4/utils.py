import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(url)
    if res.status_code == 200:
        final_text = res.text.upper()
        i = final_text.find('<CHARCODE>' + code.upper() + '</CHARCODE>')
        if i == -1:
            return None

        start_value = final_text[i:]
        start_valute = start_value.find('<CHARCODE>')
        end_value = start_value.find('</VALUTE>')
        full_value = start_value[start_valute:end_value]
        result_valute = float(full_value[full_value.find('<VALUE>') + len('<VALUE>'):full_value.find('</VALUE>')].replace(',', '.'))
        result_nominal = int(full_value[full_value.find('<NOMINAL>') + len('<NOMINAL>'):full_value.find('</NOMINAL>')])
        result_value = f'1 {code} = {result_valute / result_nominal} рублей'

    return result_value

if __name__ == '__main__':
    print(currency_rates('USD'))