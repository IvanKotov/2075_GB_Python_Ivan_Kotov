import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open(path_users_file, encoding='utf-8') as users, open(path_hobby_file, encoding='utf-8') as hobbies:
        name = [line.strip().replace(',', ' ') for line in users if line.strip()]
        hobby = [line.strip().split(',') for line in hobbies if line.strip()]

    if len(name) < len(hobby):
        sys.exit(1)


    return {user: (hobby[i] if i < len(hobby) else None) for i, user in enumerate(name)}


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
