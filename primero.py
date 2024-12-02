class Paciente():
    v_consulta=15000
    def __init__(self,nombre,apellido,email,n_tel):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.n_tel=n_tel
    def getnombre(self):
        return self.nombre
    def getapellido(self):
        return self.apellido
    def Importe(cls):
        return cls.v_consulta+cls.CalculoImporte()
    def CalculoImporte(cls):
        pass
    @classmethod
    def get_valor_consulta(cls):
        return cls.v_consulta
    @classmethod
    def set_valor_consulta(cls, nuevo_valor):
        cls.v_consulta = nuevo_valor
        
class PacienteAmbulatorio(Paciente):
    def __init__(self,nombre,apellido,email,n_tel,historial,alergias,o_social):
        super().__init__(nombre,apellido,email,n_tel)
        self.__historial=historial
        self.__alergias=alergias
        self.__o_social=o_social
    def CalculoImporte(self):
        plus=0
        if self.__o_social=="Provincia":
            plus=5000
        elif self.__o_social=="OSDE":
            plus=2000
        else: plus=10000
        c=plus-self.v_consulta
       
        return c
class PacienteHospitalizado(Paciente):
    def __init__(self,nombre,apellido,email,n_tel,n_hab,fecha_i,diagnostico,cant_dias,importe_d):
        super().__init__(nombre,apellido,email,n_tel)
        self.__n_hab=n_hab
        self.__fecha_i=fecha_i
        self.__diagnostico=diagnostico
        self.__cant_dias=cant_dias
        self.__importe_d=importe_d
    def CalculoImporte(self):
        c=self.__cant_dias*self.v_consulta+self.__importe_d
       
        return c
    def getdiagnostico(self):
        return self.__diagnostico
if __name__=='__main__':
    paciente=PacienteAmbulatorio('Rocio','Palma',2644804578,'rocioandreapalma1234@gmail.com','no historial','no','Provincia')
    print(paciente.Importe())
