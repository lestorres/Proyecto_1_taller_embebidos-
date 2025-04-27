#import os
# Comando del pipeline GStreamer
#comando = (
#    "gst-launch-1.0 "
#    "filesrc location=/usr/bin/myapp/inputs/conduccion_2.mp4 "
#    "! decodebin "
#    "! videoconvert "
#    "! ximagesink"
#)
# Ejecutar el comando
#os.system(comando)

from utils.gst_utils import gst_launch

# Ruta al archivo de entrada
INPUT_PATH = "/usr/bin/myapp/inputs/conduccion_1.mp4"
INPUT_URI = f"file://{INPUT_PATH}"

# Pipeline solo para reproducir video usando appsink
pipeline_str = (
    f'filesrc location={INPUT_PATH} ! '
    f'decodebin ! '
    f'videoconvert ! '
    f'videoscale ! '
    f'video/x-raw,width=320,height=180 ! '
    f'appsink sync=true'
)

# Ejecutar pipeline
gst_launch(pipeline_str)