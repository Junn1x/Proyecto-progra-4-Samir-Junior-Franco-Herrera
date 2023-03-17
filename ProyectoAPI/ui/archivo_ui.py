from api import archivo_api as api
def pedir_departamento():
    departamento = input("Ingrese un departamento = ")
    return departamento.upper()

def pedir_municipio():
    municipio = input("ingrese un municipio = ")
    return municipio.upper()

def pedir_cultivo():
    cultivo = input("ingrese un cultivo = ")
    cultivo = cultivo.lower()
    return cultivo.capitalize()

def pedir_limite():
    limite = input("Ingrese limite de registros = ")
    return limite

def menu(opcion):
    while opcion != "3":
        print("\n\nDatos de cultivos\n1.Ingresar datos\n2.Mostrar datos\n3.Salir")
        print(opcion)
        opcion = input("ingrese una opcion:")
        if opcion == "1":
            departamento=pedir_departamento()
            municipio=pedir_municipio()
            cultivo=pedir_cultivo()
            limite=pedir_limite()
        if opcion == "2":
            api.tomarDatos(limite,departamento,municipio,cultivo)