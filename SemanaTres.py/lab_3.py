#---------------
#Person

#dni: int
#name: str
#lasname: int
#role: int
#---------------

from faker import faker
import random

fake = faker()
people_list =[]

def generate_people(num_people: int):

    for i in range(num_people):
        person ={
            "dni": i + 1,
            "name": fake.first.name(),
            "lasname":fake.las_name(),
            "role":ramdom.randint(1, 3)
        }
        people_list.append(person)

        return people_list

def select_role():
    for person in people_list:
        if(person["role"] == 1):
            person["role"] = " Administrativo"
        elif(person["role"]==2):
                 person["role"] == "profesor"
        elif(person["role"] ==3):
            person["role"]== "SEguridad"         
        else:
                 person["role"]= "Estudiante"


def  match_role():
    for person in people_list:                  # se puede de cualquier forma si las comparaciones son mayores que tres match_case 
        match person["role"]:
            case "Administrativo":
                person["role"] = 1
            case "profesor":
                person["role"] = 2
            case "estudiante":
                person["role"] = 3
                         

    


def print_people():
    for persona in people_list:
        print (persona)    



    number = int(input("Por favor ingrese la cantidad de usuarios:\n"))
    generate_people(number) 
    select_role()   
    print_people()
    match_person()