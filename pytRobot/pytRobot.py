import click

@click.group()
def main():
    pass

@main.group()
def console():
    pass

@console.command()
def capture():
    print('img')

@console.command()
def turn():
    print('turn')

@console.command()
def forward():
    print('forward')

@main.command()
def web():
    print('hello www!!!!')
