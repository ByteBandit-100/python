#quiz program
#author :: ByteBandit-100 (github)

questions = ('1. What is the capital of Australia?',
             '2. Which planet in our solar system is known for being the largest?',
             '3. Who painted the famous artwork "The Starry Night"?',
             '4. What is the chemical symbol for gold?',
             '5. Which author wrote the famous novel "To Kill a Mockingbird"?',
             '6. What is the world\'s largest living structure, according to the Guinness World Records?',
             '7. Which musician is often referred to as the "King of Rock and Roll"?',
             '8. What is the smallest country in the world, both in terms of population and land area?',
             '9. Who is credited with inventing the first practical light bulb?',
             '10. What is the highest mountain peak in the solar system?')
options = ("""A) Sydney\tB) Melbourne
C) Canberra\tD) Perth""",
"""A) Earth\tB) Saturn
C) Jupiter\tD) Uranus""",
"""A) Leonardo da Vinci\tB) Vincent van Gogh
C) Pablo Picasso\t\tD) Claude Monet
""",
"""A) Ag\tB) Au
C) Hg\tD) Pb""",
"""A) F. Scott Fitzgerald\tB) Harper Lee
C) Jane Austen\t\t\tD) J.K. Rowling""",
"""A) The Great Barrier Reef\tB) The Amazon Rainforest
C) The Grand Canyon\t\t\tD) The Great Wall of China""",
"""A) Chuck Berry\t\tB) Elvis Presley
C) Little Richard\tD) Jerry Lee Lewis""",
"""A) Vatican City\tB) Monaco
C) Nauru\t\tD) Tuvalu""",
"""A) Thomas Edison \tB) Alexander Graham Bell
C) Nikola Tesla \tD) Guglielmo Marconi""",
"""A) Mount Everest (Earth)\tB) Olympus Mons (Mars)
C) Denali (North America)\tD) Kilimanjaro (Africa)
""")
score = 0
guesses =["","","","","","","","","",""]
answers = ('c','c','b','b','b','a','b','a','a','b')
print("\n------------- x Welcome to quiz x ---------------")
name = input("Enter your name: ").capitalize()
if len(name) < 2 :
    print("Name not possible.")
    while len(name)<2:
        name = input("Enter your name: ").capitalize()
if len(name)>1:
    print(f'\nNo -ve marking.\nEmpty,wrong or multiple inputs and wrong answers are wrong.\nBest of Luck {name}👍\n')
    for i in range(len(questions)):
        print(questions[i])
        print(options[i])
        guesses[i] = input("Enter option for answer (a,b,c or d ): ").lower()
        if answers[i] == guesses[i]:
            score += 1
            print(f'Score : {score}/{len(questions)}\n')
        else:
            print("You gave incorrect answer....")
            print(f"The Correct answer is : {answers[i].upper()}\n")
            print(f'Score : {score}/{len(questions)}\n')
    if score<4:
        print(f'{name}, your score is {score}/{len(questions)} Not so good 😒 .')
    elif 4<=score<7:
        print(f'{name}, your score is {score}/{len(questions)} is good 😊 .')
    else:
        print(f'{name}, your score is {score}/{len(questions)} is so good 😎 .')