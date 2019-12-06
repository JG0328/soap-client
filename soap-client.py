from zeep import Client

client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

while True:
    print('1 - Listar Estudiantes')
    print('2 - Consultar una asignatura')
    print('3 - Consultar un profesor')
    print('4 - Salir')
    op = int(input('\nElija la opcion que desea: '))

    if(op == 1):
        list = client.service.getAllEstudiante()

        for std in list:
            print("Matricula: {0}. Nombre: {1}.".format(
                std['matricula'], std['nombre']))
    elif(op == 2):
        asig = input("\nCodigo de la Asignatura: ")
        print(client.service.getAsignatura(asig))

    elif(op == 3):
        prof = input("\nCodigo del Profesor: ")
        print(client.service.getProfesor(prof))

    elif(op == 4):
        break
