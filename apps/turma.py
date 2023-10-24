import typer
from sqlmodel import Session
from data.database import engine


app = typer.Typer()
