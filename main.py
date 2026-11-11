from tinydb import TinyDB, Query

#Abre o crea archivo json
db = TinyDB("inventario.json", indent=4)

#Crea la tabla en la base de datos para los productos. Como en el ejemplo ID | Nombre de la clase.
productos = db.table("productos")

#Truncate borra lo que hubiera antes de esa colección para evitar datos duplicados al correr de nuevo el programa.
productos.truncate()

#Plantilla con lo que se le mete a la base de datos.
productos.insert_multiple([
    {
        "id": "P01",
        "tipo": "laptop",
        "marca": "Lenovo",
        "modelo": "ThinkPad T14",
        "precio": 950,
        "specs": {"cpu": "Ryzen 7", "ram": 16}
    },
    {
        "id": "P02",
        "tipo": "monitor",
        "marca": "Dell",
        "pulgadas": 24,
        "hz": 144,
        "precio": 210
    },
    {
        "id": "P03",
        "tipo": "mouse",
        "marca": "Logitech",
        "modelo": "G305",
        "inalambrico": True,
        "precio": 45
    }
])

#Print simple
print("Productos cargados en la Base de Datos")
for p in productos.all():
    print(p)

#Item = Query() crea un objeto comodín Item que representa cualquier documento dentro de la base de datos para
#poder armar condiciones sobre sus campos.
Item = Query()

print("\nProductos menores a $300")
baratos = productos.search(Item.precio < 300)
for b in baratos:
    print(f"{b['tipo']} {b['marca']} - ${b['precio']}")

print("\nProductos inalambricos")
wireless = productos.search(Item.inalambrico == True)
for w in wireless:
    print(w)

#Busca el documento cuyo ID coincida, cambia el precio y le agrega una nueva llave que antes no existía.
productos.update({"precio": 890, "descuento": True}, Item.id == "P01")
print("\nLaptop actualizada")
print(productos.get(Item.id == "P01"))


productos.remove(Item.id == "P02")
print(f"\nTotal de documentos despues de eliminar P02: {len(productos)}")
