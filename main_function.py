import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]

# Crear Clientes
def create_client(client):
    global clients # Para tomar variables globales

    if client not in clients:
        clients.append(client)
    else:
        print("Client already is in the client's list")


# Mostrar a los Clientes
def read_clients():
    for i, client in enumerate(clients):
            print(f"{i} | {client['name']} | {client['company']} | {client['email']} | {client['position']}")


# Actualizar clientes
def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


# Borrar clientes
def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


# Buscar Cliente
def search_client(client_name):
    
    for client in clients:
        if client['name'] != client_name:
            continue  # No ejecutar nada mas en el loop e ir a la siguiente iteración
        else:
            return True


def _get_client_field(field_name, message='What is the client {}? '):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client



# Función de Menú
def _print_welcome():
    print()
    print('*' * 50)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print()
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print()


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper() # Lo vuelve mayúscula

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        read_clients()

    elif command == 'R':
        read_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        read_clients()

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        read_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
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

