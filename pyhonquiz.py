import random


correct: str = '✓'
wrong: str = 'X'


def mental_maths():
    score = 0
    print('ONLY MENTAL MATHS!!!!!')

    random_mul = random.randrange(0, 15)
    random_mul_2 = random.randrange(0, 15)
    print("1) Multiplying: ")
    multiply = int(input("What is {} * {}: ".format(random_mul, random_mul_2)))
    mul_correct_answer = random_mul * random_mul_2
    if multiply == mul_correct_answer:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", mul_correct_answer)

    random_div_ans = random.randrange(0, 12)
    random_div_2 = random.randrange(0, 12)
    random_div = random_div_2 * random_div_ans
    print("2) Dividing: ")
    divide = int(input("What is {} / {}: ".format(random_div, random_div_2)))
    if divide == random_div / random_div_2:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", random_div_ans)

    random_add = random.randrange(0, 1000)
    random_add_2 = random.randrange(0, 1000)
    print("3) Adding: ")
    add = int(input("What is {} + {}: ".format(random_add, random_add_2)))
    add_correct_answer = random_add + random_add_2
    if add == add_correct_answer:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", add_correct_answer)

    random_sub = random.randrange(0, 1000)
    random_sub_2 = random.randrange(0, 1000)
    print("4) Subtracting: ")
    subtraction = int(input("What is {} - {}: ".format(random_sub, random_sub_2)))
    sub_correct_answer = random_sub - random_sub_2
    if subtraction == sub_correct_answer:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", sub_correct_answer)

    print_score("mental math", score, 4)


def written_maths():
    print("YOU CAN USE PAPER NOW FOR WORKING OUT!!!")
    score = 0
    rand_mul = random.randrange(0, 100)
    rand_mul_2 = random.randrange(0, 100)
    print("1) Multiplication: ")
    multi = int(input("What is {} * {}: ".format(rand_mul, rand_mul_2)))
    if multi == rand_mul * rand_mul_2:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", rand_mul * rand_mul_2)

    rand_div_ans = random.randrange(0, 100)
    rand_div_2 = random.randrange(0, 100)
    rand_div = rand_div_2 * rand_div_ans
    print("2) Division: ")
    div = int(input("What is {} / {}: ".format(rand_div, rand_div_2)))
    if div == rand_div / rand_div_2:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", rand_div_ans)

    rand_add = random.randrange(0, 10000)
    rand_add_2 = random.randrange(0, 10000)
    print("3) Addition: ")
    add = int(input("What is {} + {}: ".format(rand_add, rand_add_2)))
    if add == rand_add + rand_add_2:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", rand_add + rand_add_2)

    rand_sub = random.randrange(0, 10000)
    rand_sub_2 = random.randrange(0, 10000)
    print("4) Subtraction: ")
    sub = int(input("What is {} - {}: ".format(rand_sub, rand_sub_2)))
    if sub == rand_sub - rand_sub_2:
        print(correct)
        score = score + 1
    else:
        print(wrong, " , the right answer was: ", rand_sub - rand_sub_2)

    print_score("working out math", score, 4)


def maths():
    mental_maths()
    print()
    print("Now for working out maths :)")
    written_maths()


def print_score(subject1: str, correct_answers: int, total_answers: int):
    percentage = ((correct_answers / total_answers) * 100)
    print("Your {} score is {}%.".format(subject1, percentage))


def periodic_table():
    # dictionary - curly brackets make a dictionary (key:value)
    table = {"H": "Hydrogen", "Na": "Sodium", "Mg": "Magnesium", "K": "Potassium", "Ra": "Radium",
                      "Ti": "Titanium",
                      "Fe": "Iron", "Ag": "Silver", "Cu": "Copper", "Co": "Cobalt", "Zn": "Zinc", "C": "Carbon",
                      "N": "Nitrogen", "O": "Oxygen", "S": "Sulphur", "Al": "Aluminium", "Pd": "Palladium"}
    score = 0
    questions = 15
    for i in range(0, questions):
        index = random.randrange(0, len(table))
        element = list(table.keys())[index]
        h = input("What is '{}' in the periodic table? ".format(element))
        if h.lower() == table[element].lower():
            print(correct)
            score = score + 1
        else:
            print(wrong)
            print("The correct answer was '{}'".format(table[element]))

        # https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary
        new_periodic_table = dict(table)
        del new_periodic_table[element]
        table = new_periodic_table

    print_score("chemistry", score, questions)


def synonyms():
    def insufficient() -> bool:
        syn = input("Insufficient: is it ... a)Unsatisfactory b)Angry c)Satisfactory : ")
        is_correct = syn == "a"
        print(correct if is_correct else wrong)
        return is_correct

    def hilarious() -> bool:
        syn = input("Hilarious: is it ... a)Melancholy b)Unhappy c)Amusing : ")
        is_correct = syn == "c"
        print(correct if is_correct else wrong)
        return is_correct

    def embarrass() -> bool:
        syn = input("Embarrass: is it ... a)Annoy b)Simplify c)Organise : ")
        is_correct = syn == "a"
        print(correct if is_correct else wrong)
        return is_correct

    def selective() -> bool:
        syn = input("Selective: is it ... a)Careless b)Choosy c)Judicious : ")
        is_correct = syn == "b" or "c"
        print(correct if is_correct else wrong)
        return is_correct

    def abject() -> bool:
        syn = input("Abject: is it ... a)Object b)Hopeless c)Fortunate : ")
        is_correct = syn == "b"
        print(correct if is_correct else wrong)
        return is_correct

    questions = [insufficient, hilarious, embarrass, selective, abject]
    score = 0
    total_questions = 3
    for i in range(0, total_questions):
        print("What is the synonym for:")

        random_question = random.randrange(0, 4)

        question = questions[random_question]
        was_correct = question()
        if was_correct:
            score = score + 1

    print_score("synonyms", score, total_questions)


print('This following quiz you will be tested on different subjects')
print('At the end of the subject there will be a percentage of right answers which you answered.')
print('This is all from me... enjoy :)')

while True:
    subject = input('Pick a subject to be tested on: a) Maths, b) Periodic table, c) Synonyms ')
    if subject.lower() == "a":
        maths()
    elif subject.lower() == "b":
        periodic_table()
    elif subject.lower() == "c":
        synonyms()
    else:
        print("I do not know what you mean by '{}', please try again.".format(subject))

    answer = input("Do you want to continue? (yes/no) ")
    if answer.lower() == "no":
        break
