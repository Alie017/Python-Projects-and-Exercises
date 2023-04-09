Dict_Students = {}  # Student dictionary
Answer_Key = ()
Students_Key = []


def exam_information(key):  # Function to get the necessary information
    for a in range(5):
        value_init = 0
        student_name = input("Enter name: ")
        student_last_name = input("Enter last name: ")
        student_answer = input(str("Enter answers: "))
        b = 0
        while b < 10:
            while key[b] == student_answer[b]:
                value_init = value_init + 10
                break
            b = b + 1
        Dict_Students[student_name, student_last_name] = value_init
        Students_Key.append(value_init)
        Answer_Key = tuple(Students_Key)  # Tuple of the key
        value_result = sum(Answer_Key)
    return value_result


def search_name():  # Function to search for student's grade based on the input
    search_student_name = input("Who are you searching for? ")

    for b in Dict_Students.keys():
        first_cond = b[1] == search_student_name
        second_cond = b[0] == search_student_name

        if second_cond == 1:
            print(b[0], "", b[1], "", "received", Dict_Students[b])

        elif first_cond == 1:
            print(b[0], "", b[1], "", "received", Dict_Students[b])


key_answerB = []
key_answerB = input(str("Enter answer key: "))
avarage_score = exam_information(key_answerB)
print("Student Dictionary:\n", Dict_Students)
print("Average: ", avarage_score / 5.0)  # Prints out the average score of the students
print("Students above average")
for z, value_student in Dict_Students.items():  # Loop for calculating the scores of students who are above average
    while value_student > (avarage_score / 5.0):
        print("Name:", z[1], "", ", ", z[0][0], ".", " Score:", value_student)
        break
search_name()  # Function call to execute search function x
print("**************************** Extra **********************")
search = True
while search:  # Extra : Asks user to search again if she/he wants to search for another student
    again = input("Do you want to search again ? (Press y to search again press n to finish the program )")
    if again == "y" or again == "Y":
        search_name()
    else:
        search = False
print("**************************** End of the Program **********************")
# End of the program
