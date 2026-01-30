print("Wellcome to quiz game !!")
print("NOTE: if your spelling is incorrect then it is considered as wrong answer")
score = 0
question_no = 0
playing = input("Do you want to play ? ").lower()
if playing == "yes":
    question_no += 1
    ques = input(f"\n{question_no}. what is 1+1? ").lower()
    if ques == "2":
        score += 1
        print("correct! you got 1 point")

    else:
        print("Incorrect!")
        print(f"current answer is --> 2 you FOOL HA")

    # ------1
    question_no += 1
    ques = input(f"\n{question_no}. what is the volume of a Rect that is width 35 cm height 35cm and length 10cm.Type cm2? ").lower()

    if ques == "80 cm2":
        score += 1
        print("correct! you got 1 point")

    else:
        print("Incorrect!")
        print(f"current answer is --> APRIL FOOLS 80 cm2")

    # -----2
    question_no += 1
    ques = input(f"\n{question_no}. what does RAM stand for? ").lower()

    if ques == "random access memory":
        score += 1
        print("correct! you got 1 point")

    else:
        print("Incorrect!")
        print(f"current answer is --> random access memory")

    # -----3
    question_no += 1
    ques = input(f"\n{question_no}. what does PSU stand for? ").lower()

    if ques == "power supply unit":
        score += 1
        print("correct! you got 1 point")

    else:
        print("Incorrect!")
        print(f"current answer is --> power supply unit")

    # -----4
    question_no += 1
    ques = input(f"\n{question_no}. what does ROM stand for? ").lower()

    if ques == "read only memory":
        score += 1
        print("correct! you got 1 point")

    else:
        print("Incorrect!")
        print(f"current answer is --> read only memory")


# ------5

else:
    print("thankyou you are out of a game.")
    quit()

print(f"\nnumber of question is {question_no}")
print(f"your score is {score}")
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print("0% quetions are correct")

print(f"{percentage}% questions are correct.")