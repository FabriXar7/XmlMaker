import os

import imageio
import xml.etree.ElementTree as ET
from moviepy import VideoFileClip


ruta_programas = 'O:\\Fabrix\\LMix\\PROGRAMAS\\'
ruta_publicidad = 'O:\\Fabrix\\LMix\\PUBLICIDAD\\'
dia_segundos = 86400

extensiones_multimedia = ['.mp4', '.avi', '.mkv', '.mp3', '.wav', '.flac']


archivos_programas = []
archivos_publicidad = []

def segundosA(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

for archivo in os.listdir(ruta_programas):

    ruta_completa = os.path.join(ruta_programas, archivo)
    

    if os.path.isfile(ruta_completa) and any(archivo.lower().endswith(ext) for ext in extensiones_multimedia):
        try:

            if archivo.lower().endswith(('.mp4', '.avi', '.mkv')):
                clip = VideoFileClip(ruta_completa)
            

            duracion = segundosA(int(clip.duration))
            archivos_programas.append((archivo, duracion))
            clip.close()
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")


for archivo in os.listdir(ruta_publicidad):

    ruta_completa = os.path.join(ruta_publicidad, archivo)
    

    if os.path.isfile(ruta_completa) and any(archivo.lower().endswith(ext) for ext in extensiones_multimedia):
        try:

            if archivo.lower().endswith(('.mp4', '.avi', '.mkv')):
                clip = VideoFileClip(ruta_completa)
            

            duracion = segundosA(int(clip.duration))
            archivos_publicidad.append((archivo, duracion))
            clip.close()
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")



vMixManager = ET.Element("vMixManager")

events = ET.SubElement(vMixManager, "Events")


for nombre, duracion in archivos_programas:
    #duracion: {f"(duracion)"}
    #print(segundosA(int(duracion)) + " Segundos")
    event = ET.SubElement(events, "Event", 
                      Title=nombre, 
                      Type="video", 
                      Start="1/1/2025 00:00:00", 
                      Transition="Cut", 
                      EventDuration=str(duracion), 
                      InPoint="00:00:00", 
                      MediaDuration=str(duracion), 
                      KeepDuration="True", 
                      Looping="True", 
                      Path=ruta_programas+nombre)
    event.text = f"{ruta_programas}\\{nombre}\nVideo: AVC\nAudio: AAC\nDuration: {duracion}"
    for nombre, duracion in archivos_publicidad:
        #duracion: {f"(duracion:.2f)"}
        event = ET.SubElement(events, "Event", 
                          Title=nombre, 
                          Type="video", 
                          Start="1/1/2025 00:00:00", 
                          Transition="Cut", 
                          EventDuration=str(duracion), 
                          InPoint="00:00:00", 
                          MediaDuration=str(duracion), 
                          KeepDuration="True", 
                          Looping="True", 
                          Path=ruta_publicidad+nombre)
        event.text = f"{ruta_publicidad}\\{nombre}\nVideo: AVC\nAudio: AAC\nDuration: {duracion}"

    
tree = ET.ElementTree(vMixManager)
tree.write("PlayList.xml",encoding='utf-8',xml_declaration=True)
print("XML creado correctamente.")

