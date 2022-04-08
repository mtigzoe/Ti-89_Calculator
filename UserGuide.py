#User Guide 
#https://docs.python.org/3/library/math.html
#Real number
def RepresentationInstructions(): 

    print("\nRepresentation Functions\n")


    print('{0:10}  {1}'.format("fabs(x)","The absolute value of x."))            

    print('{0:10}  {1}'.format("factorial(x)", "x factorial as an integer."))            

    print('{0:10}  {1}'.format("gcd(*integers)","The greatest common divisor of the specified integer arguments."))                    

    print('{0:10}  {1}'.format("lcm(*integers)","The least common multiple of the specified integer arguments."))                            

    print('{0:10}  {1}'.format("prod(iterable, *, start=1)" , "Calculate the product of all the elements in the input iterable. The default start value for the product is 1."))                            
    
    print('{0:10}  {1}'.format("ulp(x)", "The value of the least significant bit of the float x."))                            
    
    
    
def PowerandLogarithmInstructions():
    print("Power and logarithmic functions")

    print('{0:10}  {1}'.format("exp(x)", "e raised to the power x, where e = 2.718281… is the base of natural logarithms. This is usually more accurate than math.e ** x or pow(math.e, x)."))                            
    
    print('{0:10}  {1}'.format("expm1(x)", "e raised to the power x, minus 1. Here e is the base of natural logarithms."))                            
    
    print('{0:10}  {1}'.format("exp(1e-5) - 1", "1.0000050000069649e-05"))                                        
    
    print('{0:10}  {1}'.format("expm1(1e-5)", "1.0000050000166668e-05"))                                        
    
    print('{0:10}  {1}'.format("log(x[, base])", "With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base)."))                                                        

    print('{0:10}  {1}'.format("log10(x)", "The base-10 logarithm of x. This is usually more accurate than log(x, 10)."))                                        

    print('{0:10}  {1}'.format("pow(x, y)","x raised to the power y."))                                        
        
    
    print('{0:10}  {1}'.format("sqrt(x)", "The square root of x."))                                        
    
def TrigonometryInstructions():
    print("\nTrigonometric functions\n")    
    print("acos(x")
    print("The arc cosine of x, in radians. The result is between 0 and pi.")
    print("math.asin(x)")
    print("The arc sine of x, in radians. The result is between -pi/2 and pi/2.")
    print("atan(x)")
    print("The arc tangent of x, in radians. The result is between -pi/2 and pi/2.")
    print("atan2(y, x)")
    print("atan(y / x), in radians. The result is between -pi and pi.")
    print(".cos(x)")
    print("The cosine of x radians.")
    print("math.sin(x)")
    print("The sine of x radians.")
    print("math.tan(x)")
    print("The tangent of x radians.")

def AngularConversionInstructions(): 
    print("\nAngular Conversion\n")

    print('{0:10}  {1}'.format("degrees(x)", "Convert angle x from radians to degrees."))                            

    
    print('{0:10}  {1}'.format("radians(x)", "Convert angle x from degrees to radians."))


    

def HyperbolicFunctionsInstructions():
    print("\nHyperbolic Functions\n")

    print('{0:10}  {1}'.format("acosh(x)", "The inverse hyperbolic cosine of x."))    

    print('{0:10}  {1}'.format("asinh(x(", "The inverse hyperbolic sine of x."))    

    print('{0:10}  {1}'.format("atanh(x)","The inverse hyperbolic tangent of x."))    
    
    print('{0:10}  {1}'.format("cosh(x)", "The hyperbolic cosine of x."))    

    
    print('{0:10}  {1}'.format("sinh(x)","The hyperbolic sine of x."))    
    
    
    print('{0:10}  {1}'.format("tanh(x)", "The hyperbolic tangent of x."))    
    
    
    
    

def ConstantsInstructions():
    print("\nConstants\n")    

    print('{0:10}  {1}'.format("pi", "The mathematical constant π = 3.141592…, to available precision."))    
    
    

    print('{0:10}  {1}'.format("e", "The mathematical constant e = 2.718281…, to available precision.")) 
    

    print('{0:10}  {1}'.format("tau", "The mathematical constant τ = 6.283185…, to available precision. Tau is a circle constant equal to 2π, the ratio of a circle’s circumference to its radius.")) 
    
    print('{0:10}  {1}'.format("inf", "A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').")) 


    print('{0:10}  {1}'.format("nan", "A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan')."))

    

    

#Complex number 
def ComplexNumberInstructions(): 
    print("\Complex Number Instructions\n")
#Derivatives 
def DerivativesInstructions(): 
    print("\nDerivatives Instructions\n")
    print("It has different eight derivatives rules: Simple, Power, Product, Quotient, Chain, Exponential, Partial and Multivariable.\n") 
    print("For example, you can type 'diff(x**2, x)''.\n")  
    
#integral 
def IntegralInstructions(): 
    print("\nIntegral Instructions\n")    
    print("It has infinite and definite integrals. For example, you can type 'integral(2*x,x)' or 'integral(2*x, x, 1, 2)'")
#Statistics 
def StatisticsInstructions(): 
    print("\nStatistics Instructions\n")

    print("mean([_,_,_])                Arithmetic mean (average) of data.")
    print("fmean([_,_,_])               Fast, floating point arithmetic mean.")
    print("geometric_mean([_,_,_])      Geometric mean of data.")
    print("harmonic_mean([_,_,_])       Harmonic mean of data.")
    print("median([_,_,_])              Median (middle value) of data.")
    print("median_low([_,_,_])          Low median of data.")
    print("median_high([_,_,_])         High median of data.")
    print("median_grouped([_,_,_])      Median, or 50th percentile, of grouped data.")
    print("mode([_,_,_])                Mode (most common value) of data.")
    print("multimode([_,_,_])           List of modes (most common values of data).")
    print("quantiles([_,_,_])           Divide data into intervals with equal probability.")

#Algebra 
def AlgebraInstructions(): 
    print("\nAlgebra Instructions\n")
    print("Usuing simplify(_) - Simplifies the given expression.")
    print("poly(_) - Efficiently transform an expression into a polynomial.")
    print("factor(_) - The factor of given expression.")
    print("Expand(_) - Expands the given expression")
    print("solve(_,_) - Solve for a variable")
    print("solve(_,_,_) - Solve for two variables")
    print("solve(_,_,_) - Solve for three variables")
