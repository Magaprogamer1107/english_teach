from random import randint
import random
db = {"orange": "апельсин", "apple": "яблоко", "grape":"виноград",
      "pink":"розовый", "flag":"флаг", "domino":"", "country":"страна",
      "crow":"ворон", "pain":"боль", "glasses":"очки", "jump":"прыжок",
      "shoe":"кросовок", "runner":"бегун", "society":"общество", "frog":"лягушка",
      "frend":"друг", "land":"земля", "sand":"песок", "candy":"конфета", "shady":"сомнительный",
      "orange": "апельсин", "apple": "яблоко", "july": "июль", "four": "четыре", "march": "март",
      "book": "книга", "pear": "груша", "pineapple": "ананас", "car": "машина", "ereser": "резинка",
      "mountain": "гора", "floor": "пол", "neighbour": "сосед", "dour": "дверь", "box": "коробка",
      "wall": "стена", "ball": "мяч", "color": "цвет", "boy": "мальчик", "inc": "чернила"
}
db_sentence = {"right": "You guessed , you spent 6 tries",
               "choose": " variance follow",
               "name": "my  is Max",
               "eated": "I  apple",
               "buys": "My friend __ a black phone"}
def write_score(name, point):
    """
    :param name: name player
    :param point: score
    :return: None
    """
    path = "file_of_scores.txt"
    with open(path, "r") as f:
        d = f.readlines()
    is_add = False
    for i in range(len(d)):
        if name in d[i]:
            new_point = int(d[i].split("-")[1]) + point
            d[i] = name + " - " + str(new_point) + "\n"
            is_add = True
            break

    if not is_add:
        text = name + " - " + str(point) + "\n"
        d.append(text)

    text = ""
    for line in d:
        text += line

    with open(path, "w") as f:
        f.write(text)

def show_helps(letters, word):
    show = []
    for i in range(len(db[word])):
        show.append('_ ')
    for x in letters:
        show[x] = db[word][x]
    show_letters = ""
    for i in show:
        show_letters += i
    return show_letters
def guess_word_by_variance(word):
    """mode 1"""
    max_XP = 5
    print(word, "in english, choose variance follow")
    some_words = random.sample(list(db.values()), 4)
    some_words[randint(0, 3)] = db[word]
    print(some_words)
    while True:
        answer = input()
        if answer == db[word] or answer == str(some_words.index(db[word]) + 1):
            print("Excellent! You guessed right, you spent", str(5 - max_XP + 1), "tries")
            return max_XP
        else:
            print("Sorry, but you didn't guess right:( Try again")
            max_XP -= 1

def guess_word_by_sentence(word):
  XP = 0
  print("choose the correct option for this sentence: ", db_sentence[word])
  some_words = random.sample(list(db_sentence.keys()), 4)
  if word in some_words:
    print(some_words)
  else:
    some_words[randint(0, 3)] = word
    print(some_words)
  while True:
    answer = input(': ')
    if answer == word or answer == str(some_words.index(word) + 1):
      XP += 5
      print("Congratulation! You guessed right, you spent", str(XP), "tries")
      break
    else:
      print("Sorry, but you didn't guess right:( Try again")
  return XP
def guess_word(word):
    max_XP = 10
    help_letters = []
    while True:
        print(word, "in russian")
        answer = input("")
        if answer == db[word]:
            print("Excellent! You guessed right")
            return max_XP
        else:
            ran = randint(0, len(db[word])-1)
            if ran in help_letters:
                ran = randint(0, len(db[word])-1)
            help_letters.append(ran)
            print("Sorry, but you didn't guess right:( Try again")
            print(show_helps(help_letters, word))
            if max_XP > 0:
                max_XP -= 1
def load_db():
    """load database from txt file
    path_db - path to txt file"""
    path_db = "db_en_ru" # for Andy and Andemir
    db = {}
    with open(path_db, "r") as f:
        k = f.read()
    c = k.split('\n')
    for i in c:
        kluch = i.split('-')[0]
        znach = i.split('-')[1]
        db[kluch] = znach
    return db

if __name__ == "__main__":
    print("Hello! what's your name?")
    name = input(" ")
    XP = 0
    db = load_db()
    while True:
        print("\nwhat mode do you prefer? \nwrite 1 if guess word by variance, write 2 if guess word by letters, write exit to close program")
        mode = input()
        if mode == '1':
            tasks = random.sample(db.keys(), 5)
            for word in tasks:
                XP += guess_word_by_variance(word)
        elif mode == '2':
            tasks = random.sample(db.keys(), 5)
            for word in tasks:
                XP += guess_word(word)
        elif mode == '3':
            tasks = random.sample(db_sentence.keys(), 5)
            for word in tasks:
                XP += guess_word_by_sentence(word)
        elif mode == "exit":
            break
        print("Congratulations! You scored {} XP".format(XP))

    write_score(name, XP)




