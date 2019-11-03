import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def read_contacts(read_file="phonebook_raw.csv"):
    with open(read_file, encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


#

# TODO 1: выполните пункты 1-3 ДЗ
def reformat_contacts():
    names = {}
    contacts_list_after = list()
    contacts_list_after.append(['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'])
    pattern_phone = re.compile(r'^.?[\+7|7|8]?[\s\-]?\(?([489][0-9]{2})\)?[\s\-]?([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?'
                               r'([0-9]{2})[\s\-]?\(?([а-я]+[\s\-.])?[\s\-]?(\d+)?\)?[\s\-]?$')
    # pat_phone_tobe = re.compile(r"\0")
    for line in read_contacts(input('Введите имя файла откуда прочитать: '))[1:]:
        fn = ' '.join(line[0:3])

        fn = re.sub(r'[\s]+', ' ', fn)

        org_pos = line[3:5]
        rest = line[5:]
        fn_ex = fn.split(' ')

        phone = re.findall(pattern_phone, rest[0])
        if len(phone):
            phone = f'+7({phone[0][0]}){phone[0][1]}-{phone[0][2]}-{phone[0][3]} {phone[0][4]} {phone[0][5]}'
        else:
            phone = ''
        names[fn_ex[0]] = {'lastname': '', 'firstname': '', 'midlename': '', 'organisation': '',
                           'position': '', 'phone': [], 'e-mail': ''}
        if fn_ex[0]:
            names[fn_ex[0]]['lastname'] = fn_ex[0]
        if fn_ex[1]:
            names[fn_ex[0]]['firstname'] = fn_ex[1]
        if fn_ex[2]:
            names[fn_ex[0]]['midlename'] = fn_ex[2]
        if org_pos[0]:
            names[fn_ex[0]]['organisation'] = org_pos[0]
        if org_pos[1]:
            names[fn_ex[0]]['position'] = org_pos[1]
        if rest[1]:
            names[fn_ex[0]]['e-mail'] = rest[1]

        names[fn_ex[0]]['phone'] = []
        names[fn_ex[0]]['phone'].append(phone.strip())

    for v in names.values():
        contacts_list_after.append([v["lastname"], v["firstname"], v["midlename"], v["organisation"], v["position"],
                                    " ".join(v["phone"]), v["e-mail"]])
    return contacts_list_after


#
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def write_contacts(write_file="phonebook.csv"):
    with open(write_file, "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f)
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(reformat_contacts())


def main():
    write_contacts(f'{input("Введите имя файла, куда записать результат: ")}.csv')


if __name__ == '__main__':
    main()
