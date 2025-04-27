import cv2
import numpy as np
from openvino.runtime import Core
from utils.gst_utils import gst_launch  
import os

# Configuración
BASE_PATH = "/usr/bin/myapp"
MODELS_PATH = os.path.join(BASE_PATH, "models")
MODEL_1 = "person-vehicle-bike-detection-2004"  # Modelo de detección de vehículos
HPE_MODEL = f"{MODELS_PATH}/intel/{MODEL_1}/FP32/{MODEL_1}.xml"
BIN_FILE = HPE_MODEL.replace(".xml", ".bin")  # El archivo .bin correspondiente

# Verificar que los archivos existen
if not os.path.exists(HPE_MODEL):
    print(f"Error: El archivo {HPE_MODEL} no existe.")
    exit()

if not os.path.exists(BIN_FILE):
    print(f"Error: El archivo {BIN_FILE} no existe.")
    exit()

print(f"Archivos encontrados correctamente: {HPE_MODEL} y {BIN_FILE}")

# Cargar el modelo con OpenVINO Runtime
ie = Core()

# Cargar el modelo (el XML y el BIN deberían ser cargados automáticamente por OpenVINO)
try:
    model = ie.read_model(model=HPE_MODEL)
    compiled_model = ie.compile_model(model=model, device_name="CPU")
    print("Modelo cargado y compilado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Obtener las capas de entrada y salida del modelo
input_layer = compiled_model.input(0)
output_layer = compiled_model.output(0)

# Ruta al archivo de entrada
INPUT_PATH = "/usr/share/myapp/inputs/conduccion_1.mp4"
INPUT_URI = f"file://{INPUT_PATH}"

# Pipeline GStreamer para video
pipeline_str = (
    f'filesrc location={INPUT_PATH} ! '
    f'decodebin ! '
    f'videoconvert ! '
    f'videoscale ! '
    f'video/x-raw,width=320,height=180 ! '
    f'appsink sync=true'
)

# Ejecutar pipeline para capturar frames
cap = cv2.VideoCapture(pipeline_str, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error al abrir GStreamer pipeline")
    exit()

# Bucle de procesamiento de video
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al leer el siguiente frame.")
        break

    # Preprocesamiento
    resized = cv2.resize(frame, (input_layer.shape[3], input_layer.shape[2]))  # Redimensionamos al tamaño de entrada del modelo
    input_blob = np.expand_dims(resized.transpose(2, 0, 1), 0)  # Convertimos la imagen al formato CxHxW y la agregamos al batch

    # Realizar la inferencia con OpenVINO
    try:
        results = compiled_model([input_blob])[output_layer]
    except Exception as e:
        print(f"Error al realizar la inferencia: {e}")
        break

    # Postprocesamiento y dibujo de resultados
    for detection in results[0][0]:
        confidence = float(detection[2])
        if confidence > 0.3:  # Umbral de confianza
            xmin = int(detection[3] * frame.shape[1])
            ymin = int(detection[4] * frame.shape[0])
            xmax = int(detection[5] * frame.shape[1])
            ymax = int(detection[6] * frame.shape[0])

            # Dibujar el rectángulo y la etiqueta
            label = "Vehicle"
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostrar el resultado
    cv2.imshow('Detección de Vehículos', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

