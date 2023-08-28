from PIL import Image
import os
import keyboard
from tqdm import tqdm

username = os.environ["USERNAME"]

respaldoFolder = f"C:/Users/{username}/Desktop/Respaldo/"

downloadsFolder = f"C:/Users/{username}/Downloads/"
userFolder = f"C:/Users/{username}/"
desktopFolder = f"C:/Users/{username}/Desktop/"
picturesFolder = f"C:/Users/{username}/Pictures/"
documentsFolder = f"C:/Users/{username}/Documents/"

musicFolder = f"C:/Users/{username}/Desktop/Respaldo/Sonidos y Musica/"
documentos = f"C:/Users/{username}/Desktop/Respaldo/Documentos/" 
exceldocuments = f"C:/Users/{username}/Desktop/Respaldo/Documentos/Documentos Excel y CSV/"
worddocuments = f"C:/Users/{username}/Desktop/Respaldo/Documentos/Documentos Word/"
pptdocuments = f"C:/Users/{username}/Desktop/Respaldo/Documentos/Documentos Power Point/"
pdfdocuments = f"C:/Users/{username}/Desktop/Respaldo/Documentos PDF/"
WinrarDocuments = f"C:/Users/{username}/Desktop/Respaldo/Documentos Winrar/"
imagenes = f"C:/Users/{username}/Desktop/Respaldo/Imagenes/"

scripts = f"C:/Users/{username}/Desktop/Respaldo/Scripts/"
scriptspython = f"C:/Users/{username}/Desktop/Respaldo/Scripts/Python/"
scriptsphp = f"C:/Users/{username}/Desktop/Respaldo/Scripts/PHP/"
basededatos = f"C:/Users/{username}/Desktop/Respaldo/Scripts/SQL/"


print("Respaldando archivos...")
# Crear la carpeta de salida si no existe
folders_to_create = [
    musicFolder,
    documentos,
    exceldocuments,
    worddocuments,
    pptdocuments,
    pdfdocuments,
    WinrarDocuments,
    imagenes,
    scripts,
    scriptspython,
    scriptsphp,
    basededatos
]

folders_to_scan = [
    downloadsFolder,
    userFolder,
    desktopFolder,
    picturesFolder,
    documentsFolder,
]
if not os.path.exists(respaldoFolder):
    os.makedirs(respaldoFolder)

# Crear las carpetas si no existen
for folder in tqdm(folders_to_create, desc="Creando carpetas"):
    folder_path = os.path.join(respaldoFolder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
if __name__ == "__main__":
    for folder in folders_to_scan:
        for filename in tqdm(os.listdir(folder), desc="Ordenando archivos"):
            name, extension = os.path.splitext(filename)       
            
            if extension in [".mp3"]:
                os.rename(folder + filename, musicFolder + filename)
                
            if extension in [".xlsx",".xlsm",".xltx",".xltm",".xlsb","xlam",".csv",
                            ".doc",".docx",".docm",".dotx",".dotm",
                            ".pptx",".pptm",".potx",".potm",".ppam",".ppsx",".sldx",".sldm",".thmx"]:
                if extension.lower() in [".xlsx",".xlsm",".xltx",".xltm",".xlsb","xlam",".csv"]:
                    os.rename(folder + filename, exceldocuments + filename)
                elif extension.lower() in [".doc",".docx",".docm",".dotx",".dotm"]:
                    os.rename(folder + filename, worddocuments + filename)
                elif extension.lower() in [".pptx",".pptm",".potx",".potm",".ppam",".ppsx",".sldx",".sldm",".thmx"]:
                    os.rename(folder + filename, pptdocuments + filename)
            
            if extension in [".pdf"]:
                os.rename(folder + filename, pdfdocuments + filename)
            
            if extension in [".rar", ".zip", ".7z"]:
                documento = os.path.join(WinrarDocuments + filename)
                if not os.path.exists(documento):
                    os.rename(folder + filename, WinrarDocuments + filename)
                
            if extension.lower() in [".jpg", ".jpeg", ".png",".gif"]:
                os.rename(folder + filename, imagenes + filename)

            if extension.lower() in [".py",".php",".js"]:
                if extension.lower() in [".py"]:
                    os.rename(folder + filename, scriptspython + filename)
                elif extension.lower() in [".php"]:
                    os.rename(folder + filename, scriptsphp + filename)
                    
            if extension.lower() in [".sql"]:
                os.rename(folder + filename, basededatos + filename)
            
print("Archivos ordenados y respaldados correctamente...")

print("Presiona Escape (ESC) para finalizar")

keyboard.wait("esc")