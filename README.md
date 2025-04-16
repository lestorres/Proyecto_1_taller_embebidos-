# Proyecto 1: Sistema operativo a la medida 

El objetivo del proyecto es desarrollar un sistema operativo a la medida para  aplicaciones embebidas de multimedia con el marco de trabajo de Intel DLStreamer y el flujo de síntesis de Yocto Project


## Aplicación Elegida:
"Detección de Vehículos y Personas en cámaras dashcam de vehículos mediante Intel Openvino + DLStreamer y Yocto Project"


## DockerFile
Comandos para levantar el contenedor Docker de la aplicacion


- docker compose build dlstreamer

- docker compose run --rm dlstreamer
  - python3 deteccion.py



## Yocto 
### Estructura de archivos de los contenidos importantes de yocto

yocto/
│
├── meta-mylayer/
│   │
│   ├── conf/
│   │   └── layer.conf
│   ├── recipes-example/
│   │
│   └── local_model 
│
├── build-templates/
│   │
│   ├── local.conf
│   └── bblayers.conf
│
└── other-scripts/



###Crear imagen

- bitbake core-image-minimal

### Emular imagen generada

- runqemu qemux86-64




