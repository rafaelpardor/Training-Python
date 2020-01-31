import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycles"""
    pass


@clients.command()
@click.option('-n', '--name',   type=str, prompt=True, help = 'The client name')
@click.option('-c', '--company', type=str, prompt=True, help = 'The client company')
@click.option('-e', '--email', type=str, prompt=True, help = 'The client email')
@click.option('-p', '--position', type=str, prompt=True, help = 'The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    click.echo('ID  | NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*'*100)
    
    for client in client_list:
        click.echo('{uid}    |   {name}  |   {company}   |   {email} |   {position}'.format(
            uid         =   client['uid'],
            name        =   client['name'],
            company     =   client['company'],
            email       =   client['email'],
            position    =   client['position']
        ))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client update')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client
    

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    pass

all = clients