from modes.base_mode import BaseMode
import statistics 
from statistics import *

class StatsMode(BaseMode):
    def calculateStats(expression):
        #return print("%s" % "statistics."+expression)
        result = str("statistics."+expression)
        #return print(f"statistics.{expression}")
        return print(eval(result ))


    
        
         
