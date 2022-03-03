from sympy import *
import sympy as sym
from math import *
import statistics 
import re

previous = 0
run = True

print("Hello and welcome to this simple python command calculator")
print("Type 'quit' to quit the calculator!")

def meine_calculator():
    global run
    global previous
    global x, t, x2, y2, intey 

    x = Symbol('x') #Simple 
    #t = sym.cos(x**2) #chain 
    t = sym.Symbol('x')
    #p = sym.exp(x)*sym.cos(x) #Product 
    
    #Derivatives of multivariable function
    x2 , y2 = sym.symbols('x y')
    #m = x**4+x*y**4
    intex = symbols('x')




    
    equation = ""
    if previous == 0:
        equation = input("Type your math equation -> ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Come back whenever you feel you are stuck!")
        run = False
    elif equation =="clear":
        previous = 0    
        run = True 
    elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
        start_of_expr = equation.find('(')
        f = parse_expr(equation[start_of_expr+1:-1])
        
        if previous == 0:
            previous = f.diff(x) + f.diff(t) + \
                f.diff(y2) + f.diff(x2,y2) 
            #previous = 
            #previous = f.diff(p)
            #previous = 
            #previous = f.diff(x2,y2)
        else:
            previous += f.diff(x) + f.diff(t) + \
                f.diff(y2) + f.diff(x2,y2) 
            #previous += f.diff(t)
            #previous += f.diff(p)
            #previous += f.diff(y2)
            #previous += f.diff(x2,y2)
        
    elif equation[0:9] == "integral(" or equation[0:10] == "+integral(":

        opening_paren = equation.find("(")
        closing_paren = equation.find(")")

        elements = equation[opening_paren + 1: closing_paren]

        elements = elements.split(",")

        elements = [x.strip() for x in elements]

        integral = elements[0]
        variable = elements[1]
        lower = elements[2]
        upper = elements[3]

# from here you can actually calculate the integral
        intrwnum = integrate(integral,variable, upper, lower)

        
        if previous == 0:
            previous = intrwithnum 
        else:
            previous += intrwithnum 
    #Statistics 
    elif equation[0:5] == "mean(":
        sum_lst = equation[5:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        mean = sum(sum_lst ) / len(sum_lst )
        result = str(mean)
        #print(result)
        if previous == 0:
            previous = result 
        else:
            previous += result 

    ###############
    #mode 
    elif equation[0:7] == "median(":
        
        sum_lst = equation[7:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        #mean = sum(sum_lst ) / len(sum_lst )
        median = statistics.median(sum_lst)
        result = str(median)
        #print(result)

        ###############
        #Mode 
        #mode 
    elif equation[0:5] == "mode(":
        
        sum_lst = equation[5:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        #mean = sum(sum_lst ) / len(sum_lst )
        mode = statistics.mode(sum_lst)
        result = str(mode)
        #print(result)
        if previous == 0:
            previous = result 
        else:
            previous += result 

        ######################
        #multimode 
    elif equation[0:10] == "multimode(":
        
        sum_lst = equation[10:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        #mean = sum(sum_lst ) / len(sum_lst )
        mode = statistics.multimode(sum_lst)
        result = str(mode)
        #print(result)
        if previous == 0:
            previous = result 
        else:
            previous += result 
    ##################
    #range

    elif equation[0:6] == "range(":
        
        sum_lst = equation[6:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        #mean = sum(sum_lst ) / len(sum_lst )
        minimum = min(sum_lst )
        maximum = max(sum_lst )
        range = (maximum-minimum) 
        result = str(range)
        if previous == 0:
            previous = result 
        else:
            previous += result 
        #print(result)

    ##############
    #Standard deviation 

        
    elif equation[0:6] == "stdev(":
        
        sum_lst = equation[6:-1].split(",")
        sum_lst = [int(i) for i in sum_lst]
        standard_deviation = statistics.stdev(sum_lst)    
        result = str(standard_deviation)
        #print(result)
        if previous == 0:
            previous = result 
        else:
            previous += result 






    else:
        equation = re.sub('[A-Za-z:;.?,()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    meine_calculator()
