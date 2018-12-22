import random
from typing import Any, Union

correct: str = '✓'
wrong: str = 'X'


def mental_maths():
    mm = 0
    print('ONLY MENTAL MATHS!!!!!')

    random_mul = random.randrange(0, 15)
    random_mul_2 = random.randrange(0, 15)
    print("1) Multiplying: ")
    multiply = int(input("What is {} * {}: ".format(random_mul, random_mul_2)))
    if multiply == random_mul * random_mul_2:
        print(correct)
        mm = mm + 1
    else:
        print(wrong, " , the right answer was: ", random_mul - random_mul_2)

    random_div_ans = random.randrange(0, 12)
    random_div_2 = random.randrange(0, 12)
    random_div = random_div_2 * random_div_ans
    print("2) Dividing: ")
    divide = int(input("What is {} / {}: ".format(random_div, random_div_2)))
    if divide == random_div / random_div_2:
        print(correct)
        mm = mm + 1
    else:
        print(wrong, " , the right answer was: ", random_div_ans)

    random_add = random.randrange(0, 1000)
    random_add_2 = random.randrange(0, 1000)
    print("3) Adding: ")
    add = int(input("What is {} + {}: ".format(random_add, random_add_2)))
    if add == random_add + random_add_2:
        print(correct)
        mm = mm + 1
    else:
        print(wrong, " , the right answer was: ", random_add - random_add_2)

    random_sub = random.randrange(0, 1000)
    random_sub_2 = random.randrange(0, 1000)
    print("4) Subtracting: ")
    subtraction = int(input("What is {} - {}: ".format(random_sub, random_sub_2)))
    if subtraction == random_sub - random_sub_2:
        print(correct)
        mm = mm + 1
    else:
        print(wrong, " , the right answer was: ", random_sub - random_sub_2)

    mmperc = ((mm / 4) * 100)
    print("Your percentage for mental maths is ", mmperc, '%')


def written_maths():
    print("YOU CAN USE PAPER NOW FOR WORKING OUT!!!")
    wm = 0
    rand_mul = random.randrange(0, 100)
    rand_mul_2 = random.randrange(0, 100)
    print("1) Multiplication: ")
    multi = int(input("What is {} * {}: ".format(rand_mul, rand_mul_2)))
    if multi == rand_mul * rand_mul_2:
        print(correct)
        wm = wm + 1
    else:
        print(wrong, " , the right answer was: ", rand_mul * rand_mul_2)

    rand_div_ans = random.randrange(0, 100)
    rand_div_2 = random.randrange(0, 100)
    rand_div = rand_div_2 * rand_div_ans
    print("2) Division: ")
    div = int(input("What is {} / {}: ".format(rand_div, rand_div_2)))
    if div == rand_div / rand_div_2:
        print(correct)
        wm = wm + 1
    else:
        print(wrong, " , the right answer was: ", rand_div_ans)

    rand_add = random.randrange(0, 10000)
    rand_add_2 = random.randrange(0, 10000)
    print("3) Addition: ")
    add = int(input("What is {} + {}: ".format(rand_add, rand_add_2)))
    if add == rand_add + rand_add_2:
        print(correct)
        wm = wm + 1
    else:
        print(wrong, " , the right answer was: ", rand_add * rand_add_2)

    rand_sub = random.randrange(0, 10000)
    rand_sub_2 = random.randrange(0, 10000)
    print("4) Subtraction: ")
    sub = int(input("What is {} - {}: ".format(rand_mul, rand_mul_2)))
    if sub == rand_sub - rand_sub_2:
        print(correct)
        wm = wm + 1
    else:
        print(wrong, " , the right answer was: ", rand_sub * rand_sub_2)

    wmperc = ((wm / 4) * 100)
    print("Your percentage for working out maths is ", wmperc, '%')


def maths():
    mental_maths()
    print()
    print("Now for working out maths :)")
    written_maths()


def periodtable():
    period = {}
    period["H"] = "Hydrogen"
    period["Na"] = "Sodium"
    period["Mg"] = "Magnesium"
    period["K"] = "Potassium"
    period["Ra"] = "Radium"
    period["Ti"] = "Titanium"
    period["Fe"] = "Iron"
    period["Ag"] = "Silver"
    period["Cu"] = "Copper"
    period["Co"] = "Cobalt"
    period["Zn"] = "Zinc"
    period["C"] = "Carbon"
    period["N"] = "Nitrogen"
    period["O"] = "Oxygen"
    period["S"] = "Sulphur"
    period["Al"] = "Aluminium"
    period["Pd"] = "Palladium"
    for i in range (0,15):
        index = random.randrange(0, len(period))
        element = list(period.keys())[index]
        h = input("What is '{}' in the periodic table? ".format(element))
        if h == period[element]:
            print(correct)
        else:
            print(wrong)

def english():
    nouns = [""]

print('The following quizes you will be tested on will be on different subjects.')
print('Always after a question a tick or a cross will be shown.')
print('This way you know if it is right or wrong.')
print('At the end of the subject there will be a percentage of right answers which you answered.')
print('This is all from me... enjoy :)')
select = input('Pick a subject to be tested on: a) Maths, b) Periodic table, c) ')
if select == "a":
    maths()
if select == "b":
    periodtable()

if select == "c":
    english()
