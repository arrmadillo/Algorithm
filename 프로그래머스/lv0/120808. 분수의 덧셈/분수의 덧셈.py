import fractions
def solution(denum1, num1, denum2, num2):
    a = fractions.Fraction(denum1, num1)
    b = fractions.Fraction(denum2, num2)
    c = a + b
    
    return [c.numerator, c.denominator]