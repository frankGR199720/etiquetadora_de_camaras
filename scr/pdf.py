import os
import fitz

def convert_pdf_to_png(pdf_directory, output_directory):
    
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            doc = fitz.open(os.path.join(pdf_directory, filename))
            for i in range(len(doc)):
                page = doc.load_page(i)  # Cargar cada página
                zoom_x = 10.0
                zoom_y = 10.0
                mat = fitz.Matrix(zoom_x, zoom_y)
                pix = page.get_pixmap(matrix = mat)  # Obtener una imagen de la página
                output = os.path.join(output_directory, filename[:-4] + '_page_' + str(i) + '.png')
                pix.save(output)#Directorio de entrada y salida
input_directory = 'C:/Users/ATM-DESING4/Documents/muestreo/'
output_directory = 'C:/Users/ATM-DESING4/Documents/muestreo'


convert_pdf_to_png(input_directory, output_directory)