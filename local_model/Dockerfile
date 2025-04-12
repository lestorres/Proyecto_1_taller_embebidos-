ARG OS_VER="2023.0.0-ubuntu22-gpu682-dpcpp-devel"
FROM intel/dlstreamer:${OS_VER}

USER root

# Instala dependencias de sistema
RUN apt-get update && apt-get install -y \
    git \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgirepository1.0-dev \
    python3-gi \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    && rm -rf /var/lib/apt/lists/*

# Desinstala OpenCV preinstalado y compila OpenCV 4.7.0 con GStreamer
RUN pip3 uninstall -y opencv-python && \
    git clone https://github.com/opencv/opencv.git && \
    cd opencv && git checkout 4.7.0 && \
    mkdir build && cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D WITH_GSTREAMER=ON \
          -D BUILD_opencv_python3=ON \
          -D PYTHON_EXECUTABLE=$(which python3) .. && \
    make -j$(nproc) && make install && \
    cd / && rm -rf opencv

# Cambia a usuario dlstreamer (mejor práctica)
USER dlstreamer

# Instala dependencias de Python
RUN pip3 install --no-cache-dir pillow matplotlib numpy PyGObject

# Establece carpeta de trabajo
WORKDIR /home/dlstreamer/app

# Copia tu código (modifica si usas .dockerignore)
COPY . .

# Comando por defecto para correr tu script
CMD ["python3", "deteccion.py"]
