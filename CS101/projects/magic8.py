# https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/
# modules/cspath-python-control-flow/projects/python-magic-8-ball

from random import randint

name = "Vriska"
question = "Are you able to turn the volume down?"
answer = ""

random_number = randint(1, 12)
#print(random_number) (Testing the function)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Probably not, no."
elif random_number == 11:
    answer = "Certainly not."
elif random_number == 12:
    answer = "Don't even think about it."
else:
    answer = "Error"

if name == "":
    print("Question :", question)
else:
    print(name, "asks:", question)

if question == "":
    print("""Your question was lost in the void for eternity...
    Couldn't find your question.""")
else:
    print("Magic 8-Ball's answer:", answer)
