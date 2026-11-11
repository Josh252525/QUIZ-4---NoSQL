# Quiz #4 - Bases de Datos NoSQL

**Curso:** Algoritmos y Estructuras de Datos II  
**Institución:** Instituto Tecnológico de Costa Rica  
**Estudiante:** Josué Daniel Vargas Arias.
**Carnet:** 2025068102
**Fecha:** 10/11/2026

## Tipo de base de datos seleccionada
Se escogió una base de datos NoSQL del tipo **orientada a documentos**, implementada por medio de Python utilizando la librería TinyDB (almacenamiento local en formato JSON).

## Escenario del problema
Para el problema, se modeló el inventario de una tienda de electrónicos donde se manejan distintos tipos de artículos, como laptops o monitores. El reto principal es que cada categoría maneja atributos distintos, como una laptop la cual necesita registrar procesador y memoria RAM, un monitor necesita el tamaño en pulgadas y tasa de refresco, y un mouse si es inalámbrico o no.

## Cómo se resolvió con NoSQL
En una base de datos relacional tradicional habría que crear una tabla con muchas columnas que quedarían en `NULL` para varios productos, o dividir todo en varias tablas. Al usar un enfoque orientado a documentos, cada producto se guarda en la tabla `productos` como un documento JSON independiente que solo contiene los atributos que realmente ocupa.

En el archivo `main.py` se prueban las operaciones principales sobre estos documentos:
* Se insertan varios artículos con distinta estructura, incluyendo diccionarios anidados como `specs` en el caso de la laptop.
* Se hacen consultas filtrando por precio menor a $300 y buscando atributos que solo existen en ciertos documentos (como `inalambrico`).
* Se actualiza el precio de un producto agregándole un campo nuevo (`descuento`) sin tener que modificar el esquema de los demás registros.
* Se elimina uno de los productos por su `id`.

## Cómo ejecutarlo
Instalar la librería para la base de datos:
```bash
pip install tinydb
```

Ejecutar el programa:
```bash
python main.py
```
Al correrlo se crea el archivo `inventario.json` con los datos guardados.