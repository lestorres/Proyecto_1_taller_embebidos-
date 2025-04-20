# Proyecto 1: Sistema operativo a la medida 
El objetivo del proyecto es desarrollar un sistema operativo a la medida para  aplicaciones embebidas de multimedia con el marco de trabajo de Intel DLStreamer y el flujo de síntesis de Yocto Project

## Aplicación Elegida: 
**Aplicación elegida**: Vehicle and pedestrian tracking using Intel Openvino + DLStreamer and Docker.

**Problematica a resolver**: Integración Intel Openvino + DLStreamer y Yocto Project para la detección de vehículos y personas implementado en cámaras dashcam de vehículos.

## Descripción del proyecto
El proyecto consta de 2 secciones: 
- El desarrollo de la aplicación en un contenedor mediante Docker.
- El desarrollo de la aplicación en un sistema operativo a la medida mediante YoctoProject.

Dentro del tutorial se encontrará el paso a paso en el flujo de desarrollo de ambas presentaciones de la aplicación.

**Nota:** La integración de Dlstreamer dentro del sistema operativo a la medida mediante YoctoProject aún **NO** se encuentra disponible.


# Tutorial

### Descripción del Computador Host
El desarrollo del proyecto se realizó en un entorno virtualizado utilizando Ubuntu 24.04.2 LTS bajo WSL2 (Windows Subsystem for Linux) sobre una máquina host con Windows 11. A continuación, se describen las especificaciones relevantes del computador:

- **Fabricante:** Acer
- **Modelo:** Predator PHN16-71
- **Sistema operativo:** Microsoft Windows 11 Home, versión 10.0.26100 Build 26100
- **Procesador:** Intel Core i5-13500HX de 13ª generación, 14 núcleos físicos, 20 hilos, frecuencia base de 2.5 GHz
- **Memoria RAM instalada:** 16 GB
- **Tipo de sistema:** PC basado en x64
- **Modo de BIOS:** UEFI
- **Virtualización:** Seguridad basada en virtualización activa
- **Estado de Secure Boot:** Activado

**Entorno de desarrollo - Ubuntu (WSL2):**
- **Distribución:** Ubuntu 24.04.2 LTS sobre Windows 11 vía WSL2
- **Kernel:** 5.15.167.4-microsoft-standard-WSL2
- **Shell:** Bash 5.2.21
- **Número de paquetes instalados:** 1483 (`dpkg`)
- **Memoria disponible al momento del escaneo:** 463 MiB / 15.7 GiB
- **Tema e íconos:** Adwaita (GTK3)
- **GPU (virtual):** Microsoft Basic Render Driver (limitado en WSL2)

## Configuración del Entorno: Contenedor Docker

### Prerequisitos para la Configuración del Entorno: Contenedor Docker
Como prerequisito se debe clonar el repositorio Proyecto_1_taller_embebidos e instalar Docker

* [Docker](https://docs.docker.com/engine/install/ubuntu/)

### Estructura de archivos para el contenedor Docker y pasos a seguir

```plaintext
local_model/
│
├── compose.yaml
├── deteccion.py
├── Dockerfile
├── model_proc/
├── models/
├── inputs/
├── outputs/
└── utils/

```
El directorio local_model basado en [1], incluye dentro los archivos: **compose.yaml** y **Dockerfile** estos configuran el entorno necesario para la aplicación, esta se encuentra dentro del script deteccion.py, que utiliza los modelos incluidos en le directorio models y sus scripts dentro de model_proc.


Utilizando una terminal Linux dentro del directorio local_model, los pasos a seguir son: 
1. Contruir el contenedor Docker de la aplicación.

```plaintext
docker compose build dlstreamer
```
2. Levantar el contenedor Docker con una terminal habilitada.
   
```plaintext
docker compose run --rm dlstreamer
```
3. Una vez levantado el docker con su terminal, se debe ejecutar el script de la siguiente manera.

```plaintext
python3 deteccion.py
```
A este punto el modelo debe mostrar lo siguiente: 




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
python3 reproducir.py
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

# Referencias
[1] L. Murillo, "openvino-workshop-tec," GitHub, 2025. [Online]. Available: https://github.com/lumurillo/openvino-workshop-tec



