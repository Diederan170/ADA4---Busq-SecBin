[readme_m_todos_de_b_squeda.md](https://github.com/user-attachments/files/35107619/readme_m_todos_de_b_squeda.md)
# Métodos de Búsqueda en Python

Programa interactivo con menú de opciones que reúne tres ejercicios prácticos de búsqueda en un solo archivo (`metodos_busqueda.py`). Antes de solicitar los datos, el sistema muestra instrucciones claras sobre qué números se pueden ingresar y cuáles no, y presenta paso a paso cómo localiza el valor buscado.

## Ejercicios incluidos

1. **Búsqueda Secuencial – Folios de asistencia:** Busca un folio (números enteros mayores a 0 en cualquier orden) revisando la lista elemento por elemento desde el principio hasta encontrarlo o llegar al final.
2. **Búsqueda Binaria – Catálogo de precios ordenado:** Localiza un precio (números mayores a 0 ingresados de menor a mayor) partiendo la lista por la mitad en cada paso y descartando la mitad donde no puede estar el valor.
3. **Búsqueda Hash – Códigos de casilleros:** Guarda cada código (números enteros mayores a 0 en cualquier orden) en una casilla calculada mediante residuo (`%`) para ir directamente a su ubicación sin recorrer toda la lista.

## Requisitos
* Tener instalado **Python 3**.

## Cómo ejecutarlo
1. Abre una terminal en la carpeta donde guardaste el archivo `metodos_busqueda.py`.
2. Ejecuta el comando:
   ```bash
   python metodos_busqueda.py
   ```
3. Elige en el menú el método de búsqueda que deseas probar (opciones `1` a `3`), revisa las reglas de captura en pantalla, ingresa los datos y escribe el número que deseas localizar. Para cerrar el programa, selecciona la opción `4`.
