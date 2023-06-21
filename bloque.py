class Bloque:
    def __init__(self, tiene_bomba):
        self.tiene_bomba = tiene_bomba
        self.fue_clickeado = False
        self.tiene_bandera = False
    
    def get_tiene_bomba(self):
        return self.tiene_bomba
    
    def get_fue_clickeado(self):
        return self.fue_clickeado
    
    def get_tiene_bandera(self):
        return self.tiene_bandera
    
    def crear_vecinos(self, vecinos):
        self.vecinos = vecinos
        self.crear_numero_cerca()

    def crear_numero_cerca(self):
        self.numero_cerca = 0
        for bloque in self.vecinos:
            if bloque.get_tiene_bomba():
                self.numero_cerca += 1
    
    def get_numero_cerca(self):
        return self.numero_cerca
    
    def alternar_bandera(self):
        self.tiene_bandera = not self.tiene_bandera

    def click(self):
        self.fue_clickeado = True

    def get_vecinos(self):
        return self.vecinos