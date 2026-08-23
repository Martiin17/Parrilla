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

## Sprint 2

Como paso previo al guardado en el Excel, se va a utilizar la libreria SupaBase para guardar los datos en una base de datos relacional. Al ser poco trafico de datos se utilizara la versión gratuita que cuenta con un limite más que suficiente para las necesidades de este proyecto.

## Sprint 3

Se utilizara Streamlit con el fin de contar con un frontend sencillo e intuitivo. Ademas de la posibilidad de poder usar el software desde el celular.

## Descubrimiento de Nueva Tecnologia

En la búsqueda de librerías y bases de datos para avanzar con el proyecto me tope con que Google cuenta con un Software llamado "AppSheet" que crea páginas con las funciones que necesito. Una vez realizada pondre el link aquí!
