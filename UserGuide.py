# User Guide

# Real number
def RepresentationInstructions():

    print("\nRepresentation Functions\n")

    print("{0:10}  {1}".format("fabs(x)", "The absolute value of x."))

    print("{0:10}  {1}".format("factorial(x)", "x factorial as an integer."))

    print(
        "{0:10}  {1}".format(
            "gcd(*integers)",
            "The greatest common divisor of the specified integer arguments.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "lcm(*integers)",
            "The least common multiple of the specified integer arguments.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "prod(iterable, *, start=1)",
            "Calculate the product of all the elements in the input iterable. The default start value for the product is 1.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "ulp(x)", "The value of the least significant bit of the float x."
        )
    )


def PowerandLogarithmInstructions():
    print("Power and logarithmic functions")

    print(
        "{0:10}  {1}".format(
            "exp(x)",
            "e raised to the power x, where e = 2.718281… is the base of natural logarithms. This is usually more accurate than math.e ** x or pow(math.e, x).",
        )
    )

    print(
        "{0:10}  {1}".format(
            "expm1(x)",
            "e raised to the power x, minus 1. Here e is the base of natural logarithms.",
        )
    )

    print("{0:10}  {1}".format("exp(1e-5) - 1", "1.0000050000069649e-05"))

    print("{0:10}  {1}".format("expm1(1e-5)", "1.0000050000166668e-05"))

    print(
        "{0:10}  {1}".format(
            "log(x[, base])",
            "With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).",
        )
    )

    print(
        "{0:10}  {1}".format(
            "log10(x)",
            "The base-10 logarithm of x. This is usually more accurate than log(x, 10).",
        )
    )

    print("{0:10}  {1}".format("pow(x, y)", "x raised to the power y."))

    print("{0:10}  {1}".format("sqrt(x)", "The square root of x."))


def TrigonometryInstructions():
    print("\nTrigonometric functions\n")

    print(
        "{0:10}  {1}".format(
            "acos(x", "The arc cosine of x, in radians. The result is between 0 and pi."
        )
    )

    print(
        "{0:10}  {1}".format(
            "asin(x)",
            "The arc sine of x, in radians. The result is between -pi/2 and pi/2.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "atan(x)",
            "The arc tangent of x, in radians. The result is between -pi/2 and pi/2.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "atan2(y, x)", "atan(y / x), in radians. The result is between -pi and pi."
        )
    )

    print("{0:10}  {1}".format("cos(x)", "The cosine of x radians."))

    print("{0:10}  {1}".format("sin(x)", "The sine of x radians."))

    print("{0:10}  {1}".format("tan(x)", "The tangent of x radians."))


def AngularConversionInstructions():
    print("\nAngular Conversion\n")

    print(
        "{0:10}  {1}".format("degrees(x)", "Convert angle x from radians to degrees.")
    )

    print(
        "{0:10}  {1}".format("radians(x)", "Convert angle x from degrees to radians.")
    )


def HyperbolicFunctionsInstructions():
    print("\nHyperbolic Functions\n")

    print("{0:10}  {1}".format("acosh(x)", "The inverse hyperbolic cosine of x."))

    print("{0:10}  {1}".format("asinh(x(", "The inverse hyperbolic sine of x."))

    print("{0:10}  {1}".format("atanh(x)", "The inverse hyperbolic tangent of x."))

    print("{0:10}  {1}".format("cosh(x)", "The hyperbolic cosine of x."))

    print("{0:10}  {1}".format("sinh(x)", "The hyperbolic sine of x."))

    print("{0:10}  {1}".format("tanh(x)", "The hyperbolic tangent of x."))


def ConstantsInstructions():
    print("\nConstants\n")

    print(
        "{0:10}  {1}".format(
            "pi", "The mathematical constant π = 3.141592…, to available precision."
        )
    )

    print(
        "{0:10}  {1}".format(
            "e", "The mathematical constant e = 2.718281…, to available precision."
        )
    )

    print(
        "{0:10}  {1}".format(
            "tau",
            "The mathematical constant τ = 6.283185…, to available precision. Tau is a circle constant equal to 2π, the ratio of a circle’s circumference to its radius.",
        )
    )

    print(
        "{0:10}  {1}".format(
            "inf",
            "A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').",
        )
    )

    print(
        "{0:10}  {1}".format(
            "nan",
            "A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').",
        )
    )


# Derivatives
def DerivativesInstructions():
    print("\nDerivatives Instructions\n")
    print(
        "It has different eight derivatives rules: Simple, Power, Product, Quotient, Chain, Exponential, Partial and Multivariable.\n"
    )
    print("For example, you can type 'diff(x**2, x)''.\n")


# integral
def IntegralInstructions():
    print("\nIntegral Instructions\n")
    print("It has infinite and definite integrals.\n")
    print("For example, you can type 'integral(2*x,x)' or 'integral(2*x, x, 1, 2)'\n")


# Statistics
def StatisticsInstructions():
    print("\nStatistics Instructions\n")

    print("{0:10}  {1}".format("mean([_,_,_])", "Arithmetic mean (average) of data."))
    print(
        "{0:10}  {1}".format("fmean([_,_,_])", "Fast, floating point arithmetic mean.")
    )
    print("{0:10}  {1}".format("geometric_mean([_,_,_])", "Geometric mean of data."))
    print("{0:10}  {1}".format("harmonic_mean([_,_,_])", "Harmonic mean of data."))
    print("{0:10}  {1}".format("median([_,_,_])", "Median (middle value) of data."))
    print("{0:10}  {1}".format("median_low([_,_,_])", "Low median of data."))
    print("{0:10}  {1}".format("median_high([_,_,_])", "High median of data."))
    print(
        "{0:10}  {1}".format(
            "median_grouped([_,_,_])", "Median, or 50th percentile, of grouped data."
        )
    )
    print("{0:10}  {1}".format("mode([_,_,_])", "Mode (most common value) of data."))
    print(
        "{0:10}  {1}".format(
            "multimode([_,_,_])", "List of modes (most common values of data)."
        )
    )
    print(
        "{0:10}  {1}".format(
            "quantiles([_,_,_])", "Divide data into intervals with equal probability."
        )
    )
    print(
        "{0:10}  {1}".format("pstdev(_,_,_)", "Population standard deviation of data.")
    )
    print("{0:10}  {1}".format("pvariance([_,_,_])", "Population variance of data."))


print("{0:10}  {1}".format("stdev([_,_,_])", "Sample standard deviation of data."))
print("{0:10}  {1}".format("pvariance([_,_,_])", "Sample variance of data."))

# Algebra
def AlgebraInstructions():
    print("\nAlgebra Instructions\n")
    print(
        "{0:10}  {1}".format("Usuing simplify(_)", "Simplifies the given expression.")
    )
    print(
        "{0:10}  {1}".format(
            "poly(_)", "Efficiently transform an expression into a polynomial."
        )
    )
    print("{0:10}  {1}".format("factor(_)", "The factor of given expression."))
    print("{0:10}  {1}".format("Expand(_)", "Expands the given expression"))
    print("{0:10}  {1}".format("solve(_ = _)", "Solve for a variable"))

def HowtoUseInstructions():
    print("\nHow to Use Instructions\n")
    print(
        "{0:10}  {1}".format("c or clear", "Clear the calculator.")
    )
    print(
        "{0:10}  {1}".format(
            "b or back", "Return to a menu."
        )
    )
    
