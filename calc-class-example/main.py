from modes.base_mode import BaseMode

#from modes.derivative_mode import DerivMode
#from modes.complex_mode import ComplexMode
#from modes.real_mode import RealMode
#from modes.statistics_mode import StatsMode

#import m 

if __name__ == "__main__":
    run = True
    previous = 0
    def runmain():
        global run
        global previous
        
        MODES = BaseMode() 
    
         
        
        
        
        expression = ""
        print(MODES.calculateRealMode(m.sqrt(4)))
        if previous == 0:
            expression = input("Type your math equation -> ")
        else:
            expression = input(str(previous))
            

        if expression == "quit":
            print("Come back whenever you feel you are stuck!")
            run = False
        elif expression =="clear":
            previous = 0    
            run = True 
        else:
    #equation = re.sub('[A-Za-z:;.?,()" "]', '', equation)
          if previous == 0:
              previous = eval(expression)
          else:
              previous = eval(str(previous) + expression)



        
    while run:
       runmain()

