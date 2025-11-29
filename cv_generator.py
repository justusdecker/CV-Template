import jinja2
from src.cvc_settings import CVC

def generate(filepath: str, settings: CVC = CVC):
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('./src/template/'))
    template = ENV.get_template('index.html')
    
    with open(f'./src/static/styles.css', 'rb') as f:
        CSS = f.read().decode()
    
    with open(filepath, 'wb') as f:
        f.write(template.render( data = settings, enumerate = enumerate, css = CSS ).encode())


generate('test.html')