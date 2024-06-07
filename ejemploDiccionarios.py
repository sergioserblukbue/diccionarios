personas=[]
datosPersona = {}

def agregarpersona(dic):
    hijos=[]
    nombre=input("ingrese el nombre: ")
    apellido= input("ingrese el apellido: ")
    edad=int(input("ingrese la edad: "))
    ciudad=input("ingrese la ciudad: ")
    jubilado=input("es jubilado? ")
    resp=input("agregar un hijo? s/n ")
    while resp.lower() == "s":
       hijo=input("ingrese el nombre del hijo/a ")
       hijos.append(hijo)
       resp=input("agregar otro hijo? s/n ")
    dic={
       "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "ciudad": ciudad,
        "jubilado": jubilado,
        "hijos": hijos
        }
    personas.append(dic)
    return
def listar(lista):
    print("listado de personas")
    for elemento in lista:
        print("-"*30)
        for c, v in elemento.items() :
            if c=="hijos":
                print("hijos: ")
                for nom in v:
                    print(f" {nom}  ")
            else:
                print(f"{c}={v}")
# menu principal
op=0
while op!=3:
    print("1 para agregar persona")
    print("2 para listar")
    print("3 para salir")
    op=int(input("ingrese una opcion"))
    match op:
        case 1:
            agregarpersona(datosPersona)
            input("presione enter para salir")
        case 2:
            listar(personas)
            input("presione enter para salir")

print("gracias por cargar la nomina")
 

