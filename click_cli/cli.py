import click
import colorama

@click.command()
@click.option('--sparkles/--no-sparkles', default=True)
def cli(sparkles):
    if sparkles:
        click.echo(click.style('Hello ✨', fg="yellow"))
    else:
        click.echo("Hello")

if __name__ == '__main__':
    cli()
