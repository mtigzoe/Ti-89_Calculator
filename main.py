from math import *
from sympy import * 
#from sympy import Symbol, symbols, integrate
from statistics import * 
import UserGuide 
#from sympy import solve
from sympy.abc import x, y, z, a, b
from sympy.parsing.sympy_parser import parse_expr

previous = 0

# function to list modes


def mode_menu():

    print("\nText-based calculator\n")

    print("Calculator Modes:\n") 

    print("R) real")     
    print("D) derivative")
    print("I) integral") 
    print("S) statistics") 
    print("A) Algebra")
    print("U) User Guides")
    print("Q) Quit")

def derivative_menu(): 
    print("\nDerivative options\n")
    
    print("1) Power Rule")
    print("2) Product Rule")
    print("3) Quotient Rule")
    print("4) Chain Rule")    
    print("5) Partial Rule")
    print("6) Multivariable Rule")
    print("B) Back")
    
def algebra_solver_menu(): 
    print("\nAlgebra Options\n")    

    print("1) Solver")
    print("2) Factor")
    print("3) Simplify")    
    print("B) Back")

def UserGuideMenuSelectionDisplay(): 
    print("\nUser Guide Menu\n")
    
    print("R) Real Number User Guide")
    print("D) Derivative User Guide")
    print("I) Integral User Guide")
    print("S) Statistics User Guide")
    print("A) Algebra User Guide")
    print("H) How to use")
    print("B) Back")

def RealNumberInstructionsMenu(): 
    print("\nReal Number Functions\n")

    print("R) Representation")
    print("P) Power and logarithmic")
    print("T) Trigonometry")
    print("A) Angular Conversion")
    print("H) Hyperbolic")
    print("C) Constants")
    print("B) Back")
    

def         mode_selection_function():    


    while True:
        
        
        mode_menu()

        mode_selection = input("Which calculator mode would you like to use? ")
        mode_selection = mode_selection.lower() 
        mode_selection = mode_selection.strip()

        if mode_selection == "r" or mode_selection == "real":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in real number mode:\n")
            RealModeFunction()        
        elif mode_selection == "d" or mode_selection  == "derivative":
            derivative_menu()
            derivative_rules_selection()
            
        elif mode_selection == "i" or mode_selection  == "integral":
            
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in integral mode:\n")
            integral_mode()    
        elif mode_selection == "s" or mode_selection  == "statistics":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in statistics mode:\n")
            statistics_mode()
        elif mode_selection == "a" or mode_selection  == "algebra":
            
            algebra_solver_menu()
            algebra_mode_selection()

        elif mode_selection == "u" or mode_selection  == "user" or mode_selection  == "user guides":
            UserGuideMenuSelection()
        elif mode_selection == "q":
            exit()
        else: 
            continue 
                

        
#Selection for derivative rules 
def derivative_rules_selection():

    

    
    menu_back = False

    while menu_back == False:
        derivative_menu()

        derivative_selection = input("Select an option: ")
        derivative_selection = derivative_selection.lower() 
        derivative_selection = derivative_selection.strip()
        
        if derivative_selection == "power" or derivative_selection  == "1":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in power derivative mode:\n")
            simple_derivative()
        elif derivative_selection == "product" or derivative_selection  == "2": 
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in product derivative mode:\n")
            simple_derivative()
        elif derivative_selection == "quotient" or derivative_selection  == "3":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in quotient derivative mode:\n")
            simple_derivative()
        elif derivative_selection == "chain" or derivative_selection  == "4":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in chain derivative mode:\n")
            simple_derivative()        
        elif derivative_selection == "partial" or derivative_selection == "5":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in partial derivative mode:\n")
            multivariable_derivative() 
        elif derivative_selection == "multivariable" or derivative_selection  == "6": 
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in multivariable derivative mode:\n")
            multivariable_derivative()                
        elif derivative_selection == "b" or derivative_selection == "back":
            menu_back = True         
        elif derivative_selection  == "q": 
            exit() 
        else:
            continue 

def algebra_mode_selection(): 
    
    
    
    menu_back = False

    while menu_back == False:

        algebra_solver_menu()

        algebra_selection = input("Select an option: ")
        algebra_selection  = algebra_selection .lower()
        algebra_selection  = algebra_selection.strip()

        if algebra_selection == "1":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in algebra solver mode:\n")
            algebra_solver_function() 
               
        elif algebra_selection == "2": 
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in factoring mode:\n")
            factor_function()                            
        elif algebra_selection == "3":
            print("\nb - Return to the menu or q - Quit")
            print("\nType your equation in simplifying mode:\n")
            simplify_function()     
        elif algebra_selection == "b" or algebra_selection  == "back":     
            menu_back = True 
        elif algebra_selection == "q": 
            exit()
        else: 
            continue 
def UserGuideMenuSelection(): 
    UserGuideMenuSelectionDisplay()
    

    back = False

    while back == False:        

        UserGuideOptions = input('Choose a user guide/type "o" to view the options: ')
        UserGuideOptions = UserGuideOptions.lower()
        UserGuideOptions = UserGuideOptions.strip()

        if UserGuideOptions == "r" or UserGuideOptions == "real":
            RealNumberInstructionsMenu()
            
            RealNumberInstructionsSelection()
            
        elif UserGuideOptions == "d" or UserGuideOptions == "derivative": 
            UserGuide.DerivativesInstructions()
        
        elif UserGuideOptions == "i" or UserGuideOptions == "integral":
            UserGuide.IntegralInstructions()
            
        elif UserGuideOptions== "s" or UserGuideOptions == "statistics":
            UserGuide.StatisticsInstructions()
            
        elif UserGuideOptions == "a" or UserGuideOptions == "algebra":
            UserGuide.AlgebraInstructions()
        elif UserGuideOptions == "h" or UserGuideOptions  == "how":
            UserGuide.HowtoUseInstructions()
        elif UserGuideOptions   == "o" or UserGuideOptions == "options":    
            UserGuideMenuSelectionDisplay()
        elif UserGuideOptions   == "b" or UserGuideOptions == "back":
            back = True

        elif UserGuideOptions  == "q": 
            exit()   
        else: 
            continue 
def RealNumberInstructionsSelection():

    real_back = False

    while real_back == False:

        realnumberinstructionoptions = input('\nSelect an option/type "o" to view the options: ')
        realnumberinstructionoptions  = realnumberinstructionoptions.lower()
        realnumberinstructionoptions  = realnumberinstructionoptions.strip()

        if realnumberinstructionoptions  == "r" or realnumberinstructionoptions  == "representation": 
            UserGuide.RepresentationInstructions()
        
        elif realnumberinstructionoptions  == "p" or realnumberinstructionoptions  == "power":         
            UserGuide.PowerandLogarithmInstructions()        
        
        elif realnumberinstructionoptions  == "t" or realnumberinstructionoptions  == "trigonometry":                 
            UserGuide.TrigonometryInstructions()

        elif realnumberinstructionoptions  == "a" or realnumberinstructionoptions  == "angular":
            UserGuide.AngularConversionInstructions()

        elif realnumberinstructionoptions  == "h" or realnumberinstructionoptions  == "hyperbolic":                 
            UserGuide.HyperbolicFunctionsInstructions()
      
        elif realnumberinstructionoptions  == "c" or realnumberinstructionoptions  == "constants":                 
            UserGuide.ConstantsInstructions()
            
        elif realnumberinstructionoptions   == "b" or realnumberinstructionoptions  == "back":
            UserGuideMenuSelectionDisplay()
            real_back = True
             
        elif realnumberinstructionoptions   == "o" or realnumberinstructionoptions == "options":    
            RealNumberInstructionsMenu()

        elif realnumberinstructionoptions    == "q":
            exit()    
        else: 
            continue 
def RealModeFunction():
    

    global previous

    run_real_mode = True
    
    while run_real_mode:
        try:
                    
            equation = input()
            equation = equation.lower()
            equation = equation.strip()        

            
            #print(previous)
        
            

            if equation  == "c" or equation =="clear":
                previous = 0
                print(previous)        
            
            elif equation == "b" or equation == "back":
                previous = 0
                run_real_mode = False    
                
            elif equation[0:3] == "ans": 
                
                equation = equation[3:]
                previous = eval(str(previous) + equation)     
                print(previous)        
                
            else:
                previous = eval(equation)
                print(previous)        
            
                    
            
        except: 
            if equation == "q" or equation == "quit":
                run_real_mode = False

                exit()

            else: 
                
            
                continue 
#Simple, power, product, quotient, and chain with x = symbol('x')
def simple_derivative(): 
    
    x = Symbol('x') 
    global previous
    run_simple_mode = True
#    

    while run_simple_mode: 
                        
        equation = input()        
        equation = equation.lower()
        equation = equation.strip()                        

        if equation == "q" or equation == "quit":
            
            

            exit()

        if equation  == "c" or equation =="clear":

            previous = 0
            print(previous)            

        
        elif equation == "b" or equation == "back":
            previous = 0
            run_simple_mode = False                        
        elif equation[0:3] == "ans": 
            
            equation = equation[3:]
            equation = diff(equation)
            previous += equation             
            print(previous)        
            
        else:
            
                previous = diff(equation)
            
                print(previous)        
    
                    
            

#partial and multiplevariable with x, y = symbols('x y ')
def multivariable_derivative(): 
    print("\nType your equation in multivariable mode:\n")
    x, y = symbols('x y')

    global previous
    run_multivariable_mode = True 
    
   
    while run_multivariable_mode:
        equation = input()        
        equation = equation.lower()
        equation = equation.strip()                        

        if equation == "q" or equation == "quit":
                        
            exit()

        if equation  == "c" or equation =="clear":

            previous = 0
            print(previous)            

        
        elif equation == "b" or equation == "back":
            previous = 0
            run_multivariable_mode = False                        
        elif equation[0:3] == "ans": 
            
            equation = equation[3:]
            equation = diff(equation)
            previous += equation             
            print(previous)        
            
        else:
            
                previous = diff(equation)
            
                print(previous)        
        

def integralMethod(equation):
    global previous                 
    x, y = symbols('x y')
    

    opening_paren = equation.find("(")
    closing_paren = equation.rfind(")")
    elements = equation[opening_paren + 1: closing_paren]
    elements = elements.split(",")
    elements = [x.strip() for x in elements]

    integral = elements[0]
    variable = parse_expr(elements[1])

                
    if len(elements) == 2:
    
        resultwithoutlh = integrate(integral, variable)
                    
        return resultwithoutlh 

    elif len(elements) == 4:
        lower = elements[2]
        upper = elements[3]
        resultwlh = integrate(integral, (variable, lower, upper)) 
                                        
        return resultwlh 

def integral_mode(): 
    

    global previous
    run_integral_mode = True 
    count = 0
        
    
    while run_integral_mode:        
        try:

            if count == 0:
                equation = input("integral(")            
                equation = equation.lower()
                equation = equation.strip()
            else: 
                equation = input()            
                equation = equation.lower()
                equation = equation.strip()
            count += 1 
            if equation == "c" or equation == "clear":

                previous = 0            
                print(previous)
            
            elif equation == "b" or equation == "back":
                previous = 0
                run_integral_mode = False

            elif equation[0:3] == "ans":                                                     
                equation = equation[3:]                                
                
                equation = integralMethod(equation)
                previous += equation                 
                print(previous)
                
            else:
                equation = integralMethod(equation)
                previous = equation
                print(previous)        
            
        except: 
            if equation == "q" or equation == "quit":
                run_integral_mode = False

                exit()

            else:                 
            
                continue 

def statisticsFunction(equation):
    print(equation)
            
    opening_paren = equation.find("(")
    closing_paren = equation.rfind(")")
    elements = equation[opening_paren + 1: closing_paren]
    elements = elements.split(",")
    
        
    elements = [int(i) for i in elements]
    
    
    statisticsMethod = equation[:opening_paren]
    
    statisticsMethod  = str(statisticsMethod)
    elements = str(elements)

    result = statisticsMethod + "(" + elements + ")"
    print(result)

    return result 


def statistics_mode(): 
    

    global previous

    run_statistics_mode = True


    while run_statistics_mode:
        try:
        

            equation = input()
            equation = equation.lower()
            equation = equation.strip()        
                
            if equation == "c" or equation =="clear":

                previous = 0
                print(previous)
            
            elif equation == "b" or equation == "back":
                previous = 0
                run_statistics_mode = False        
            elif equation[0:3] == "ans": 
                
                equation = equation[3:]
                equation = statisticsFunction(equation)
                previous = eval(str(previous) + equation)     
                print(previous)
                
            else:
                equation = statisticsFunction(equation)
                previous = eval(equation)
                print(previous)        
        
        except: 
            if equation == "q" or equation == "quit":
                run_statistics_mode = False

                exit()

            else: 
                
            
                continue 


def equationSolver(string_):
    try:
        lhs =  parse_expr(string_.split("=")[0])
        rhs =  parse_expr(string_.split("=")[1])
        solution = solve(lhs-rhs)
        return solution
    except:
        print("Invalid equation.")


def algebra_solver_function(): 

    

    global previous
    run_algebra_solver_function_mode = True 
    
    while run_algebra_solver_function_mode:        
    


        equation = input()
        equation = str(equation) 
        equation = equation.lower()
        equation = equation.strip()        
    

        if equation == "q" or equation == "quit":
            
            exit()

        if equation == "c" or equation == "clear":

            previous = 0
            print(previous)            
        elif equation == "b" or equation == "back":
            previous = 0
            run_algebra_solver_function_mode = False    

        
        elif equation[0:3] == "ans": 
            
            equation = equation[3:]
            previous = list(previous) + equationSolver(equation)
            print(previous)
            
        else:
            previous = equationSolver(equation)
            
            print(previous)        
            
                    

def factor_function():

    
    x = symbols('x')

    global previous

    run_algebra_factor = True


    while run_algebra_factor:
        try:
        

            equation = input()
            equation = equation.lower()
            equation = equation.strip()
            
                
            if equation == "c" or equation == "clear":

                previous = 0
                print(previous)
            elif equation == "b" or equation == "back":
                previous = 0
                run_algebra_factor = False    
            elif equation[0:3] == "ans": 
                
                equation = equation[3:]
                factor(equation)
                previous = eval(str(previous) + equation)     
                print(previous)        
                
            else:
                factor(equation)
                previous = eval(equation)
                print(previous)        
            
                    
        except: 
            if equation == "q" or equation == "quit":
                run_algebra_factor = False

                exit()

            
            else: 
                
            
                continue 
        
def simplify_function():
    
    x = symbols('x')

    global previous

    run_algebra_simplify = True


    while run_algebra_simplify:
        try:
        

            equation = input()
            equation = equation.lower()
            equation = equation.strip()
            
                
            if equation == "c" or equation == "clear":

                previous = 0
                print(previous)
            elif equation == "b" or equation == "back":
                previous = 0
                run_algebra_simplify = False    
            elif equation[0:3] == "ans": 
                
                equation = equation[3:]
                simplify(equation)
                previous = eval(str(previous) + equation)     
                print(previous)        
                
            else:
                simplify(equation)
                previous = eval(equation)
                print(previous)        
            
                    
        except: 
            if equation == "q" or equation == "quit":
                run_algebra_simplify = False

                exit()

            
            else: 
                
            
                continue 

    

mode_selection_function()
