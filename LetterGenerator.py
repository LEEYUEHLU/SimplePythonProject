import random
pitch_of_names = ["C", "D", "E", "F", "G", "A", "B"]
names_of_notes = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Xi"]
score = 0
total_question_numbers = 3
question = list()
isLeave = False

def main():
    global  isLeave
    while(isLeave  == False):
        print("test")
        DisplayQuestion()
        PrepareQuestion()
        AskQuestion()
        Score()
        DeterminIfLeave()

def DeterminIfLeave():
    global isLeave
    isLeave = True if input("are you want to quit?(Yes/No)") == "Yes" else False

def DisplayQuestion():
    print("############################################################")
    global  total_question_numbers
    total_question_numbers = random.randrange(3,5)
    print("Here comes the " + str(total_question_numbers)+ " question\n")

def AskQuestion():
    question_number = 1
    for question_to_ask in question:
        print(str(question_number)+")"+"what is name of note " + question_to_ask + "?")
        anwser = input("anwser:")
        Examine(question_to_ask, anwser)
        question_number+=1

def PrepareQuestion():
    global  total_question_numbers
    global  question
    global  score
    score = 0
    question.clear()
    for i in range(total_question_numbers):
        length = len(pitch_of_names)
        letter = pitch_of_names[random.randrange(0, length)]
        question.append(letter)

def Examine(questioning_pitch_name, name_of_note):
    if (name_of_note not in names_of_notes):
        print("wrong! please give me one of the following name " + str(names_of_notes) + "\n")
        return
    if(pitch_of_names.index(questioning_pitch_name) == names_of_notes.index(name_of_note)):
        print("you got the right anwser!\n")
        global  score
        score += 1
    else:
        print(pitch_of_names.index(questioning_pitch_name))
        print("wrong! the right anwser is :" + names_of_notes[pitch_of_names.index(questioning_pitch_name)] + "\n")
def Score():
    print("You got " + str(score) + " out of " + str(total_question_numbers))

main()
