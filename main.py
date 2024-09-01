import pyttsx3

questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "Php", 4],
    ["When was Java introduced?", "1994", "1995", "1876", "1877", 2],
    ["Who invented Python?", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "Donald Chamberlin", 1],
    ["Who invented Java?", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "Donald Chamberlin", 2],
    ["Who invented C++?", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "Donald Chamberlin", 3],
    ["When was ChatGPT launched?", "21 Oct 2021", "11 Nov 2022", "30 Nov 2022", "29 Nov 2020", 3],
    ["Who invented HTML?", "Tim Berners-Lee", "James Gosling", "Bjarne Stroustrup", "Donald Chamberlin", 1],
    ["Which language was used to create AI?", "Python", "French", "JavaScript", "Php", 1]
]

levels = [1000,2000,4000,8000,10000,20000,40000,80000,160000,320000]
checkpoint_levels = [1000,10000,320000]
money = 0
last_checkpoint = 0

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1

# Function to speak the question
def speak_question(question_info):
    question = question_info[0]
    print(question)  # Print the question on screen
    engine.say(question)  # Speak the question
    engine.runAndWait()

# To print Questions
for i in range(len(questions)):
    question_info = questions[i]
    print(f"Question for Rs. {levels[i]}")
    engine.say(f"Question for Rs. {levels[i]}")
    speak_question(question_info)  # Speak and print the question
    # To print Options
    for j in range(1, len(question_info)-1):
        print(f"{chr(96 + j)}. {question_info[j]}")
    reply = input("Enter your option (a-d): ").lower()
    correct_answer_index = question_info[-1]
    correct_answer = chr(96 + correct_answer_index).lower()
    # To check answer
    if reply == correct_answer:
        print(f"Correct Answer! You have Won Rs. {levels[i]}")
        money = levels[i]
        # For checkpoints
        for checkpoint in checkpoint_levels:
            if levels[i] >= last_checkpoint:
                last_checkpoint = checkpoint
        engine.say(f"Correct Answer! You have Won Rs. {levels[i]}")
    else:
        print("Wrong Answer!")
        if levels[i] > last_checkpoint:
            money = last_checkpoint
        engine.say("Wrong Answer!")
        break

print(f"Your take home money is {money}")
engine.say(f"Your take home money is {money}")
# Run and wait for the speech to finish
engine.runAndWait()