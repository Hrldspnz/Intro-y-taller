class Pali(object):
    def __init__(self):
        pass
    
    def palindromo(self,Palabra):
        if isinstance(Palabra,list):
            return self.palindromo_aux(Palabra)
        else:
            return "Error"

    def palindromo_aux(self,palabra):
        if len(palabra)<=1:
            return True
        elif palabra[0]==palabra[-1]:
            return self.palindromo_aux(palabra[1:-1])
        else:
            return False


    def promedio(self,numero,longitud):
        if isinstance(numero,int):
            return self.suma_aux(numero) / longitud
        else:
            return "Error"

    def suma_aux(self,numero):
        if numero==0:
            return 0
        else:
            return (numero%10) + self.suma_aux(numero//10)
