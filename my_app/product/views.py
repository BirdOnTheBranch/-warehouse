#from my_app import app
from flask import Blueprint

product = Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
   return "Hola mundo"
