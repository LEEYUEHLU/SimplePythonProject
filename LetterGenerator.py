import random
pitch_of_names = ["C", "D", "E", "F", "G", "A", "B"]
names_of_notes = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Xi"]
score = 0
total_question_numbers = 3
question = list()

def main():
    DisplayQuestion()
    PrepareQuestion()
    AskQuestion()
    Score()

def DisplayQuestion():
    print("############################################################")
    print(", ".join(pitch_of_names) + " are names of notes in guitar")
    print("followed by " + ", ".join(names_of_notes) + " respectively")
    print("############################################################\n")
    print("Here comes the " + str(total_question_numbers)+ " question\n")

def AskQuestion():
    question_number = 1
    for question_to_ask in question:
        print(str(question_number)+")"+"question: " + question_to_ask)
        anwser = input("anwser:")
        Examine(question_to_ask, anwser)
        question_number+=1

def PrepareQuestion():
    for i in range(total_question_numbers):
        length = len(pitch_of_names)
        letter = pitch_of_names[random.randrange(0, length)]
        question.append(letter)

def Examine(questioning_pitch_name, name_of_note):
    if(pitch_of_names.index(questioning_pitch_name) == names_of_notes.index(name_of_note)):
        print("you got the right anwser!")
        global  score
        score += 1
    else:
        print(pitch_of_names.index(questioning_pitch_name))
        print("wrong! the right anwser is :" + names_of_notes[pitch_of_names.index(questioning_pitch_name)])
def Score():
    print("You got " + str(score) + " out of " + str(total_question_numbers))

main()