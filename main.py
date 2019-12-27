# Parse txt and generate users
# populate to dict with uuid as key
# return list of keys, shuffle
# assign receivers based on shuffled list
# send emails, store file with pairs

from santa import Santa
from email_sender import EmailSender
import random

fname = 'the_list.txt'
santas = {}

with open(fname) as f:
    content = f.readlines()

for line in content:
    santa_line = line.strip().split(', ')
    new_santa = Santa(santa_line[0], santa_line[1])
    santas[new_santa.get_id()] = new_santa

key_list = list(santas.keys())
random.shuffle(key_list)
list_of_pairs = []

for i in range(len(key_list)):
    if i + 1 == len(key_list):
        receiver_id = key_list[0]
    else:
        receiver_id = key_list[i + 1]
    santas[key_list[i]].set_receiver(receiver_id)

    list_of_pairs.append(
        '{} gives to {}'.format(santas[key_list[i]].get_name(), santas[receiver_id].get_name()))

email_sender = EmailSender()

for santa in santas.values():
    print(santa.get_name(), 'gives to',
          santas[santa.get_receiver()].get_name())

    message = """
    Heisann {}.
    Du er nisse for {}.
    God jul!
    """.format(santa.get_name(), santas[santa.get_receiver()].get_name())

    email_sender.send(santa.get_email(), message)

print(list_of_pairs)

f = open("pairs.txt", "w+")

for line in list_of_pairs:
    f.write(line + '\n')

f.close()
