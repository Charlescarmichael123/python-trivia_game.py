#!/usr/bin/env python3

"""This is a trivia game where the user is asked a series of questions and must answer correctly to advance to the next level.

Each level consists of five multiple-choice questions. The user has three attempts to answer each question correctly. If they fail to do so, the game is over.

At the end of the game, the user's score is displayed along with their ranking.

"""

import random

# Define a list of questions, each with four possible answers and the index of the correct answer

questions = [

    {

        "question": "What is the capital of France?",

        "options": ["Paris", "Madrid", "Rome", "Berlin"],

        "answer": 0

    },

    {

        "question": "What is the largest planet in our solar system?",

        "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],

        "answer": 0

    },

    {

        "question": "Which city is home to the Eiffel Tower?",

        "options": ["London", "New York", "Paris", "Tokyo"],

        "answer": 2

    },

    {

        "question": "What is the name of the first man to walk on the moon?",

        "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"],

        "answer": 1

    },

    {

        "question": "What is the chemical symbol for gold?",

        "options": ["Au", "Ag", "Cu", "Pt"],

        "answer": 0

    }

]

# Define a function to ask a question and get the user's answer

def ask_question(question, options):

    print(question)

    for i, option in enumerate(options):

        print(f"{i+1}. {option}")

    answer = input("Enter the number of your answer (1-4): ")

    while not answer.isdigit() or int(answer) not in range(1, 5):

        answer = input("Invalid input. Enter the number of your answer (1-4): ")

    return int(answer) - 1

# Define a function to play a level of the game

def play_level(level):

    print(f"Level {level+1}:")

    score = 0

    for i in range(5):

        question = random.choice(questions)

        print(f"\nQuestion {i+1}:")

        answer = ask_question(question["question"], question["options"])

        attempts = 1

        while answer != question["answer"] and attempts < 3:

            print("Incorrect answer. Try again.")

            answer = ask_question(question["question"], question["options"])

            attempts += 1

        if answer == question["answer"]:

            print("Correct answer!")

            score += 1

        else:

            print(f"Incorrect answer. The correct answer was {question['options'][question['answer']]}.")

    return score

# Define a function to play the game

def play_game():

    print("Welcome to the Trivia Game!")

    score = 0

    for i in range(3):

        print(f"\nAttempt {i+1}:")

        level_score = play_level(i)

        score += level_score

        if level_score == 5:

            print("Congratulations! You have passed this level.")

        else:

            print("Sorry, you have failed this level.")

            break

    print(f"\nYour final score is {score} out of 15.")

    if score == 15:

        print("Excellent!

