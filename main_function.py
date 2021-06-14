import sys


clients = 'pablo,ricardo,'

# Crear Clientes
def create_client(client_name):
    global clients # Para tomar variables globales

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else: 
        print("Client already is in the client's list")


# Mostrar a los Clientes
def read_clients():
    global clients
    print(clients)


# Actualizar clientes
def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print('Client is not in clients list')


# Borrar clientes
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')


# Buscar Cliente
def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue  # No ejecutar nada mas en el loop e ir a la siguiente iteración
        else:
            return True



# Función auxiliar para añadir coma despues de cada cliente
def  _add_comma():
    global clients
    clients += ','


# Función de Menú
def _print_welcome():
    print()
    print('*' * 50)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print()
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print()


def _get_client_name():
    client_name = None  # Variable vacía

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break        # si el nombre del cliente es 'exit' entonces salir del programa

    if not client_name:
        sys.exit()  #  modulo para salir del programa
    
    return client_name

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper() # Lo vuelve mayúscula

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        read_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        read_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        read_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('Invalid command')




def funcion():
    '''Documentar función'''
    pass

