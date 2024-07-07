# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

def convert_to_polar(z):
    modulus_complex = abs(z)
    phase_complex = phase(z)
    return f'{modulus_complex}\n{phase_complex}'
    
z = complex(input())
print(convert_to_polar(z))
