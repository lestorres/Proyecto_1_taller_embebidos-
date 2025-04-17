# Proyecto 1: Sistema operativo a la medida 

El objetivo del proyecto es desarrollar un sistema operativo a la medida para  aplicaciones embebidas de multimedia con el marco de trabajo de Intel DLStreamer y el flujo de síntesis de Yocto Project


## Aplicación Elegida:
"Detección de Vehículos y Personas en cámaras dashcam de vehículos mediante Intel Openvino + DLStreamer y Yocto Project"


## DockerFile
Comandos para levantar el contenedor Docker de la aplicacion

```plaintext
 docker compose build dlstreamer
```
```plaintext
docker compose run --rm dlstreamer
```
Una vez levantado el docker, se debe ejecutar el script de la siguiente manera.

```plaintext
python3 deteccion.py
```


## Yocto

### Estructura de archivos de los contenidos importantes de Yocto en github

```plaintext
yocto/
│
├── meta-mylayer/
│   ├── conf/
│   │   └── layer.conf
│   ├── recipes-example/
│   └── local_model/
│
├── build-templates/
│   ├── local.conf
│   └── bblayers.conf
│
└── other-scripts/
```


### Crear imagen

```plaintext
bitbake core-image-minimal
```

### Emular imagen generada

```plaintext
runqemu qemux86-64
```

### Conexión ssh para utilizar ventanas de la computadora (única parada cada computadora)

```plaintext
ssh -X root@192.168.7.2
```

