#!/usr/bin/env python3
import os

# Comando del pipeline GStreamer
comando = (
    "gst-launch-1.0 "
    "filesrc location=/usr/bin/myapp/inputs/conduccion_2.mp4 "
    "! decodebin "
    "! videoconvert "
    "! ximagesink"
)

# Ejecutar el comando
os.system(comando)
