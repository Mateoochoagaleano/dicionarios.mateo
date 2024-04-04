mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario,cod_persona,nombre,edad,contacto,sexo,extracto,correo):
    if cod_persona == '' or nombre == '' or edad == '' or contacto == '' or sexo == '' or extracto == '' or correo =='':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[cod_persona] = {'nombre': nombre, 'edad': edad, 'contacto': contacto, 'sexo': sexo, 'extracto': extracto, 'correo': correo}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')   
        
def fnt_selector(op):
    if op == '1':
        os.system('cls')
        nombre = input('Nombre:  ')
        edad = input('Edad:  ')
        contacto = input('Telefono:  ')
        sexo = input('Sexo [M/F]:  ')
        extracto = input('Extracto:  ')
        correo = input('Correo: ')
        fnt_agregar(mi_diccionario, nombre, edad, contacto,  sexo, extracto, correo)
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
        fnt_agregar()
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False