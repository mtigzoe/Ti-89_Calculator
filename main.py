# import math and cmath

from math import *

from cmath import *
from sympy.solvers import solve
from sympy import * 
from statistics import * 
from sympy.matrices import Matrix
import UserGuide 

previous = 0

modes_history = []



# function to list modes

def mode_menu():

    print("Text-based calculator\n")

    print("Calculator Modes:\n") 

    print("R) real") 

    print("C) complex") 

    print("D) derivative")
    print("I) integral") 

    print("S) statistics") 
    print("A) Algebra")
    print("U) User Guides")
    print("Q) Quit")


#derivative menu 
def derivative_menu(): 
    print("1. Simple Rule")
    print("2. Power Rule")
    print("3. Product Rule")
    print(" 4. Quotient Rule")
    print("5. Chain Rule")
    print("6. Exponential")
    print("7. Partial Rule")
    print("8. Multivariable Rule")
    

def algebra_solver_menu(): 
    print("Algebra Solver")    
    print("1. One variable")
    print("2. Two variables")
    print("3. Three variables")

#User Guide Menu 
def UserGuideMenu(): 
    print("\nUser Guide Menu\n")
    print("R) Real Number User Guide")
    print("D) Derivative User Guide")
    print("I) Integral User Guide")
    print("S) Statistics User Guide")
    print("A) Algebra User Guide")

#Keep mode history under 100 entries
def trim_mode_history():
    modes_history.pop() if len(modes_history) > 99 else None

# mode selection function
def mode_selection_function():

    while True:
        trim_mode_history()
        
        mode_selection = input("Which calculator mode would you like to use? ")

        if mode_selection == "r":
            calculateRealMode()
        elif mode_selection == "c":    
            calculateComplex()
        elif mode_selection == "d":
            derivative_menu_with_selections()
        elif mode_selection == "i":
            integral_mode()    
        elif mode_selection == "s":
            statistics_mode()
        elif mode_selection == "a":
            algebra_menu_with_selection()
        elif mode_selection == "m":
            matrix_function()    
        elif mode_selection == "u":
            UserGuideswithSelection()    
        elif mode_selection == "options":

            mode_menu()

        else: 

            exit()


#Selection for derivative rules 
def derivative_rules_selection():
    derivative_selection = input("What derivative rule would you like to choose")
    if derivative_selection == "simple": 
        simple_derivative() 
    elif derivative_selection == "power":
        power_derivative()
    elif derivative_selection == "product": 
        product_derivative()
    elif derivative_selection == "quotient":
        quotient_derivative()
    elif derivative_selection == "chain":
        chain_derivative()
    elif derivative_selection == "exponential":
        exponential_derivative()
    elif derivative_selection == "partial":
        partial_derivative() 
    elif derivative_selection == "multivariable": 
        multivariable_derivative()
    elif derivative_selection == "options":    
        mode_menu()
    elif derivative_selection == "switch":
        mode_selection_function() 
    elif derivative_selection == "derivative options":    
        derivative_menu()
    elif derivative_selection == "derivative switch":    
        derivative_rules_selection()
    else: 
        exit() 


def algebra_mode_selection(): 
    print("\nAlgebra solver\n")
    algebra_selection = input("What kind of algebra solver would you like to choose?")
    if algebra_selection == "1": 
        algebra_onevariable() 
    elif algebra_selection == "2":
        algebra_twovariables()
    elif algebra_selection == "3":  
        algebra_threevariables()
    elif algebra_selection == "4":
        simplify_factor()   
    else: 
        exit()


def UserGuide_Selection():
    UserGuideOptions = input("Which user guide would you like to read?")
    if UserGuideOptions== "r":
        
        UserGuide.RealNumberInstructions()
    elif UserGuideOptions== "d": 
        
        UserGuide.DerivativesInstructions()
    elif UserGuideOptions == "i":
        
        UserGuide.IntegralInstructions()
    elif UserGuideOptions== "s":
        UserGuide.StatisticsInstructions()    
    elif UserGuideOptions == "a":
        UserGuide.AlgebraInstructions()
    elif UserGuideOptions == "switch":    
        UserGuideswithSelection()
    else: 
        exit()    

#The function prints the derivative menu with selections 
def derivative_menu_with_selections():
    derivative_menu()
    derivative_rules_selection()

def algebra_menu_with_selection():
    algebra_solver_menu()
    algebra_mode_selection()
#User Guides with Selections 
def UserGuideswithSelection():
    UserGuideMenu()
    UserGuide_Selection()
# calculator for real numbers

def calculateRealMode():

    global previous

    run_real_mode = True

    modes_history.append("Real Mode")

    print("\nReal Mode\n")



    # loop the real number calculator until user quits or switches modes

    while run_real_mode:

        

        if previous == 0:

            equation = input("Type your REAL calculation -> ")

        else:

            equation = input(str(previous))



        if equation == "quit":

            print("Come back soon!")

            run_real_mode = False

            

        elif equation =="clear":

            previous = 0

            

        elif equation == "switch":

            previous = 0

            run_real_mode = False

            

        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)



            previous = previous.real



# calculator for complex numbers

def calculateComplex():

    global previous

    run_complex_mode = True

    modes_history.append("Complex Mode")

    print("\nComplex Mode\n")



    # loop the complex number calculator until user quits or switches modes

    while run_complex_mode:

        

        if previous == 0:

            equation = input("Type your COMPLEX calculation -> ")

        else:

            equation = input(str(previous))



        if equation == "quit":

            print("Come back soon!")

            run_complex_mode = False

            

        elif equation =="clear":

            previous = 0

            

        elif equation == "switch":

            previous = 0

            run_complex_mode = False

            

        else:

            if previous == 0:

                previous = eval(equation)

                previous = complex(previous)

            else:

                previous = eval(str(previous) + equation)



def simple_derivative(): 
    print("\nSimple Mode\n")
    x = Symbol('x') 
    global previous
    run_simple_mode = True

    modes_history.append("Simple Mode")

    
    
    while run_simple_mode:        

        if previous == 0:

            equation = input("Type your SIMPLE expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_simple_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_simple_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def power_derivative(): 
    print("\nPower Mode\n")
    x = Symbol('x') 
    global previous
    run_power_mode = True

    modes_history.append("Power Mode")
    
   
    while run_power_mode:        

        if previous == 0:

            equation = input("Type your POWER expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_power_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_power_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def product_derivative():
    print("\nProduct Mode\n")
    x = Symbol('x') 
    global previous
    run_product_mode = True

    modes_history.append("Product Mode")
    
   
    while run_product_mode:        

        if previous == 0:

            equation = input("Type your PRODUCT expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_product_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_product_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def quotient_derivative():
    print("\nQuotient Mode\n")
    x = Symbol('x') 
    global previous
    run_quotient_mode = True

    modes_history.append("Quotient Mode")
    
   
    while run_quotient_mode:        

        if previous == 0:

            equation = input("Type your QUOTIENT expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_quotient_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_quotient_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def chain_derivative():
    print("\nChain Mode\n")
    x = Symbol('x') 
    global previous
    run_chain_mode = True

    modes_history.append("Chain Mode")
    
   
    while run_chain_mode:        

        if previous == 0:

            equation = input("Type your CHAIN expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_chain_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_chain_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def exponential_derivative():
    print("\nexponential Mode\n")
    x = Symbol('x') 
    global previous
    run_exponential_mode = True

    modes_history.append("Exponential Mode")
    
   
    while run_exponential_mode:        

        if previous == 0:

            equation = input("Type your EXPONENTIAL expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_exponential_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_exponential_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def partial_derivative():
    print("\nPartial Mode\n")
    x, y = symbols('x y')

    global previous
    run_Partial_mode = True

    modes_history.append("Partial Mode")
    
   
    while run_Partial_mode:        

        if previous == 0:

            equation = input("Type your PARTIAL expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_Partial_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_Partial_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)


#multivariable function
def multivariable_derivative(): 
    print("\nMultivariable Mode\n")
    x, y = symbols('x y')

    global previous
    run_multivariable_mode = True

    modes_history.append("Multivariable Mode")
    
   
    while run_multivariable_mode:        

        if previous == 0:

            equation = input("Type your MULTIVARIABLE expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_multivariable_mode = False            

        elif equation =="clear":

            previous = 0            

        elif equation == "switch":

            previous = 0

            run_multivariable_mode = False            
        #derivative 
        elif equation[0:6] == "deriv(" or equation[0:7] == "+deriv(":
            start_of_expr = equation.find('(')
            f = parse_expr(equation[start_of_expr+1:-1])
        
            if previous == 0:
                previous = f.diff(x) 
            
            else:
                previous += f.diff(x) 
        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

    
def integral_mode(): 
    print("\nIntegral\n")
    x, y = symbols('x y')

    global previous
    run_integral_mode = True

    modes_history.append("Integral Mode")
    
    while run_integral_mode:        

        if previous == 0:

            equation = input("Type your INTEGRAL expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_integral_mode = False            

        elif equation =="clear":

            previous = 0            
        elif equation == "switch":

            previous = 0
            run_integral_mode = false;

        elif equation[0:9] == "integral(" or equation[0:10] == "+integral(":        
            
            opening_paren = equation.find("(")
            closing_paren = equation.rfind(")")
            elements = equation[opening_paren + 1: closing_paren]
            elements = elements.split(",")
            elements = [x.strip() for x in elements]

            integral = elements[0]
            variable = parse_expr(elements[1])

            # indefinite
            if len(elements) == 2:
  
                resultwithoutlh = integrate(integral, variable)

                if previous == 0:
                    previous = resultwithoutlh        
                else:
                    previous += resultwithoutlh
                

            elif len(elements) == 4:
                lower = elements[2]
                upper = elements[3]
                resultwlh = integrate(integral, (variable, lower, upper)) 

                if previous == 0:
                    previous = resultwlh        
                else:
                    previous += resultwlh


        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def statistics_mode(): 
    print("\nStatistics\n")

    global previous

    run_statistics_mode = True

    modes_history.append("Statistics Mode")


    while run_statistics_mode:
        
        if previous == 0:

            equation = input("Type your statistics calculation -> ")

        else:

            equation = input(str(previous))



        if equation == "quit":

            print("Come back soon!")

            run_statistics_mode = False
            
        elif equation =="clear":

            previous = 0
        elif equation == "switch":

            previous = 0
            run_statistics_mode = false 
            
        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)
    
def algebra_onevariable(): 

    print("\n Algebra Solver One Variable\n")
    x = Symbol('x')

    global previous
    run_algebra_onevariable_mode = True 

    modes_history.append("Algebra Solver One Variable Mode")
    
    while run_algebra_onevariable_mode:        

        if previous == 0:

            equation = input("Type your Solver expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_algebra_onevariable_mode = False            

        elif equation =="clear":

            previous = 0            
        elif equation == "switch":
            previous = 0 
            run_algebra_onevariable_mode = false 
        elif equation[0:6] == "solve(" or equation[0:7] == "+solve(":
            
            opening_paren = equation.find("(")
            closing_paren = equation.find(")")
            elements = equation[opening_paren + 1: closing_paren]
            elements = elements.split(",")
            elements = [x.strip() for x in elements]
            print(elements)
            algebra_equation = elements[0]
            variable = parse_expr(elements[1])
            
            solver = solve(algebra_equation, (variable)) 
            print(solver)
            if previous == 0:

                equation = input("Type your Solver expression -> ")

            else:

                equation = input(str(previous))
                    
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)

def algebra_twovariables():
    print("Algebra Solver with Two Variables")    
    x, y = symbols('x y')

    global previous
    run_algebra_twovariables_mode = True

    modes_history.append("Algebra Solver Two Variable Mode")
    
    while run_algebra_twovariables_mode:        

        if previous == 0:

            equation = input("Type your Solver expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_algebra_twovariables_mode = False            

        elif equation =="clear":

            previous = 0            

        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)


def algebra_threevariables():
    print("Algebra Solver with Three Variables")    
    x, y, y = symbols('x y y')

    global previous
    run_algebra_threevariables_mode = True

    modes_history.append("Algebra Solver Three Variable Mode")
    
    while run_algebra_threevariables_mode:        

        if previous == 0:

            equation = input("Type your Solver expression -> ")

        else:

            equation = input(str(previous))

        if equation == "quit":

            print("Come back soon!")

            run_algebra_threevariables_mode = False            

        elif equation =="clear":

            previous = 0            

        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)


def simplify_factor():

    print("\nSimlify/Factor\n")
    x = symbols('x')

    global previous

    run_algebra_simplify_factor = True

    modes_history.append("Simplify Factor Mode")


    while run_algebra_simplify_factor:
        
        if previous == 0:

            equation = input("Type your Algebra equation -> ")

        else:

            equation = input(str(previous))



        if equation == "quit":

            print("Come back soon!")

            run_algebra_simplify_factor = False
            
        elif equation =="clear":

            previous = 0
            
        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)

def matrix_function():
    print("\nMatrix\n")
    
    global previous

    run_matrix_mode = True

    modes_history.append("Matrix Mode")


    while run_matrix_mode:
        
        if previous == 0:

            equation = input("Type your Matrix calculation -> ")

        else:

            equation = input(str(previous))



        if equation == "quit":

            print("Come back soon!")

            run_matrix_mode = False
            
        elif equation =="clear":

            previous = 0
            
        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)



if __name__ == "__main__":
    mode_menu()
    mode_selection_function()