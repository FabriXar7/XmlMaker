import os
import imageio
import xml.etree.ElementTree as ET
from moviepy import VideoFileClip


ruta_carpeta = 'C:\\TEMP'


extensiones_multimedia = ['.mp4', '.avi', '.mkv', '.mp3', '.wav', '.flac']


archivos_multimedia = []


for archivo in os.listdir(ruta_carpeta):

    ruta_completa = os.path.join(ruta_carpeta, archivo)
    

    if os.path.isfile(ruta_completa) and any(archivo.lower().endswith(ext) for ext in extensiones_multimedia):
        try:

            if archivo.lower().endswith(('.mp4', '.avi', '.mkv')):
                clip = VideoFileClip(ruta_completa)
            

            duracion = clip.duration
            archivos_multimedia.append((archivo, duracion))
            clip.close()
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")


vMixManager = ET.Element("vMixManager")

events = ET.SubElement(vMixManager, "Events")

event = ET.SubElement(events, "Event", 
                      Title="C   STAGNARI 3", 
                      Type="video", 
                      Start="11/1/2025 10:20:00", 
                      Transition="Cut", 
                      EventDuration="00:00:42.2510000", 
                      InPoint="00:00:00", 
                      MediaDuration="00:00:42.2510000", 
                      KeepDuration="True", 
                      Looping="True", 
                      Path="E:\\comerciales\\2024\\C   STAGNARI 3.mp4")


for nombre, duracion in archivos_multimedia:
    eEvento = ET.SubElement(eEventos,"Event")
    eEvento.text = nombre
    tree = ET.ElementTree(eEventos)

    tree.write("new_data.xml",encoding='utf-8',xml_declaration=True)
    print(f"Archivo: {nombre}, Duración: {duracion:.2f} segundos")
