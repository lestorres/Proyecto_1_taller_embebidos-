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

## Emulación de la imagen con Qemu

### Emular imagen generada

```plaintext
runqemu qemux86-64
```

### Conexión ssh para utilizar el gestor de ventanas de la computadora (única para cada computadora)

```plaintext
ssh -X root@192.168.7.2
```

### Prueba de multimedia Gstreamer
```plaintext
gst-launch-1.0 videotestsrc ! videoconvert ! autovideosink
```

### Verificar el contenido de la aplicación
Al ingresar:

```plaintext
ls /usr/bin/myapp
```
Debe aparecer algo similar a esto:

```plaintext
deteccion.py  inputs/  model_proc/  models/  utils/ reproducir.py
```

### Ingresar y ejecutar el contenido de la aplicación
Ingresar al directorio de la aplicación
```plaintext
cd /usr/bin/myapp
```

### Prueba de multimedia de videos de entrada con Gstreamer
```plaintext
gst-launch-1.0 filesrc location=/usr/bin/myapp/inputs/conduccion_1.mp4 ! decodebin ! videoconvert ! ximagesink
```

## VirtualBox
La imagen una vez cocinada, se encontrará ubicada en el directorio:

```plaintext
~/yocto/poky/build/tmp/deploy/images/qemux86-64
```

La imagen a utilizar en Virtual-Box será:

```plaintext
core-image-minimal-qemux86-64.rootfs-20250418215706.wic.vdi
```

Se debe configurar una dirección ip para acceder a la máquina virtual

```plaintext
dhcpcd eth0
```

Verificar la ip de eth0

```plaintext
ip a
```

### Conexión ssh para utilizar el gestor de ventanas de la computadora

```plaintext
ssh -X root@<ip-eth0>
```

### Verificar el contenido de la aplicación
Al ingresar:

```plaintext
ls /usr/bin/myapp
```
Debe aparecer algo similar a esto:

```plaintext
deteccion.py  inputs/  model_proc/  models/  utils/ reproducir.py
```

### Ingresar y ejecutar el contenido de la aplicación
Ingresar al directorio de la aplicación
```plaintext
cd /usr/bin/myapp
```

### Prueba de multimedia de videos de entrada con Gstreamer
```plaintext
python3 reproducir.py
```


