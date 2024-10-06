
# crear un diccionario

tarea = {

    "id": "",
    "titulo": "",
    "calificacion": 0,
    "categoria": ""
}

# crear una lista para almacenar las tareas

tareas = []


def agregar_tarea():
    tarea = {
        "id": input("Ingrese el ID de la tarea: "),
        "titulo": input("Ingrese el título de la tarea: "),
        "calificacion": int(input("Ingrese la calificación de la tarea (0-5): ")),
        "categoria": input("Ingrese la categoría de la tarea (quiz, parcial o trabajo): ")
    }
    tareas.append(tarea)

def clasificar_tareas():
    tareas_quiz = [tarea for tarea in tareas if tarea["categoria"] == "quiz"]
    tareas_parcial = [tarea for tarea in tareas if tarea["categoria"] == "parcial"]
    tareas_trabajo = [tarea for tarea in tareas if tarea["categoria"] == "trabajo"]
    return tareas_quiz, tareas_parcial, tareas_trabajo

def selec_categoria(tareas):  # La función recibe la lista de tareas
    for tarea in tareas:  # Iteramos sobre cada una de las tareas
        if tarea["categoria"] == "1":
            tarea["categoria"] = "quiz"
        elif tarea["categoria"] == "2":
            tarea["categoria"] = "parcial"
        elif tarea["categoria"] == "3":
            tarea["categoria"] = "trabajo"

def mostrar_tareas(tareas):
    for tarea in tareas:
        print(f"ID: {tarea['id']}, Título: {tarea['titulo']}, Calificación: {tarea['calificacion']}, Categoría: {tarea['categoria']}")
            
                

def imprimir_tareas():
    tareas_quiz, tareas_parcial, tareas_trabajo = clasificar_tareas()
    print("Tareas de quiz:")
    for tarea in tareas_quiz:
        print(tarea)
    print("Tareas de parcial:")
    for tarea in tareas_parcial:
        print(tarea)
    print("Tareas de trabajo:")
    for tarea in tareas_trabajo:
        print(tarea)

        
while True:
    agregar_tarea()
    continuar = input("¿Desea agregar otra tarea? (s/n): ").lower()
    if continuar != 's':  # Si el usuario no ingresa 's', se rompe el ciclo
        break

imprimir_tareas()
