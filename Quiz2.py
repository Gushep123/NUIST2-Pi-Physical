
#Yang Letain 26/4/2 This is a program for quiz, python quiz
import RPi.GPIO as GPIO
import time 
# NUIST Quiz Game in Python
def quiz():
	print("Welcome to the Python Knowledge Quiz!")
	print("Answer the following questions(only a,b,c):")
	# Questions and Answers
	questions = [
        "1. Which of the following is not a python data type?:\n a. int, b. float, c. rational, d. string e. bool \n",
        "2. Which of the following is not a built-in-operation in python?:\n a. +,b.%, c.abs() d.sqrt()\n",
        "3. In a mixed type expression involing ints and floats, python will convert:\n a.floats to ints, b. ints to strings, c.floats and ints to strings d.ints to floats\n",
	"4.The best structure for implementing a multi-way decision in python is:\n a.if b.if-else c.if-elif-else d.try\n",
	"5.What statement can be excuted in the body of a loop to cause it to terminate?\n a.if b.exit c.continue d.break\n"
	]
	answers = [
        "c",
        "d",
        "d",
	"c",
	"d"
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
			GPIO.output(17,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(17,GPIO.LOW)
			# Provide final score
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
quiz()
