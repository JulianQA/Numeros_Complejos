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
        
        
    def suma_matrices(m1,m2): # m1 and m2 are matrices
        matriz = [[0]*(len(m1[0])) for i in range(len(m1))] # create a matrix with the dimensions of m1 and m2
        if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): # check if the dimensions of the matrices are equal
            for a in range(len(m1)):
                for b in range(len(m1[0])):
                    matriz[a][b] = suma(m1[a][b],m2[a][b]) #if they are, add position to position
            return matriz # return a matrix added
        else:
            return False # if they aren't, return False
            
            
    def unit(m1): # m1 is a matrix
        res = multiplicacion_matrices(m1,mat_adjunta(m1)) # 'res' is assigned matrix multiplication
        identidad = [[(0,0)]*len(m1) for i in range(len(m1))] # create a matrix with the dimension of m1
        for i in range(len(identidad)):
                identidad[i][i] = (1,0) # create a identity matrix
        if res == identidad: # check if the multiplication is equal to identity matrix 
            return True # and returns True if it's unitary
        else:
            return False # if they aren't, return False
```

+ if you need to try any function, before using the library unittest, you must do the following:
```python
     print(function_name_of_test(the_parameters_that_the_function receives))
```
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
           def testsumamatriz(self):
              a = [[(1,2)],[(2,1)]] # the first matrix you want to operate
              b = [[(3,1)],[(1,3)]] # the second matriz you want to operate
              esperado = [[(4,3)], [(3,4)]] # the result you expect to get
              res = NumerosComplejos.suma_matrices(a,b) # the result that the functions gives
              self.assertEqual(esperado,res)
           def testunitaria(self):
              a = [[(1,0),(0,0)],[(0,0),(1,0)]] # the first matrix you want to operate
              esperado = True # the result you expect to get
              res = NumerosComplejos.unit(a) # the result that the functions gives
              self.assertEqual(esperado,res)
        
    
    if __name__ == '__main__':
          unittest.main() 
               
    #############################
    
    In the Python console you should see:
    ..............................
    Ran 3 tests in (your time)s

    OK
    ..............................
```
    else, should correct the error
    
# Made by:
 + Julián Quintero
 + Systems Engineer
 + Escuela Colombiana de Ingeniería Julio Garavito
