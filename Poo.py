"""
>>> VC = ValidacionCaracter('A')
>>> VC.getTipoCaracter()
'Letra mayúscula'
"""
class ValidacionCaracter: #clase
    __caracter = ''
    __tipo_caracter = '' #atributos

    def __init__(self, caracter):
        self.__caracter = caracter
        self.identificarCaracter()

    def identificarCaracter(self):
        tipo = ord(self.__caracter)
        if(tipo >= 65 and tipo <=90):
            self.__tipo_caracter = "Letra mayúscula"
        elif(tipo >= 97 and tipo <=122 ):
            self.__tipo_caracter = "Letra minúscula"
        elif(tipo >=48 and tipo <=57):
            self.__tipo_caracter = "Número"
        else:
            self.__tipo_caracter = "Invalido"

    def getTipoCaracter(self):
        return self.__tipo_caracter


if __name__ == '__main__':
    import doctest
    doctest.testmod()