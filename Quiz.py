#Yang Letain 26/3/30 This is a program for quiz, Amimal quiz
import RPI.GPIO as GPIO
import time 
# NUIST Quiz Game in Python
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")
    # Questions and Answers
    questions = [
        "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat\n",
        "2. Which bird can fly backwards?: a. Cuckoo,b.Eagle, c.Hummingbird\n",
        "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c.Dolphin\n"
    ]
    answers = [
        "blue whale",
        "hummingbird",
        "bat"
    ]
    score = 0
    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
	    GPIO.output(18,GPIO.HIGH)
	    time.sleep(1)
	    GPIO.output(18,GPIO.LOW)
        else:
            print("Incorrect!")
	    GPIO.output(23,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(23,GPIO.LOW)
    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
quiz()
