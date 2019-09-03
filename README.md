# Complex Calculator
This is a complex number calculator, which allows you to calculate the addition, subtraction, multiplication, division, conjugate, module, phase, conversion from polar to cartesian and from cartesian to polar, scalar multiplication by vector, transposed matrix, conjugate matrix, attached matrix, matrix norm, check if it is unitary, if it is Hermitian and tensor product. And some of these are already for matrix.
# How does it work?
First, you must download the .py file whose name is 'NumerosComplejos.py'. It's a library implemented in Python, which works based on functions, each of these receives the necessary parameters to execute the desired operation and return the result of each operation, keep in mind that every time the function returns a tuple is the same as an imaginary number, the first position being the whole part and the second position the imaginary part. 
Below are examples of how it should be used:

```python
    def suma(a,b): #'a' and 'b' are complex numbers in tuples
        ent = a[0] + b[0] # 'ent' add the whole parts
        imag = a[1] + b[1] # 'imag' add the imaginary parts
        return ent,imag # returns a tuple with the whole and imaginary part
        
        
    def suma_matrices(m1,m2):
    matriz = [[0]*(len(m1[0])) for i in range(len(m1))]
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for a in range(len(m1)):
            for b in range(len(m1[0])):
                matriz[a][b] = suma(m1[a][b],m2[a][b])
        return matriz
    else:
        return False
```
In this case, the sum of matrices is being implemented, the code verifies if the operations can be done.
# Test
If you need to test your results, you must download the .py file called 'Test.py'. The files 'NumerosComplejos.py' and 'Test.py' must be in the same folder so that it can be executed correctly. Example of how it should be done:
```python
    import unittest
    import NumerosComplejos
    class TestmyFunctions(unittest.TestCase):
          def testadd(self):
              a = (1,2) # the first tuple you want to operate
              b = (1,3) # the second tuple you want to operate
              esperado = (2,5) # the result you expect to get
              res = NumerosComplejos.suma(a,b) # the result that the function gives
              self.assertEqual(esperado,res)
    if __name__ == '__main__':
          unittest.main() 
    #############################
    In the Python console you should see:
    ..............................
    Ran 1 tests in (your time)s

    OK
    ..............................
    else, should correct the error
    
```
# Made by:
Julián Quintero
Systems Engineer
Escuela Colombiana de Ingeniería Julio Garavito
