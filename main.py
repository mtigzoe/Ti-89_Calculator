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
    print("1) Simple Rule")
    print("2) Power Rule")
    print("3) Product Rule")
    print("4) Quotient Rule")
    print("5) Chain Rule")
    print("6) Exponential")
    print("7) Partial Rule")
    print("8) Multivariable Rule")
    print("B) Back")
    
def algebra_solver_menu(): 
    print("\nAlgebra Options\n")    

    print("1) Solver")
    print("2) Factor, Expand, Simplify, and Polynomials")    
    print("B) Back")

def UserGuideMenuSelectionDisplay(): 
    print("\nUser Guide Menu\n")
    print("R) Real Number User Guide")
    print("D) Derivative User Guide")
    print("I) Integral User Guide")
    print("S) Statistics User Guide")
    print("A) Algebra User Guide")
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
    
# mode selection function

def mode_selection_function():    


    while True:
        
        mode_menu()

        mode_selection = input("Which calculator mode would you like to use? ")
        mode_selection = mode_selection.lower() 
        mode_selection = mode_selection.strip()

        if mode_selection == "r" or mode_selection == "real":
            calculateRealMode()        
        elif mode_selection == "d" or mode_selection  == "derivative":
            derivative_menu()
            derivative_rules_selection()
            
        elif mode_selection == "i" or mode_selection  == "integral":
            integral_mode()    
        elif mode_selection == "s" or mode_selection  == "statistics":
            statistics_mode()
        elif mode_selection == "a" or mode_selection  == "algebra":
            
            algebra_solver_menu()
            algebra_mode_selection()

        elif mode_selection == "u" or mode_selection  == "user" or mode_selection  == "user guides":
            UserGuideMenuSelection()
        
        else: 
            exit()


#Selection for derivative rules 
def derivative_rules_selection():

    

    
    menu_back = False

    while menu_back == False:
        derivative_menu()

        derivative_selection = input("Select an option: ")
        derivative_selection = derivative_selection.lower() 
        derivative_selection = derivative_selection.strip()
        if derivative_selection == "simple" or derivative_selection  == "1": 
            simple_derivative() 
        elif derivative_selection == "power" or derivative_selection  == "2":
            power_derivative()
        elif derivative_selection == "product" or derivative_selection  == "3": 
            product_derivative()
        elif derivative_selection == "quotient" or derivative_selection  == "4":
            quotient_derivative()
        elif derivative_selection == "chain" or derivative_selection  == "5":
            chain_derivative()
        elif derivative_selection == "exponential" or derivative_selection == "6":
            exponential_derivative()
        elif derivative_selection == "partial" or derivative_selection == "7":
            partial_derivative() 
        elif derivative_selection == "multivariable" or derivative_selection  == "8": 
            multivariable_derivative()                
        elif derivative_selection == "b" or derivative_selection == "back":
            menu_back = True         
        else: 
            exit() 


def algebra_mode_selection(): 
    
    
    
    menu_back = False

    while menu_back == False:

        algebra_solver_menu()

        algebra_selection = input("Select an option: ")
        algebra_selection  = algebra_selection .lower()
        algebra_selection  = algebra_selection.strip()

        if algebra_selection == "1":
            algebra_solver_function() 
               
        elif algebra_selection == "2": 
            simplify_factor()                            
        elif algebra_selection == "b" or algebra_selection  == "back":     
            menu_back = True 
        else: 
            exit()

def UserGuideMenuSelection(): 
    UserGuideMenuSelectionDisplay()
    

    back = False

    while back == False:        

        UserGuideOptions = input("Choose a user guide: ")
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

        elif UserGuideOptions   == "o" or UserGuideOptions == "options":    
            UserGuideMenuSelectionDisplay()
        elif UserGuideOptions   == "b" or UserGuideOptions == "back":
            back = True

        else: 
            exit()   

def RealNumberInstructionsSelection():

    real_back = False

    while real_back == False:

        realnumberinstructionoptions = input("\nSelect an option: ")
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
            real_back = True
             
        elif realnumberinstructionoptions   == "o" or realnumberinstructionoptions == "options":    
            RealNumberInstructionsMenu()

        else:
            exit()    
        print('\nType "o" to view the options.')

# calculator for real numbers

def calculateRealMode():

    global previous

    run_real_mode = True

    print("\nReal Mode\n")


    while run_real_mode:

    
        if previous == 0:
            equation = input("Type your REAL calculation -> ")
            equation = equation.lower()
            equation = equation.strip()  

        else:
            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":
            run_real_mode = False

            exit()

        elif equation  == "c" or equation =="clear":
            previous = 0

        elif equation == "b" or equation == "back":
            previous = 0
            run_real_mode = False

        else:
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
        

def simple_derivative(): 
    print("\nSimple Mode\n")
    x = Symbol('x') 
    global previous
    run_simple_mode = True

    while run_simple_mode:        

        if previous == 0:

            equation = input("Type your SIMPLE expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation  == "q" or equation == "quit":

            exit()            

        elif equation  == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_simple_mode = False            
                            
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
    
   
    while run_power_mode:        

        if previous == 0:

            equation = input("Type your POWER expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation  == "q" or equation == "quit":

            exit()

        elif equation  == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_power_mode = False                            
        
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
    
   
    while run_product_mode:        

        if previous == 0:

            equation = input("Type your PRODUCT expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation  == "b" or equation == "back":

            previous = 0

            run_product_mode = False            

        
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
    
   
    while run_quotient_mode:        

        if previous == 0:

            equation = input("Type your QUOTIENT expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_quotient_mode = False            
        
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
    
   
    while run_chain_mode:        

        if previous == 0:

            equation = input("Type your CHAIN expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_chain_mode = False            

        
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
    
   
    while run_exponential_mode:        

        if previous == 0:

            equation = input("Type your EXPONENTIAL expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_exponential_mode = False            

        
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
    
   
    while run_Partial_mode:        

        if previous == 0:

            equation = input("Type your PARTIAL expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_Partial_mode = False            

        
        else:

            if previous == 0:

                previous = eval(equation)

                previous = previous

            else:

                previous = eval(str(previous) + equation)



def multivariable_derivative(): 
    print("\nMultivariable Mode\n")
    x, y = symbols('x y')

    global previous
    run_multivariable_mode = True 
    
   
    while run_multivariable_mode:        

        if previous == 0:

            equation = input("Type your MULTIVARIABLE expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation =="clear":

            previous = 0            

        elif equation == "b" or equation == "back":

            previous = 0

            run_multivariable_mode = False            

        
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
    
    while run_integral_mode:        

        if previous == 0:

            equation = input("Type your INTEGRAL expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation == "clear":

            previous = 0            
        elif equation == "b" or equation == "back":

            previous = 0
            run_integral_mode = False

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


    while run_statistics_mode:
        
        if previous == 0:

            equation = input("Type your statistics calculation -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()
            
        elif equation == "c" or equation =="clear":

            previous = 0
        elif equation == "b" or equation == "back":

            previous = 0
            run_statistics_mode = False 
            
        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)
    

def equationSolver(string_):
    try:
        lhs =  parse_expr(string_.split("=")[0])
        rhs =  parse_expr(string_.split("=")[1])
        solution = solve(lhs-rhs)
        return solution
    except:
        print("Invalid equation.")


def algebra_solver_function(): 

    print("\n Algebra Solver One Variable\n")

    global previous
    run_algebra_solver_function_mode = True 
    
    while run_algebra_solver_function_mode:        

        if previous == 0:

            equation = input("Type your Solver expression -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()

        elif equation == "c" or equation == "clear":

            previous = 0            
        elif equation == "b" or equation == "back":
            previous = 0 
            run_algebra_solver_function_mode = False 
        elif equation[0:6] == "solve(" or equation[0:7] == "+solve(":
            
            opening_paren = equation.find("(")
            closing_paren = equation.rfind(")")
            elements = equation[opening_paren + 1: closing_paren]
#           elements = elements.split(",")            
            solution = equationSolver(elements)
            
            if previous == 0: 
                previous = solution 

            else:     
                previous += solution
                   
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


    while run_algebra_simplify_factor:
        
        if previous == 0:

            equation = input("Type your Algebra equation -> ")
            equation = equation.lower()
            equation = equation.strip()

        else:

            equation = input(str(previous))
            equation = equation.lower()
            equation = equation.strip()

        if equation == "q" or equation == "quit":

            exit()
            
        elif equation == "c" or equation == "clear":

            previous = 0
        elif equation == "b" or equation == "back":
            previous = 0
            run_algebra_simplify_factor = False       
        else:

            if previous == 0:

                previous = eval(equation)

            else:

                previous = eval(str(previous) + equation)

#mode_menu()

mode_selection_function()

