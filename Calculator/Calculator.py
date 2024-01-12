"""
@Author : Bharat Kshirsagar
@Date : 09/01/2024
@Goat : To make a Calculator which perform the basic arithmetic operations

"""
import sys

def add(num1, num2)->float:
    """
    addition
    """
    return num1 + num2

def sub(num1, num2)->float:
    """
    subtraction
    """
    return num1 - num2

def multi(num1, num2)->float:
    """
    multiplication
    """
    return num1 * num2


def div(num1, num2)->float:
    """
    Divison
    """
    return num1 / num2


def power(num1, num2)->float:
    """
    Power
    """
    return num1 ** num2

def modules(num1, num2)->float:
    """
    modules
    """
    return num1 % num2



def Calculator(Oper1: float|int,
               Sym: str,
               Oper2: float|int
               )->float:
    """
    These it the calculator function which perform the basic arithmetic operations
    like, addition, multiplication, subtraction, division, power, modules, Sq.root
    """
    # typechecks
    if type(Oper1) != float and type(Oper1) != int:
        raise TypeError("Bad type: it should be int or float")
    
    if type(Oper2) != float and type(Oper2) != int:
        raise TypeError("Bad type: it should be int or float")

    if type(Sym) != str:
        raise TypeError("bad type: it should be str ")
    
    if Sym == "+":
        return add(Oper1, Oper2)

    elif Sym == "-":
        return sub(Oper1,Oper2)
    
    elif Sym == "*":
        return multi(Oper1, Oper2)

    elif Sym == "/":
        return div(Oper1, Oper2)

    elif Sym == "^":
        return power(Oper1, Oper2)
              
    elif Sym == "%":
        return modules(Oper1, Oper2)
              
    else:
        print("enter the valid Operator")
        sys.exit(-1)
    
        

def main()->None:

    """
    It is the main function form there execution starts
    """


    while(True):

        num1 = float(input("Enter Operant1: "))
        Operator = input("Enter Operator: ")
        num2 = float(input("Enter Operant2: "))
        

        result = Calculator(num1, Operator, num2)
        print("The result of operation is : {}".format(result))

        terminate = input("if you want to terminate press Y/y: ")
        if(terminate == 'Y' or terminate == 'y'):
            break

    sys.exit(0)

main()