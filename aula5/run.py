import click

filename = "COMPRAS.txt"
todo_list=[]
@click.command()
def hello():
    click.echo("Hello",color=True)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("item")
def add(item):
    todo_list.append(item)
    with open(filename, 'w') as file:
        for item in todo_list:
            file.write(f"{item}\n")
    click.echo(f"Item added: {item}")
    # with open(filename, "a") as file:
    #     file.write(f"{product}\n")
    # click.echo(f"{product.upper()} added!")




if __name__ == "__main__":
    hello()
