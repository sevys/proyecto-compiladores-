class Pila():

    #iniciamos la pila
    def __init__(self):
        self.items=[]


    #agregamos un dato en la pila
    def apilar(self, dato):
        self.items.append(dato)


    #eliminamos un dato de la pila
    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()


    #verificamos si la pila esta vacia
    def esta_vacia(self):
        if len(self.items) == 0:
            return True
        else:
            return False


    #mostramos todos los elementos de la pila
    def ver_pila(self):
        print(self.items)