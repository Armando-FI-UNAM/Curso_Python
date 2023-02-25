# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:48:00 2023

@author: arman
"""

##clase de coche

class Coches():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def estado(self):
        if(self.enmarcha):
            return "El cohce esta en marcha"
        else:
            return "El coche sigue detenido"
        
    def detener(self):
        self.enmarcha=False
    
miCoche=Coches()##instanciar una clase


print("El largo del coche es:",miCoche.largoChasis)##acceder a la propiedad
print("El coche tiene:",miCoche.ruedas,"ruedas")
miCoche.arrancar()
print(miCoche.estado())
miCoche.detener()
print(miCoche.estado())