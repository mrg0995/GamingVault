# 🎮 Gestor de Videojuegos Personal (Python)

¡Bienvenido a mi primer proyecto de gestión de datos! Este programa es un **CRUD** (Create, Read, Update, Delete) desarrollado en Python, diseñado para ayudar a coleccionistas y jugadores a llevar un control exhaustivo de su biblioteca.

Surgió como una herramienta práctica para organizar mis juegos (especialmente la saga *Kingdom Hearts* 🗝️) y poner en práctica conceptos avanzados de programación.

---

## 🚀 Características Principales

* **Persistencia de Datos:** Los juegos se guardan en un archivo `biblioteca_juegos.json`, por lo que no pierdes nada al cerrar el programa. 💾
* **Buscador Inteligente:** Filtra juegos por nombre sin necesidad de escribir el título completo. 🔍
* **Normalización de Datos:** No importa si escribes en mayúsculas o minúsculas, el sistema organiza todo con formato de título (.title()). ✨
* **Gestión de Estados:** Controla si has completado el juego ✅ y si has obtenido el trofeo de Platino 🏆.
* **Orden Alfabético:** La biblioteca se muestra siempre perfectamente ordenada de la A a la Z. 📚

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Formato de datos:** JSON (JavaScript Object Notation)
* **Librerías nativas:** `json`, `os`

---

## 📋 Cómo Funciona

1.  **Añadir/Editar:** Escribe el nombre de un juego. Si no existe, se crea; si existe, se abre el menú de edición.
2.  **Buscar:** Escribe la palabra `Buscar` para localizar juegos específicos en tu colección.
3.  **Borrar:** Dentro del menú de un juego existente, puedes eliminarlo definitivamente.
4.  **Salir:** Escribe `Salir` para guardar todos los cambios y cerrar la aplicación.



---

## ✒️ Autor

* **Mario Ramírez** - *Full Stack Developer* (https://github.com/mrg0995)

---

> *"Mejor algo pequeño que funcione bien, a algo gigante que no entiendas."* — Mi filosofía de aprendizaje en este proyecto. 💡
