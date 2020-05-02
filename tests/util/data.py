import os
import random
import string


def create_fake_mail():
    mail = 'nico_' + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + "@mail.com"
    save_data_in_file(mail)
    return mail


def get_data():
    file = open("temp", "r")
    data = file.readlines()
    file.close()
    return data


def get_data_and_destroy_file():
    data = get_data()
    destroy_file_data()
    return data


def destroy_file_data():
    os.remove("temp")


def save_data_in_file(s):
    file = open("temp", "a")
    file.write(s)
    file.close()
