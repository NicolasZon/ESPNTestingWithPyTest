import string
from random import random


def create_fake_mail():
    return 'nico_' + ''.join(random.choice(string.ascii_letters) for x in range(5)) + "@mail.com"
