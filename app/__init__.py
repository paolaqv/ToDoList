from flask import Flask
from pathlib import Path

template_dir = Path('C:/Users/paola qv/Documents/ToDoList/templates')
app = Flask(__name__, template_folder=template_dir)

from app import routes  # Esto debe ir al final


