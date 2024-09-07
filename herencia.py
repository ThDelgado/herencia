class A: 
    def __init__(self): 
         print("Pertenezco a la clase A") 
    def metodo_a(self): 
         print("Método heredado de A") 

  

class B: 
    def __init__(self): 
        print("Clase B") 
    def metodo_b(self): 
        print("Método heredado de B") 

  

class C(B, A): 
    def metodo_c(self): 
        print("Metodo de la clase C") 

  
objeto = C() 


print(objeto.metodo_a()) 
print(objeto.metodo_b()) 
print(objeto.metodo_c()) 