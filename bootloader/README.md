# Información del bootloader

El bootloader que viene en el micro HR_C7000 del DM32-UV [parece ser muy similar al descripto en esta página](https://github.com/MarcinWad/CHIPUP/blob/main/README.md?plain=1#L66), por lo que se puede usar el mismo procedimiento para cargar datos en memoria y ejecutarlo.

Todos los comandos a 115200 8N1.

- Cuando se inicia, el HT manda "02 24 00 03". Luego de un rato bootea normalmente si no se le contesta (si pasa eso escribe "00 10 00 03 00" al parecer).
- Si se contesta "02 14 00 03" entra al modo de pruebas de fábrica

## Escrituras en memoria
Para escribir en posiciones de memoria arbitrarias, puede usarse un comando "02 18 xx 03", donde xx es un checksum básico de la suma de los bytes enviados en "data+size+address".
- Luego se envía la dirección, por ejemplo "00 01 00 00"
- Luego se envía el tamaño en bytes, por ejemplo "00 00 00 40" (64 bytes)
- Luego se envía el bloque de datos, por ejemplo: "74 09 01 00 f0 09...""
Al llegar a los N bytes enviados, el micro luego contesta "02 05 00 03". Si el tercer byte es 00 está todo OK.

## Ejecución de código
Para ejecutar código desde alguna posición de memoria, puede usarse un comando "02 1b xx 03" donde xx es un checksum básico de la suma de los bytes enviados en "address". 
Luego se envía la dirección a la cual saltar, por ejemplo "00 01 09 74".
El micro contesta "02 05 00 03". Si el tercer byte es 00 está todo OK. Y luego salta al lugar indicado.

## Créditos
Parte de la info de acá fue obtenida haciendo ingeniería inversa a este [dumper/flasher](http://infotex58.ru/forum/index.php?topic=1155.0), puede no estar 100% correcta.
