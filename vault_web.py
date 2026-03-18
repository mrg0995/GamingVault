import streamlit as st
import json
import os

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="GamingVault", page_icon="🎮", layout="wide")

# --- 2. FUNCIONES DE PERSISTENCIA ---
def cargar_biblioteca():
    if os.path.exists('biblioteca_juegos.json'):
        with open('biblioteca_juegos.json', 'r') as archivo:
            return json.load(archivo)
    return {}

def guardar_biblioteca(datos):
    with open('biblioteca_juegos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4, sort_keys=True)

# Nueva función específica para borrar
def borrar_juego(nombre_juego):
    if nombre_juego in st.session_state.biblioteca:
        del st.session_state.biblioteca[nombre_juego]
        guardar_biblioteca(st.session_state.biblioteca)
        st.rerun()

# Cargamos los datos al inicio
if 'biblioteca' not in st.session_state:
    st.session_state.biblioteca = cargar_biblioteca()

# --- 3. INTERFAZ: BARRA LATERAL ---
with st.sidebar:
    st.header("➕ Añadir Nuevo Juego")
    with st.form("formulario_juego", clear_on_submit=True):
        nombre = st.text_input("Nombre del Juego").strip().title()
        plataforma = st.selectbox("Plataforma", ["PC", "PS5", "XBOX", "SWITCH", "RETRO"])
        completado = st.checkbox("¿Completado? ✅")
        platino = st.checkbox("¿Platino? 🏆")
        
        btn_añadir = st.form_submit_button("Guardar en la Bóveda")
        
        if btn_añadir and nombre:
            st.session_state.biblioteca[nombre] = {
                'plataforma': plataforma,
                'completado': completado,
                'platino': platino
            }
            guardar_biblioteca(st.session_state.biblioteca)
            st.success(f"¡{nombre} añadido!")
            st.rerun()

# --- 4. CUERPO PRINCIPAL ---
st.title("🎮 GamingVault: Tu Bóveda de Juegos")

# Estadísticas
total = len(st.session_state.biblioteca)
completados = sum(1 for j in st.session_state.biblioteca.values() if j['completado'])
platinos = sum(1 for j in st.session_state.biblioteca.values() if j['platino'])

col_a, col_b, col_c = st.columns(3)
col_a.metric("Total Juegos", total)
col_b.metric("Completados", completados)
col_c.metric("Platinos", platinos)

st.divider()

# Buscador
busqueda = st.text_input("🔍 Busca un juego en tu colección...", "").strip().title()

# Filtrar y Mostrar
datos_filtrados = {k: v for k, v in st.session_state.biblioteca.items() if busqueda in k}

if datos_filtrados:
    # Cabecera de la tabla manual
    c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
    c1.write("**Nombre**")
    c2.write("**Plataforma**")
    c3.write("**Estado**")
    c4.write("**Acción**")
    
    for nombre_juego, info in datos_filtrados.items():
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        
        with col1:
            st.write(nombre_juego)
        with col2:
            st.write(info['plataforma'])
        with col3:
            estado = "🏆 Platino" if info['platino'] else ("✅ Completado" if info['completado'] else "⏳ Pendiente")
            st.write(estado)
        with col4:
            # Usamos el nombre del juego como key única para el botón
            if st.button("🗑️", key=f"borrar_{nombre_juego}"):
                borrar_juego(nombre_juego)
else:
    st.info("No hay juegos que coincidan con la búsqueda.")