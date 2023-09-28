import csv


archivo_pendientes = "pendientes.csv"
archivo_completadas = "completadas.csv"


def cargar_tareas(archivo):
    try:
        with open(archivo, mode="r", newline="") as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []


def guardar_tareas(archivo, tareas):
    with open(archivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tareas)


def agregar_tarea(titulo, descripcion, tareas):
    tareas.append([titulo, descripcion])


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. Título: {tarea[0]}")
            print(f"   Descripción: {tarea[1]}")
            print()


def marcar_completada(indice, tareas_pendientes, tareas_completadas):
    if 1 <= indice <= len(tareas_pendientes):
        tarea_completada = tareas_pendientes.pop(indice - 1)
        tareas_completadas.append(tarea_completada)
        guardar_tareas(archivo_pendientes, tareas_pendientes)
        guardar_tareas(archivo_completadas, tareas_completadas)
        print(f"Tarea '{tarea_completada[0]}' marcada como completada.")
    else:
        print("Índice de tarea inválido.")


def main():
    
    tareas_pendientes = cargar_tareas(archivo_pendientes)
    tareas_completadas = cargar_tareas(archivo_completadas)

    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Agregar una tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(titulo, descripcion, tareas_pendientes)
            guardar_tareas(archivo_pendientes, tareas_pendientes)
            print("Tarea agregada con éxito.")
        elif opcion == "2":
            print("\n--- Tareas Pendientes ---")
            listar_tareas(tareas_pendientes)
        elif opcion == "3":
            print("\n--- Tareas Pendientes ---")
            listar_tareas(tareas_pendientes)
            indice = input("Seleccione el número de la tarea a marcar como completada (0 para cancelar): ")
            if indice == "0":
                continue
            try:
                indice = int(indice)
                marcar_completada(indice, tareas_pendientes, tareas_completadas)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

