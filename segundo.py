
from primero import PacienteAmbulatorio
from primero import PacienteHospitalizado


class Nodo:
    paciente = None
    sig = None

    def __init__(self, paciente):
        self.paciente = paciente
        self.sig = None

    def setsig(self, sig):
        self.sig = sig

    def getsig(self):
        return self.sig

    def getpaciente(self):
        return self.paciente


class Coleccion:
    cabeza = None
    #ultimo = None

    def __init__(self):
        self.cabeza = None

    def insertar(self, paciente):
        nodo = Nodo(paciente)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            aux = self.cabeza
            while aux.getsig():
                aux = aux.getsig()
            aux.setsig(nodo)
    def CantPHN(self):
        print("aaaaaa")
        phn = 0
        aux = self.cabeza
        
        while aux:
            paciente=aux.getpaciente()
            if isinstance(paciente, PacienteHospitalizado):
                if paciente.getdiagnostico() == "Neumonia":
                    phn += 1
            aux = aux.getsig()
        print(f"Pacientes con neumonia:{phn}")


    def CantPA(self):
        print("oooooo")
        pa = 0
        aux = self.cabeza
        while aux:
            paciente=aux.getpaciente()
            if isinstance(paciente, PacienteAmbulatorio):
                pa += 1
            aux = aux.getsig()
        print(f"Pacientes ambulatorios:{pa}")

    def MostrarImporte(self):
        aux=self.cabeza
        while aux:
            paciente=aux.getpaciente()
            print(f"Importe de {paciente.getnombre()} {paciente.getapellido()}: {paciente.Importe()}")
            aux=aux.getsig()
    
    def TipoPaciente(self,i):
        j=0
        aux=self.cabeza
        while j!=i:
            aux=aux.getsig()
            j+=1
        paciente=aux.getpaciente()
        if isinstance(paciente,PacienteAmbulatorio):
            print(f"Tipo de paciente: Ambulatorio")
        elif isinstance(paciente,PacienteHospitalizado):
            print(f"Tipo de paciente: Hospitalizado")

if __name__=='__main__':
    paciente=PacienteAmbulatorio('Rocio','Palma',2644804578,'rocioandreapalma1234@gmail.com','no historial','no','Provincia')
    coleccion=Coleccion()
    coleccion.insertar(paciente)
    coleccion.MostrarImporte()
