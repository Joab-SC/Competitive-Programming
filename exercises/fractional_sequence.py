import math
from fractions import Fraction
def main():
    pos = int(input())
    group = int(1 + (-7 + 8*pos)**(1/2)/2)
    print(obtener_resultado(group, pos))
    
def obtener_resultado(group, pos):
    primer_pos = ((group-1)*group/2) +1
    
    num = group + (pos - primer_pos)/group
    entero = int(num)
    fr = Fraction(num-entero)
    return f"{entero} {fr}"
    
    
main()