class ParcialLaboratorio:
    def __init__(self, parcial, laboratorio):
        self.parcial=parcial
        self.laboratorio=laboratorio
    def califi(self):
        return"en el laboratorio tiene {} y en el parcial tiene {}".format(self.parcial,self.laboratorio)
    
calificacion1=ParcialLaboratorio(8,8)
print(calificacion1.califi())
   