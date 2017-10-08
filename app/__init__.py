from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config') #Carrega as configurações do banco


db = SQLAlchemy(app) #Banco de dados

migrate = Migrate(app, db)

manager = Manager(app) #Gerenciador do app
manager.add_command('db', MigrateCommand)

lm = LoginManager() #Controlador do login 
lm.init_app(app)
from app.controllers import default
from app.models import tables

