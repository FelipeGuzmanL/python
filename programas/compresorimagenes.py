from PIL import Image
import os
import keyboard
from tqdm import tqdm

username = os.environ["USERNAME"]

downloadsFolder = f"C:/Users/{username}/Downloads/"
outputFolder = f"C:/Users/{username}/Downloads/Imagenes/Imagenes Comprimidas/"
musicFolder = f"C:/Users/{username}/Downloads/Sonidos y Musica/"
exceldocuments = f"C:/Users/{username}/Downloads/Documentos Excel y CSV/"
pdfdocuments = f"C:/Users/{username}/Downloads/Documentos PDF/"
WinrarDocuments = f"C:/Users/{username}/Downloads/Documentos Winrar/"
imagenes = f"C:/Users/{username}/Downloads/Imagenes/"

scripts = f"C:/Users/{username}/Downloads/Scripts/"
scriptspython = f"C:/Users/{username}/Downloads/Scripts/Python/"
scriptsphp = f"C:/Users/{username}/Downloads/Scripts/PHP/"
basededatos = f"C:/Users/{username}/Downloads/Scripts/SQL/"


print("Ordenando archivos de descarga...")
# Crear la carpeta de salida si no existe
folders_to_create = [
    outputFolder,
    musicFolder,
    exceldocuments,
    pdfdocuments,
    WinrarDocuments,
    imagenes,
    scripts,
    scriptspython,
    scriptsphp,
    basededatos
]

# Crear las carpetas si no existen
for folder in tqdm(folders_to_create, desc="Creando carpetas"):
    folder_path = os.path.join(downloadsFolder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
if __name__ == "__main__":
    for filename in tqdm(os.listdir(imagenes), desc="Ordenando archivos"):
        name, extension = os.path.splitext(filename)
    
        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            picture_path = os.path.join(imagenes, filename)
            
            try:
                picture = Image.open(picture_path)
                
                # Verificar el tamaño de la imagen
                max_image_size = 178956970  # Tamaño máximo permitido
                if picture.size[0] * picture.size[1] <= max_image_size:
                    output_path = os.path.join(outputFolder, "compressed_" + filename)
                    picture.save(output_path, optimize=True, quality=60)
                    #print(f"Imagen comprimida guardada en {output_path}")
                else:
                    print(f"Imagen {filename} demasiado grande, no se procesará.")
                
            except Image.DecompressionBombError:
                print(f"Error de bomba de descompresión en la imagen {filename}.")
            except Exception as e:
                print(f"Error al procesar la imagen {filename}: {e}")
        
        
            
print("Archivos ordenados correctamente...")

print("Presiona Escape (ESC) para finalizar")

keyboard.wait("esc")