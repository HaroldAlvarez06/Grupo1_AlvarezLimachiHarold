def ingresar_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()

        if nombre:
            return nombre

        print("ERROR: El nombre no puede estar vacío.")


def ingresar_calificacion(numero):
    while True:
        try:
            calificacion = float(
                input(f"Ingrese la calificación {numero} (0-100): ")
            )

            if 0 <= calificacion <= 100:
                return calificacion

            print("ERROR: La calificación debe estar entre 0 y 100.")

        except ValueError:
            print("ERROR: Debe ingresar un valor numérico.")


def registrar_estudiante():
    nombre = ingresar_nombre()

    calificacion1 = ingresar_calificacion(1)
    calificacion2 = ingresar_calificacion(2)
    calificacion3 = ingresar_calificacion(3)

    promedio = (calificacion1 + calificacion2 + calificacion3) / 3

    if promedio >= 60:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return {
        "nombre": nombre,
        "calificaciones": [
            calificacion1,
            calificacion2,
            calificacion3
        ],
        "promedio": promedio,
        "estado": estado
    }


def mostrar_estudiante(estudiante):
    print("\n--- RESULTADOS ---")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Calificación 1: {estudiante['calificaciones'][0]}")
    print(f"Calificación 2: {estudiante['calificaciones'][1]}")
    print(f"Calificación 3: {estudiante['calificaciones'][2]}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
    print(f"Estado: {estudiante['estado']}")


def main():
    estudiantes = []

    print("=== SISTEMA DE REGISTRO DE CALIFICACIONES ===")

    while True:
        estudiante = registrar_estudiante()
        estudiantes.append(estudiante)

        mostrar_estudiante(estudiante)

        continuar = input(
            "\n¿Desea registrar otro estudiante? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break

    print("\n=== REGISTRO FINALIZADO ===")
    print(f"Total de estudiantes registrados: {len(estudiantes)}")


if __name__ == "__main__":
    main()