from functools import reduce

dic = {}  # the dictionary in which the patient's names will be hold
dic2 = {}
lst = []  # list to hold each patient's 12-hour blood glucose values
name = ''  # key of the dictionary which the patient's name will saved
lst2 = []

lst_ = []
doses = []
lst3 = []


def fun():  # function take the patient's name, blood values
    global lst
    global name
    global lst2
    global lst_
    global doses
    global lst3
    sub = []
    name = input("Enter patient name:")
    lst = list(map(int, input("Enter patient's 12-hour blood glucose values:").split(" ")))
    dic[name] = lst
    lstfil = list(filter(calc, lst))  # filter function to hold the glauce values over 120 on list
    print("Glucose values over 120 mg/dl :", lstfil)

    lst_length = len(lstfil)
    i = 0
    while i in range(lst_length):
        x = lstfil[i]
        overdose = x - 120
        sub.append(overdose)
        i += 1
    times = int(input("How many times did you take insulin in 12 hours? :"))
    doses = list(map(int, input("Enter insulin doses:").split()))
    # use of map and split to take the input on a sing line
    total = reduce(sum, doses)
    calculate(total, sub, lstfil, name)


def calc(a):  # calc function to calculate the return the values over 120
    if a > 120:
        return True
    else:
        return False


def sum(x1, x2):  # sum function of reduce to return the sum of 12 hour insulin doses
    return x1 + x2


def calculate(tot, lst_2, lst_3, name):  # calculate function to take the amount of unisilin with 1800/total formula
    lst3 = []
    low_bs = 1800 / tot
    lst_2_length = len(lst_2)
    for i in range(lst_2_length):
        need = lst_2[i] / low_bs
        lst3.append(round(need, 2))
        dic2[name] = (lst3, lst_3)


j = 0
while j in range(5):  # to print each patient's blood glucose levels from the dictionary
    fun()
    j += 1
print("12-hour blood glucose values of patients in service:\n", dic)
for name, g in dic2.items():
    print(name, "should take")
    for c in range(len(g[0])):  # to print how much insulin should any patient take based on the calculations
        print(g[0][c], "unit insulin for", g[1][c], "mg/dl")

print("**************************** End of the Program **********************")
# End of the program
