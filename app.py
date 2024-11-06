# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

# Struktur folder:
# /static
#   /css
#     style.css
#   /img
#     logo.png
# /templates
#   base.html
#   index.html
#   about.html
#   products.html
#   contact.html