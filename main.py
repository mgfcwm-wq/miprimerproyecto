import json

with open('C:/Proyectos/MiPrimerProyecto/data/data.json', 'r') as file:
  datos = json.load(file)

# 1. Gasto total por usuario: Muestra el nombre de cada usuario y el dinero total que ha gastado. 
# Si un usuario no tiene compras (como david_perez), debe mostrar 0.00 €.
print("1. Gasto total por usuario:")
for usuario, compras in datos.items():
    # Sumamos el precio de cada producto de la lista del usuario.
    # Si la lista está vacía (como david_perez), sum() devuelve 0 automáticamente.
    gasto_total = sum(item.get("precio") or 0.0 for item in compras)  
    print(f"- {usuario}: {gasto_total:.2f} €")

# 2. Cliente VIP (Mayor gasto): Indica qué usuario ha gastado más dinero en total y cuál ha sido esa cantidad.
print("\n2. Cliente VIP (Mayor gasto):")
max_gasto = 0
vip_usuario = ""
for usuario, compras in datos.items():
    gasto_total = sum(item.get("precio") or 0.0 for item in compras)
    if gasto_total > max_gasto:
        max_gasto = gasto_total
        vip_usuario = usuario

print(f"\nCliente VIP: {vip_usuario} con un gasto total de {max_gasto:.2f} €")

# 3. Cliente con más artículos: Indica qué usuario ha comprado mayor cantidad de productos (sin importar el precio) y cuántos fueron.
print("\n3. Cliente con más artículos:")
max_articulos = 0
articulos_usuario = ""
for usuario, compras in datos.items():
    cantidad_articulos = len(compras)
    if cantidad_articulos > max_articulos:
        max_articulos = cantidad_articulos
        articulos_usuario = usuario

print(f"\nCliente con más artículos: {articulos_usuario} con {max_articulos} productos comprados.")

# 4. Producto más caro y más barato: Encuentra entre todas las compras de todos los usuarios cuál es el producto más caro y cuál es el más barato. Muestra su nombre, su precio y qué usuario lo compró.
print("\n4. Producto más caro y más barato:")

mas_caro = None
mas_barato = None

for usuario, compras in datos.items():
    gasto_total = 0.0
    
    for item in compras:
        precio = item.get("precio")
        if precio is None:
            continue
            
        # 1. Sumamos al total del usuario actual
        gasto_total += precio
        
        # 4. Comparamos directamente para actualizar el más caro y el más barato
        if mas_caro is None or precio > mas_caro["precio"]:
            mas_caro = {"producto": item["producto"], "precio": precio, "usuario": usuario}
            
        if mas_barato is None or precio < mas_barato["precio"]:
            mas_barato = {"producto": item["producto"], "precio": precio, "usuario": usuario}

    print(f"- {usuario}: {gasto_total:.2f} €")

print("Producto más caro y más barato:")

if mas_caro and mas_barato:
    print(f"- Más caro: {mas_caro['producto']} ({mas_caro['precio']:.2f} €) - Comprado por: {mas_caro['usuario']}")
    print(f"- Más barato: {mas_barato['producto']} ({mas_barato['precio']:.2f} €) - Comprado por: {mas_barato['usuario']}")
else:
    print("- No hay compras registradas.")

# 5. Resumen por categorías : Crea un nuevo diccionario dinámico que calcule cuánto dinero se ha gastado en total en cada categoría 
# (ej. {"Informática": 325.44, ...}) y muéstralo por pantalla.
print("\n5. Resumen por categorías:")

resumen_categorias = {}
for usuario, compras in datos.items():
    for item in compras:
        categoria = item.get("categoria")
        precio = item.get("precio")
        if categoria and precio is not None:
            if categoria not in resumen_categorias:
                resumen_categorias[categoria] = 0
            resumen_categorias[categoria] += precio

for categoria, gasto in resumen_categorias.items():
    print(f"- {categoria}: {gasto:.2f} €")

# 6. Productos con IVA : esos precios son sin IVA -que gran error-, incluye un nuevo atributo 'precioIVA' siendo el valor el calculo de $precio*1.21$
# 7. Crea un fichero CSV, llamado contabilidad_a.csv donde cada muestra sea: producto y precioIVA.
print("\n6. Productos IVA:")
lista_contabilidad = []

for usuario, compras in datos.items():
    print(f"\nUsuario: {usuario}")
    if not compras:
        print("  - Sin compras registradas.")
        
    for item in compras:
        precio = item.get("precio")
        if precio is not None:
            # Añadimos el nuevo atributo 'precioIVA' al diccionario original
            item["precioIVA"] = round(precio * 1.21, 2)
            
            # Imprimimos por pantalla el resultado de cada producto
            print(f"  - {item['producto']}: {precio:.2f} € (Sin IVA) -> {item['precioIVA']:.2f} € (Con IVA)")
            
            # Añadimos la muestra para el fichero de salida
            lista_contabilidad.append({
                "producto": item["producto"],
                "precioIVA": item["precioIVA"]
            })

# Escribimos el fichero usando json.dump()
with open("data_output.csv", "w", encoding="utf-8") as fichero_salida:
    json.dump(lista_contabilidad, fichero_salida, indent=4, ensure_ascii=False)

print("\n7. Fichero 'data_output.csv' generado en formato JSON correctamente.")
