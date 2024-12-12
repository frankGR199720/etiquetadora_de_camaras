from settings import settings

import os
import time
import fpdf
from datetime import datetime
from tkinter import *
from tkinter import filedialog as FileDialog
import fitz


def ubicacion():
    def test():
        fichero = FileDialog.askdirectory(title="Abrir un fichero")
        
        return fichero
    
    window = Tk()

    fichero=test()
    window.mainloop()

    return fichero

def lectura_de_archivo():
    file = open("scr/val_in.txt", "r")
    val_ini = file.readline()
    val_ini = int(val_ini)
    file.close()
    return val_ini

def convert_pdf_to_png(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".pdf"):
            doc = fitz.open(os.path.join(input_directory, filename))
            
            page = doc.load_page(0)  # Cargar cada página
            zoom_x = 10.0
            zoom_y = 10.0
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix = mat)  # Obtener una imagen de la página
            output = os.path.join(output_directory, filename[:-4] + '.png')
            pix.save(output)#Directorio de entrada y salida



def hoja_pdf(variable_in,direccion):
    etiqueta_in = variable_in+1
    pdf = fpdf.FPDF()
    pdf.add_page()

    pdf.image("Editable ajustado en px SIN MARCAS.png", 0, 0,210,297)
    pdf.set_font("Arial", size=6)
    for i in range(48,196,37):
        variable_in = variable_in+1
        
        pdf.text(x=i,y=35,txt=str(variable_in)) 

    for y in range(51,275 ,16):
        for i in range(30,179,37):     
            variable_in = variable_in+1
            
            pdf.text(x=i,y=y,txt=str(variable_in))
            
    for i in range(67,179,37):
        variable_in = variable_in+1
        
        pdf.text(x=i,y=275,txt=str(variable_in)) 
    
    pdf.output(f"{direccion}/Planilla del {etiqueta_in} al {variable_in}.pdf")

    return variable_in


def lectura_historial():
    file = open("historial.txt")

    os.system("cls")

    print(file.read())
    file.close()

    time.sleep(5)

def escritura_historial(variable_in,variable_fin):
    variable = variable_fin-variable_in
    now = datetime.now()
    file = open("historial.txt", "a")
    file.write(f"\n{now.year}-{now.month}-{now.day}\t\t\t|{variable}\t\t\t|{variable_in}-{variable_fin}")
    file.close()
    print("HISTORIAL ACTUALIZADO")


def actualizar(valor):
    file = open("val_in.txt", "w")
    file.write(str(valor))
    file.close()



if __name__ == "__main__":
    os.system("cls")
    
    while True:
        constante = False
        VALOR_INICIAL = lectura_de_archivo()
    
        os.system("cls")
        letrero= """
 __    __    ______    __           ___       __   __   __   __     .______    __   _______ .__   __. ____    ____  _______ .__   __.  __   _______       ___      
|  |  |  |  /  __  \  |  |         /   \     |  | |  | |  | |  |    |   _  \  |  | |   ____||  \ |  | \   \  /   / |   ____||  \ |  | |  | |       \     /   \     
|  |__|  | |  |  |  | |  |        /  ^  \    |  | |  | |  | |  |    |  |_)  | |  | |  |__   |   \|  |  \   \/   /  |  |__   |   \|  | |  | |  .--.  |   /  ^  \    
|   __   | |  |  |  | |  |       /  /_\  \   |  | |  | |  | |  |    |   _  <  |  | |   __|  |  . `  |   \      /   |   __|  |  . `  | |  | |  |  |  |  /  /_\  \   
|  |  |  | |  `--'  | |  `----. /  _____  \  |__| |__| |__| |__|    |  |_)  | |  | |  |____ |  |\   |    \    /    |  |____ |  |\   | |  | |  '--'  | /  _____  \  
|__|  |__|  \______/  |_______|/__/     \__\ (__) (__) (__) (__)    |______/  |__| |_______||__| \__|     \__/     |_______||__| \__| |__| |_______/ /__/     \__\ 


            MENU DE OPCIONES:
                [1]OPCION 1: Continuar conteo
                [2]OPCION 2: Ver historial
                [3]Salir"""


        print(letrero)

        opcion1 = input("Escribe la opcion deseada: ")

        if opcion1 == '1':
            os.system("cls")
            letrero = """
.___  ___.  _______      _______.     ___          _______   _______    .___________..______           ___      .______        ___             __    ______   
|   \/   | |   ____|    /       |    /   \        |       \ |   ____|   |           ||   _  \         /   \     |   _  \      /   \           |  |  /  __  \  
|  \  /  | |  |__      |   (----`   /  ^  \       |  .--.  ||  |__      `---|  |----`|  |_)  |       /  ^  \    |  |_)  |    /  ^  \          |  | |  |  |  | 
|  |\/|  | |   __|      \   \      /  /_\  \      |  |  |  ||   __|         |  |     |      /       /  /_\  \   |   _  <    /  /_\  \   .--.  |  | |  |  |  | 
|  |  |  | |  |____ .----)   |    /  _____  \     |  '--'  ||  |____        |  |     |  |\  \----. /  _____  \  |  |_)  |  /  _____  \  |  `--'  | |  `--'  | 
|__|  |__| |_______||_______/    /__/     \__\    |_______/ |_______|       |__|     | _| `._____|/__/     \__\ |______/  /__/     \__\  \______/   \______/  
                                                                                                                                                              """
            print(letrero)
            print("donde desea guardar el archivo")
            path = ubicacion()
            
            print(f"En la anterior mesa de trabajo se quedo en el numero: {VALOR_INICIAL}")
            opcion2 = input("desea iniciar la secuencia de trabajo: ")

            if opcion2 == 'si' or opcion2 == 'Si':
                CANTIDAD = input("Cuantas etiquetas deseas: ")
                CANTIDAD = int(CANTIDAD)
                VALOR_FINAL = VALOR_INICIAL + CANTIDAD
                print(f"la mesa de trabajo es:\n \t\t\tVALOR INICIAL = {VALOR_INICIAL+1}\n \t\t\tVALOR FINAL = {VALOR_FINAL}\n \t\t\tCANTIDAD DE ETIQUETAS = {CANTIDAD}")
                cantidad_hoj = CANTIDAD/78
                cantidad_hoj = int(cantidad_hoj)
                print(F"LA CANTIDAD DE HOJAS ES DE: {cantidad_hoj}")
                ar = 1
                
                variable = hoja_pdf(variable_in = VALOR_INICIAL,direccion=path)
                print(f"hoja numero {ar} terminada")
                print(f"numero final de la etiqueta final de la hoja {ar}: {variable}")
                if cantidad_hoj >= 1:
                    cantidad_hoj = cantidad_hoj-1

                
                    for i  in range(cantidad_hoj):
                    
                        variable = hoja_pdf(variable_in= variable,direccion=path)
                
                        print(f"hoja numero {i+2} terminada")
                        print(f"numero final de la etiqueta final de la hoja {i+2}: {variable}")
                
                if CANTIDAD % 78 != 0:
                    variable = hoja_pdf(variable_in = variable,direccion=path)
                    print(f"hoja final terminada")
                    print(f"etiqueta final de la hoja final: {variable}")

                convert_pdf_to_png(input_directory= path , output_directory=path)
                
                escritura_historial(variable_in= VALOR_INICIAL+1, variable_fin= variable)
                actualizar(valor=variable)
                
                time.sleep(5)
        
        if opcion1 == '2':
            
            while True:
                lectura_historial()
                letrero = """   OPCIONES

                        [1]Regresar al menu
                        [2]Salir del programa """

                print(letrero)
                opcion3= int(input("que deseas hacer: "))
                if opcion3 == 1:
                    print( "    Regresando al menu.....")
                    
                    time.sleep(5)
                    break
                    
                elif opcion3 == 2:
                    constante = 1
                    break
                if opcion3 != '1' and opcion3 != '2':
                    print("es una opcion no valida")
                    time.sleep(3)
                    os.system("cls")
                
                    
                

        if constante:
            print("Saliendo")
            time.sleep(3)
            os.system("cls")
            break 

        if opcion1 == '3' :
            print("Saliendo")
            time.sleep(3)
            os.system("cls")
            break

        if opcion1 != '1' and opcion1 != '2' and opcion1 != '3'  :
            print("es una opcion no valida")
            time.sleep(3)
            os.system("cls")