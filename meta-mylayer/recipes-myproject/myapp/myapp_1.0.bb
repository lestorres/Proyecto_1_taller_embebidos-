SUMMARY = "Aplicación de detección de objetos con DL Streamer y reproducción de video"
DESCRIPTION = "Este paquete incluye una aplicación Python para detección de objetos utilizando DL Streamer, junto con un script para reproducir videos mediante GStreamer."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI += "file://deteccion.py \
            file://reproducir.py \
            file://inputs \
            file://model_proc \
            file://models \
            file://utils"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}/myapp

    install -m 0755 ${WORKDIR}/deteccion.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/reproducir.py ${D}${bindir}/myapp/

    cp -r ${WORKDIR}/inputs ${D}${bindir}/myapp/
    cp -r ${WORKDIR}/model_proc ${D}${bindir}/myapp/
    cp -r ${WORKDIR}/models ${D}${bindir}/myapp/
    cp -r ${WORKDIR}/utils ${D}${bindir}/myapp/
}
