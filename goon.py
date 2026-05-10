print("Hello, welcome to my brawl stars game show!")
print("We will start our game show with some easy questions...then some hard ones!!!")

def ask_question(question, answer):
    user_answer = input(f"{question} ").strip().lower()
    if user_answer == answer.lower():
        print("Nice, that's correct!")
        return 1 
    else:
        print(f"Not quite, the answer was {answer}.")
        return 0 
def show_score(user_score, total_questions):
    percentage = (user_score / total_questions) * 100
    print(f"The game show is over. Your total score was {percentage}%")

def rundaquiz():
    score = 0
    questions = [
        ("What is the starter brawler?", "Shelly"),
        ("What is the MOST no skill brawler in the game", "Edgar"),
        ("What brawler was just recently released?", "Damian"),
        ("What brawler starts with the letter L and has the star power Spiky?", "Lily"),
        ("Which limited time brawler came into the game during late 2024 and early 2025?", "Buzz Lightyear"),
        ("Does Ethan have more trophies than me in brawl stars, yes/no?", "Yes"),
        ("What brawler just recently got his gadget removed? (Hint, it helped him charge his gadget)", "Edgar"),
        ("Who is the best support brawler in the game? (Hint, it is a mythic brawler)", "Doug"),
        ("What brawler gives the title, Bro (Hint, its a legendary brawler)", "Surge"),
        ("Final Question, what title does prestige one bibi give ", "Cool Cat")
    ]
    
    total = len(questions)
    
    for q, a in questions:
        score += ask_question(q, a)
        
    show_score(score, total)


rundaquiz()