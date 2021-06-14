
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
def list_clients():
    global clients
    print(clients)


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
    print('[D]elete client')
    print()

if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')