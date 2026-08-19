# Parrilla

EL proyecto consiste en construir un software capaz de calcular el costo de los pedidos en una parilla de alta demanda.
En la cual se sabe el precio de los items.

Las ventas se van a guardar inicialmente en un CSV y luego se espera que se guarden en un Excel.
Al principio solo se almacenaran: "Que se vendio" (o "Productos") y "Monto".

Una vez que se pase al Excel se esperan mas columnas como fecha, medio de pago, extranjeros (si o no), etc.

La primera versión sera solo ejecutable mediante consola, quizas en un futuro tenga su versión web o mobile.

Se espera que para el MVP se pueda:

- Leer precios de un csv "precios.csv"
- Menu interactuable para tomar la orden por consola
- Guardar ventas en un archivo "ventas.csv"