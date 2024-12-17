from modes.derivative_mode import DerivMode
from modes.complex_mode import ComplexMode
from modes.real_mode import RealMode
from modes.statistics_mode import StatsMode

#math libraries 
#from math import * 

if __name__ == "__main__":
    expression = ""
    run = True

    MODES = [RealMode(), ComplexMode(), DerivMode(), StatsMode()]
    current_mode_idx = 0

    while run:
    #calculatorBtn = 
        mode_selection = input("Which calculator mode would you like to use? ")
        expression = input("Type your math equation -> ") 
        

        match mode_selection.lower():
            
            
            case "real":
                print("You have selected real mode!")                
                current_mode_idx = 0                    
                RealMode.calculateRealMode(expression)
            case "complex":
                print("You have selected complex mode!")
                current_mode_idx = 1
                ComplexMode.calculateComplex(expression)
            
            case "derivative":
                print("You have selected derivative mode!")
                current_mode_idx = 2
            case "statistics":
                print("You have selected statistics mode!")
                current_mode_idx = 3
                StatsMode.calculateStats(expression)
            case _:
                print("You didn't make a valid selection. Try again!")
                current_mode_idx = 0

        MODES[current_mode_idx].meow()
