"""
The goal of this game is to random generate different opereation
between 2 number randomly selected and ask you the reponse
Then give you a score and made give you a feedback
"""

import random

NUMBER_MIN = 1
MUMBER_MAX = 10
NUMBER_QUESTION = 4

# Define the question
def ask_question():
    a = random.randint(NUMBER_MIN , MUMBER_MAX)
    b = random.randint(NUMBER_MIN , MUMBER_MAX)
    o = random.randint(0,2)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    elif o ==2:
        operator_str = "-"
    response_str = input(f"Calculate : {a} {operator_str} {b} = ")
    response_int = int(response_str)
    ans = a+b
    if o == 1:
        ans = a*b
    elif o == 2:
        ans == a-b
    if response_int == ans:
        return True
    
    return False

score_sum = 0
# Ask the question
for i in range(0,NUMBER_QUESTION):
    print(f"Question number {i+1} in {NUMBER_QUESTION}")
    if  ask_question():
        print("Correct answer")
        score_sum +=1
    else:
        print("Wrong answer")
    print()
     

print(f"Your final score is {score_sum}/{NUMBER_QUESTION}")

if score_sum == NUMBER_QUESTION:
    print("Excelent")
elif score_sum == 0:
    print("Review your math")
elif score_sum > int(NUMBER_QUESTION/2):
    print("Not Bad")
else:
    print("Can improve")
