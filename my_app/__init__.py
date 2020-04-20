from flask import Flask
from my_app.product.views import product


app = Flask(__name__)
#import views
app.register_blueprint(product)
