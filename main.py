def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = int(input("What's the first number? "))

    for operator in operations:
        print(operator)
    oper = input("Choose symbol above that what d'you wanna do?  ")
    num2 = int(input("What's the second number? "))

    calculation = operations[oper]
    answer = calculation(num1, num2)

    print(f"{num1} {oper} {num2} = {answer} \n \n ")

    is_finished = False
    while not is_finished:
        ask = input("Do you want to compute again? Type 'y' to continue or 'n' to finish:  ")
        if ask == 'y':
            oper = input("pick an operator: ")
            num3 = int(input("What's the next number? \n"))
            calculation = operations[oper]
            answer = calculation(answer, num3)
            print(f"{answer} {oper} {num3} = {answer} \n")
        elif ask == 'n':
            is_finished = True
            calculator()
        else:
            print("You have inserted unexpected string!")
            is_finished = True
calculator()
