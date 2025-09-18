# DM32-UV
Links a varias cosas interesantes para el _HT Baofeng DM32-UV_.

Por LU6CGA (gzalo), si encontrás algo interesante podés crear un _pull request_ para agregarlo a la lista.

# Cosas básicas
- [Manual](https://baofeng.s3.amazonaws.com/Baofeng_DM-32UV_User_Manual_20250210.pdf)
- [Software para programar (DMR CPS), desde Windows o Linux con Wine](https://baofeng.s3.amazonaws.com/Baofeng_DM-32UV_CPS_v1.41.zip)
- [Software para programar desde Android (OLA Radio)](https://play.google.com/store/apps/details?id=com.aewt.app.friends&hl=es_AR)
- [Pasos para conectarse desde el OLA Radio](pasos_ola.png)
- [Software para cambiar imagen de inicio](https://baofeng.s3.amazonaws.com/Baofeng_DM-32UV_Picture_Tool.zip)
- [Video explicativo de cambio de imagen de inicio](https://www.youtube.com/watch?v=kkBoR580_Q0)
- [Script para convertir CSV de CHIRP en CSV de CPS](https://github.com/gzalo/Quansheng-DM32UV-Chirp-to-DM32-channel-list-)

## Contraseñas
El software DMR CPS puede pedir contraseñas en algunos casos, las mismas son:
- Embedded info: 374612
- Adjust mode: 66660501

# Cosas avanzadas
- [Medición de armónicos en transmisiones analógicas, en potencia HIGH](armonicos.png)
- [Ajuste de potencia de transmisión, ideal uso con hotspots cercanos](power.png)
- La última version del firmware parecería ser [`DM32_049_20250905.bin`](http://infotex58.ru/forum/index.php?topic=1148.msg10422#msg10422), aunque no está en el sitio oficial de Baofeng.
- El chip principal es un HR_C7000, está disponible un [datasheet bastante completo (en chino)](https://www.connectsystems.com/products/top/radios/CS120D/HR_C7000%20Document%202.pdf). Usa un procesador raro, CK803S, de C-SKY (ahora parte de Alibaba), con arquitectura RISC de 32 bits. Tiene 288 KB de RAM y flash externa.
- El firmware no está hasheado ni encriptado, se puede modificar manualmente con un editor hexadecimal 
- [Manual de servicio (con esquemáticos y detalles de calibración) de un HT similar que usa el mismo micro, aunque sin pantalla color](https://www.connectsystems.com/products/top/radios/CS120D/DR5800-2%20ServiceManua01.pdf)
- [Dumper de memorias internas](http://infotex58.ru/forum/index.php?topic=1155.0)
- Algunas tipografías están en el firmware en formato bitmap, se pueden extraer y modificar, mientras que otras pueden ser flasheadas por separado.
- Es posible cambiar las voces del HT (las que se usan cuando _Voice prompt_ está activado) flasheando un archivo separado, que tiene un header apuntando a las distintas frases en formato WAV, y luego las mismas en formato WAV 8kHz mono 16 bits.
- Hay equipos realizando ports para otros HTs con el mismo micro (HR_C7000), pero no para el DM32-UV.

# Otros repositorios con información
- http://infotex58.ru/forum/index.php?topic=1148.330
- https://github.com/yo3hjv/Baofeng-DM32
- https://github.com/antnesswcm/Baofeng-DM32UV-Reverse (vacío)
- https://github.com/M7OCM/DM-32UV
- https://www.opengd77.com/archive/viewtopic51ba.html?f=10&t=5142&
- https://vrtp.ru/index.php?showtopic=33914&st=0
