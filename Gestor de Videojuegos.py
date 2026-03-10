"""
PROYECTO: Gestor de Biblioteca de Videojuegos 🎮
AUTOR: Mario Ramírez/mrg0995
DESCRIPCIÓN: Programa para gestionar, buscar y guardar una colección de juegos 
             con persistencia en archivo JSON.
VERSIÓN: 1.0
"""

import json
import os

biblioteca_juegos = {}

# 1. Funcion de gaurdado optimizada
def guardar_biblioteca(datos):
    with open('biblioteca_juegos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4, sort_keys=True)
        
# 2. Carga inicial
print("-----🎮Bienvenido al Gestor de Videojuegos🎮-----")
if os.path.exists('biblioteca_juegos.json'):
    with open('biblioteca_juegos.json', 'r') as archivo:
        biblioteca_juegos = json.load(archivo)
    print("Datos cargados desde 'biblioteca_juegos.json'.")
else:
    print("No existe biblioteca")
while True:
    nombre_juego = input("🎮Ingrese el nombre del juego, 'buscar' o 'salir'): ")
    nombre_juego = nombre_juego.strip().title()
    if nombre_juego == 'Buscar':
        buscar_juego = input("🔍Ingrese el nombre del juego a buscar: ")
        buscar_juego = buscar_juego.strip().title()
        encontrados = False
        print(f"\n🎮Buscando {buscar_juego}🎮")
        for juego, info in biblioteca_juegos.items():
            if buscar_juego in juego:
                comp = "✅" if info['completado'] else "❌"
                plat = "🏆" if info['platino'] else "❌"
                print(f"- {juego} ({info['plataforma']}): {info['completado']} | Platino: {info['platino']}")
                encontrados = True
        if not encontrados:
            print(f"🎮Ese juego no está registrado en esta biblioteca.🎮")
        continue
    if nombre_juego == 'Salir':
        break
    if not nombre_juego:
        print("El nombre del juego no puede estar vacío")
        continue
    if nombre_juego in biblioteca_juegos:
        print("🎮El juego ya está en la biblioteca.🎮\n")
        print("¿Qué desea hacer? [A]ctualizar Platino🏆, [B]orrar❌, [C]ompletar✅, [S]alir al menú.🚫")
        accion = input("Elige una opción (A/B/C/S)").lower()
        if accion == 'a':
            nuevo_platino = input("¿Tienes el Platino🏆? (s/n)").lower() in ['s', 'si']
            biblioteca_juegos[nombre_juego]['platino'] = nuevo_platino
            guardar_biblioteca(biblioteca_juegos)
            print(f"🏆Platino conseguido para {nombre_juego}🏆")
            continue
        elif accion == 'b':
            del biblioteca_juegos[nombre_juego]
            guardar_biblioteca(biblioteca_juegos)
            print(f"❌{nombre_juego} eliminado❌")
            continue
        elif accion == 'c':
            nuevo_completado = input("¿Lo has completado✅? (s/n)").lower() in ['s', 'si']
            biblioteca_juegos[nombre_juego]['completado'] = nuevo_completado
            guardar_biblioteca(biblioteca_juegos)
            print(f"✅Completado {nombre_juego}✅")
            continue
        else:
            print("🚫Operación cancelada🚫")
            continue
    
    # Si el juego no estaba, se añade
    plataforma = input("Ingrese la plataforma del juego: ").lower().strip()
    completado = input("¿Has completado el juego? (s/n): ").lower().strip() in ['s', 'si']
    platino = input("¿Has conseguido el platino🏆? (s/n): ").lower().strip() in ['s', 'si']
    biblioteca_juegos[nombre_juego] = {
        'plataforma': plataforma,
        'completado': completado,
        'platino': platino
    }
    # Llamamos a la función para que se guarde
    guardar_biblioteca(biblioteca_juegos)
    print(f"Juego '{nombre_juego}' agregado y guardado automáticamente en la biblioteca.\n")

# 3. Resumen Final
print("\n" + "="*40)
print("📋 LISTA DE JUEGOS EN TU BIBLIOTECA")
print("="*40)
if not biblioteca_juegos:
    print("La Biblioteca está vacía")
else:
    for nombre, info in sorted(biblioteca_juegos.items()):
        comp = "✅" if info['completado'] else "❌"
        plat = "🏆" if info['platino'] else "❌"
        print(f"- {nombre} ({info['plataforma']}): {comp} | Platino: {plat}")
print("="*40)
print("Gracias por usar el gestor. ¡A jugar! 🕹️")