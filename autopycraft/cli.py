
import click

from autopycraft.setup_scripts import setup_flask
from autopycraft.setup_scripts import setup_django
from autopycraft.setup_scripts import setup_fastapi
from autopycraft.setup_scripts import setup_pygame

@click()
def cli():
    """PyCraft: Python Project Automation Tool"""
    pass


# Command to set up a Flask project
@click.command()
@click.argument("project_name")
def setup_flask(project_name):
    setup_flask(project_name)


# Commad to setup a Django project
@click.command()
@click.argument("project_name")
def setup_django(project_name):
    setup_django(project_name)


# Command to setup a FastAPI project
@click.command()
@click.argument("project_name")
def setup_fastapi(project_name):
    setup_fastapi(project_name)
    

# Command to setup a Pygame project
@click.command()
@click.argument("project_name") 
def setup_pygame(project_name):
    setup_pygame(project_name)