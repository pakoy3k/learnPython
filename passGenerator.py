import string
from random import *
chars_matrix = string.ascii_letters + string.punctuation + string.digits
new_password = "".join(choice(chars_matrix) for x in range(randint(8,16)))
print(new_password)