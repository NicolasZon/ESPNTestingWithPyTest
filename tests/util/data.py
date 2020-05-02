import os
import random
import string


def create_fake_mail():
    mail = 'nico_' + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + "@mail.com"
    save_data_in_file(mail)
    return mail


def destroy_file_data():
    os.remove("temp")


def file_data_exist():
    return os.path.exists("temp")


def get_older_created_mail():
    file = open("temp", "r+")
    d = file.readlines()

    data = d[0][:-1]
    if len(d) < 2:
        destroy_file_data()
        return data

    file.seek(0)
    for i in d[1:]:
        file.write(i)
    file.truncate()
    return data


def save_data_in_file(s):
    file = open("temp", "a")
    file.write(s + '\n')
    file.close()
