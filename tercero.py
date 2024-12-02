import os

from primero import Paciente
from segundo import Coleccion
from primero import PacienteAmbulatorio
from primero import PacienteHospitalizado
import csv
def GenerarColeccion():
    coleccion=Coleccion()
    with open("C:/Users/Usuario/Desktop/final POO 12-08-2024/pacientes1.csv",mode='r') as archivo:
        lector=csv.reader(archivo) 
        for fila in lector:
            tipo=fila[0]
            if tipo=="P":
                coleccion.insertar(
                    PacienteAmbulatorio(
                        nombre=fila[1],
                        apellido=fila[2],
                        email=fila[3],
                        n_tel=fila[4],
                        historial=fila[5],
                        alergias=fila[6].split(';'),
                        o_social=fila[7],
                    )
                )   
            elif tipo=="H":
                coleccion.insertar(
                    PacienteHospitalizado(
                        nombre=fila[1],
                        apellido=fila[2],
                        email=fila[3],
                        n_tel=fila[4],
                        n_hab=fila[5],
                        fecha_i=fila[6],
                        diagnostico=fila[7],
                        cant_dias=int(fila[8]),
                        importe_d=float(fila[9]),
                        )
                )
            else:
                print(f"Tipo desconocido:{tipo}")  
    return coleccion


if __name__=="__main__":

    coleccion=GenerarColeccion()
    n=input("Que desea hacer?\nIngrese 1 para mostrar cantidad de pacientes hospitalizados con neumonia.\nIngrese 2 para mostrar la cantidad de pacientes ambulatorios.\nIngrese 3 para mostrar el importe de todos los pacientes\nIngrese 4 para mostrar el tipo de paciente segun posicion\nIngrese 5 para cambiar el valor de consulta")
    if n=="1":
        coleccion.CantPHN()
    elif n=="2":
        coleccion.CantPA()
    elif n=="3":
        coleccion.MostrarImporte()
    elif n=="4":
        i=int(input("Ingrese posicion"))
        try:
            coleccion.TipoPaciente(i)
        except:
            print("Indice fuera de rango.")
    elif n=="5":
        v=input("Ingrese nuevo valor de consulta.")
    
        print(f"Valor actual de consulta: {Paciente.get_valor_consulta()}")

        Paciente.set_valor_consulta(v)

        print(f"Nuevo valor de consulta: {Paciente.get_valor_consulta()}")