import jinja2
from src.cvc_settings import CVC

def generate(filepath: str, settings: CVC = CVC):
    ENV = jinja2.Environment()
    template = ENV.get_template('template.html')
    
    with open(filepath, 'wb') as f:
        f.write(template.render( data = settings ).encode())
    