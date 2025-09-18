# Cambio de voces
Desde la tool de CPS se puede flashear un archivo ENC con las voces. 
El mismo archivo tiene un header apuntando a las distintas frases, y luego las mismas, en formato WAV 8kHz mono 16 bits.

Con el script [combine.py](voice/combine.py) se pueden armar un archivito similar, **pero es necesario bajar [los archivos originales desde este post](http://infotex58.ru/forum/index.php?topic=1148.msg10317#msg10317)**, y el [0x00.wav](0x00.wav) que contiene los datos del header original.
Al modificar los WAV, es importante mantener la misma duración (en bytes) que el original, para no descalibrar los offsets del header.

En el futuro se modificará el script para que ajuste los offsets automáticamente.