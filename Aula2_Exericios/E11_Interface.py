from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Documento(Imprimivel):
    def imprimir(self):
        print("Imprimindo documento...")

class Foto(Imprimivel):
    def imprimir(self):
        print("Imprimindo foto...")

doc = Documento()
foto = Foto()

doc.imprimir() 
foto.imprimir() 
