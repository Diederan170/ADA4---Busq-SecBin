def busqueda_secuencial(lista, objetivo):
    """
    Busca un elemento recorriendo la lista uno por uno desde el inicio
    hasta encontrarlo o llegar al final.
    """
    print(f"\nLista registrada: {lista}")
    print(f"Buscando el folio: {objetivo}\n")

    for indice, valor in enumerate(lista):
        print(f"Paso {indice + 1}: Comparando posición [{indice}] -> {valor} == {objetivo}?")
        if valor == objetivo:
            print(f"  -> ¡Encontrado en la posición {indice} (elemento #{indice + 1})!")
            return indice

    print("  -> Se recorrió toda la lista y el folio no está registrado.")
    return -1


def busqueda_binaria(lista_ordenada, objetivo):
    """
    Busca un elemento en una lista previamente ordenada de menor a mayor
    dividiendo el rango de búsqueda a la mitad en cada iteración.
    """
    print(f"\nCatálogo ordenado: {lista_ordenada}")
    print(f"Buscando el precio: {objetivo}\n")

    izquierda = 0
    derecha = len(lista_ordenada) - 1
    paso = 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista_ordenada[medio]
        sublista_actual = lista_ordenada[izquierda:derecha + 1]

        print(f"Paso {paso}: Rango [{izquierda}..{derecha}] {sublista_actual} | Centro [{medio}] = {valor_medio}")

        if valor_medio == objetivo:
            print(f"  -> ¡Precio encontrado en la posición {medio} (elemento #{medio + 1})!")
            return medio
        elif valor_medio < objetivo:
            print(f"  -> {valor_medio} es menor que {objetivo}: se descarta la mitad izquierda.")
            izquierda = medio + 1
        else:
            print(f"  -> {valor_medio} es mayor que {objetivo}: se descarta la mitad derecha.")
            derecha = medio - 1

        paso += 1

    print("  -> El precio buscado no existe en el catálogo.")
    return -1


def construir_tabla_hash(claves):
    """
    Crea una tabla hash utilizando encadenamiento (listas por cubeta)
    para manejar posibles colisiones mediante la función módulo.
    """
    tamano = max(5, len(claves))
    tabla = [[] for _ in range(tamano)]

    print(f"\nConstruyendo Tabla Hash de {tamano} casillas (función: código % {tamano}):")
    for clave in claves:
        indice = clave % tamano
        tabla[indice].append(clave)
        print(f"  Código {clave} -> {clave} % {tamano} = casilla [{indice}]")

    print("\nEstado de la Tabla Hash:")
    for i, cubeta in enumerate(tabla):
        print(f"  Casilla [{i}]: {cubeta}")

    return tabla


def busqueda_hash(tabla, objetivo):
    """
    Localiza una clave aplicando directamente la función hash para ir
    a la casilla correspondiente sin recorrer toda la estructura.
    """
    tamano = len(tabla)
    indice = objetivo % tamano
    cubeta = tabla[indice]

    print(f"\nBuscando código {objetivo}:")
    print(f"Paso 1: Calculando ubicación -> {objetivo} % {tamano} = casilla [{indice}]")
    print(f"Paso 2: Revisando únicamente la casilla [{indice}] -> {cubeta}")

    for pos_interna, valor in enumerate(cubeta):
        if valor == objetivo:
            print(f"  -> ¡Código encontrado en la casilla [{indice}], lugar #{pos_interna + 1}!")
            return indice

    print(f"  -> El código {objetivo} no se encuentra en la casilla [{indice}].")
    return -1


def solicitar_cantidad(mensaje, minimo=2):
    """Solicita y valida la cantidad de elementos a registrar."""
    while True:
        entrada = input(mensaje).strip()
        try:
            cantidad = int(entrada)
            if cantidad >= minimo:
                return cantidad
            print(f"Error: Debes ingresar un número entero mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Entrada no válida. Escribe únicamente un número entero.")


def capturar_enteros_positivos(etiqueta="número"):
    """Solicita una lista de números enteros mayores a 0."""
    cantidad = solicitar_cantidad(f"\n¿Cuántos {etiqueta}s deseas ingresar? (mínimo 2): ")
    datos = []
    for i in range(cantidad):
        while True:
            entrada = input(f"Ingresa el {etiqueta} #{i + 1}: ").strip()
            if "." in entrada or "," in entrada:
                print("Error: Este ejercicio NO acepta decimales. Ingresa solo números enteros.")
                continue
            try:
                valor = int(entrada)
                if valor > 0:
                    datos.append(valor)
                    break
                print("Error: El valor debe ser mayor a 0 (no se aceptan negativos ni cero).")
            except ValueError:
                print("Error: Entrada no válida. Ingresa únicamente números enteros.")
    return datos


def capturar_numeros_ordenados():
    """Solicita números positivos mayores a 0 verificando orden ascendente."""
    cantidad = solicitar_cantidad("\n¿Cuántos precios deseas registrar en el catálogo? (mínimo 2): ")
    datos = []
    for i in range(cantidad):
        while True:
            aviso = f" (debe ser >= {datos[-1]})" if datos else ""
            entrada = input(f"Ingresa el precio #{i + 1}{aviso}: ").strip()
            try:
                valor = float(entrada)
                if valor <= 0:
                    print("Error: El precio debe ser mayor a 0 (no se aceptan negativos ni cero).")
                    continue
                valor_limpio = int(valor) if valor.is_integer() else valor
                if datos and valor_limpio < datos[-1]:
                    print(f"Error: Para Búsqueda Binaria la lista debe estar ordenada (>= {datos[-1]}).")
                    continue
                datos.append(valor_limpio)
                break
            except ValueError:
                print("Error: Entrada no válida. Ingresa un valor numérico.")
    return datos


def solicitar_objetivo(solo_enteros=True):
    """Solicita el número que el usuario desea buscar."""
    while True:
        entrada = input("\nIngresa el valor que deseas buscar: ").strip()
        if solo_enteros:
            if "." in entrada or "," in entrada:
                print("Error: Debes ingresar un número entero positivo.")
                continue
            try:
                valor = int(entrada)
                if valor > 0:
                    return valor
                print("Error: Ingresa un número entero mayor a 0.")
            except ValueError:
                print("Error: Entrada no válida. Escribe un número entero.")
        else:
            try:
                valor = float(entrada)
                if valor > 0:
                    return int(valor) if valor.is_integer() else valor
                print("Error: Ingresa un número mayor a 0.")
            except ValueError:
                print("Error: Entrada no válida. Escribe un número.")


def mostrar_instrucciones(titulo, descripcion, permitidos, no_permitidos):
    """Muestra las reglas sobre qué datos puede y no puede ingresar el usuario."""
    print("\n" + "=" * 68)
    print(f" {titulo}")
    print("=" * 68)
    print(f"Contexto: {descripcion}")
    print("\nINSTRUCCIONES DE CAPTURA DE DATOS:")
    print(f"  [+] SÍ puedes ingresar: {permitidos}")
    print(f"  [-] NO puedes ingresar: {no_permitidos}")
    print("-" * 68)


def menu_principal():
    """Controla el menú interactivo hasta que el usuario decida salir."""
    while True:
        print("\n" + "#" * 68)
        print("       SISTEMA INTERACTIVO DE MÉTODOS DE BÚSQUEDA EN PYTHON")
        print("#" * 68)
        print("1. Ejercicio 1 - Búsqueda Secuencial (Folios de asistencia)")
        print("2. Ejercicio 2 - Búsqueda Binaria    (Catálogo de precios ordenado)")
        print("3. Ejercicio 3 - Búsqueda Hash       (Códigos de casilleros)")
        print("4. Salir del programa")
        print("#" * 68)

        opcion = input("Selecciona el ejercicio que deseas ejecutar (1-4): ").strip()

        if opcion == "1":
            mostrar_instrucciones(
                titulo="EJERCICIO 1: BÚSQUEDA SECUENCIAL - FOLIOS DE ASISTENCIA",
                descripcion="Busca un folio revisando la lista uno por uno desde el inicio.",
                permitidos="Números enteros positivos mayores a 0 en cualquier orden (ej. 1045, 892, 2310).",
                no_permitidos="Números negativos, el número 0, decimales, letras o símbolos."
            )
            folios = capturar_enteros_positivos("folio")
            while True:
                objetivo = solicitar_objetivo(solo_enteros=True)
                busqueda_secuencial(folios, objetivo)
                otra = input("\n¿Deseas buscar otro folio en esta misma lista? (s/n): ").strip().lower()
                if otra != "s":
                    break

        elif opcion == "2":
            mostrar_instrucciones(
                titulo="EJERCICIO 2: BÚSQUEDA BINARIA - CATÁLOGO DE PRECIOS ORDENADO",
                descripcion="Busca un precio partiendo la lista ordenada a la mitad en cada paso.",
                permitidos="Números enteros o decimales positivos (> 0) ingresados de menor a mayor.",
                no_permitidos="Números negativos, el 0, letras, símbolos o números menores al anterior."
            )
            precios = capturar_numeros_ordenados()
            while True:
                objetivo = solicitar_objetivo(solo_enteros=False)
                busqueda_binaria(precios, objetivo)
                otra = input("\n¿Deseas buscar otro precio en este catálogo? (s/n): ").strip().lower()
                if otra != "s":
                    break

        elif opcion == "3":
            mostrar_instrucciones(
                titulo="EJERCICIO 3: BÚSQUEDA HASH - CÓDIGOS DE CASILLEROS",
                descripcion="Asigna cada código a una casilla mediante residuo (%) para acceso directo.",
                permitidos="Números enteros positivos mayores a 0 en cualquier orden (ej. 105, 232, 418).",
                no_permitidos="Números negativos, el número 0, decimales, letras o espacios vacíos."
            )
            codigos = capturar_enteros_positivos("código")
            tabla = construir_tabla_hash(codigos)
            while True:
                objetivo = solicitar_objetivo(solo_enteros=True)
                busqueda_hash(tabla, objetivo)
                otra = input("\n¿Deseas buscar otro código en esta Tabla Hash? (s/n): ").strip().lower()
                if otra != "s":
                    break

        elif opcion == "4":
            print("\nPrograma finalizado por el usuario. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()