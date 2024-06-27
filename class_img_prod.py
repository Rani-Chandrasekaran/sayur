class ComplexNumber:
   
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def product(self, other):
       
        result =f" {((self.real * other.real)- (self.imag * other.imag))} + {((self.real * other.imag) + (self.imag * other.real))}"
        return result
    
z1 = ComplexNumber(5, 3)  
z2 = ComplexNumber(3, 4)  
result = z1.product(z2)
print(f"product of complexnumber is :{result}i")
