from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Página de inicio
@app.route('/', methods=['GET'])
def index():
    products = [
        {"name": "Taladro Percutor Bosch", "image": "taladro.jpg", "price": 89090.99, "description": "Taladro percutor de alta potencia Bosch."},
        {"name": "Cemento Portland", "image": "cemento.jpg", "price": 1499.99, "description": "Cemento Portland para construcción."},
        {"name": "Casco de Seguridad", "image": "casco.jpg", "price": 2499.99, "description": "Casco resistente para seguridad industrial."},
        {"name": "Sierra", "image": "sierra.jpg", "price": 45000.00, "description": "Sierra de alta calidad, ideal para cortar madera y otros materiales."},
        {"name": "Martillo", "image": "martillo.jpg", "price": 20000.00, "description": "Martillo robusto, ideal para trabajos de construcción y reparaciones."},
        {"name": "Guantes de Seguridad", "image": "guante.jpg", "price": 8000.00, "description": "Guantes resistentes, ideales para trabajos de protección en construcción."}
    ]

    search_query = request.args.get('search', '').lower()

    if search_query:
        products = [product for product in products if search_query in product["name"].lower()]

    no_results_message = "No se encontraron productos que coincidan con tu búsqueda." if search_query and not products else None

    return render_template('index.html', products=products, no_results_message=no_results_message)

# Página de detalles del producto
@app.route('/product/<product_name>')
def product_detail(product_name):
    products = {
        "Casco de Seguridad": {"name": "Casco de Seguridad", "price": 8990, "image": "casco.jpg", "description": "Casco industrial para protección."},
        "Taladro Percutor Bosch": {"name": "Taladro Percutor Bosch", "price": 89090.99, "image": "taladro.jpg", "description": "Taladro percutor profesional Bosch."},
        "Cemento Portland": {"name": "Cemento Portland", "price": 1499.99, "image": "cemento.jpg", "description": "Cemento Portland resistente."},
        "Sierra": {"name": "Sierra", "image": "sierra.jpg", "price": 45000.00, "description": "Sierra de alta calidad, ideal para cortar madera y otros materiales."},
        "Martillo": {"name": "Martillo", "image": "martillo.jpg", "price": 20000.00, "description": "Martillo robusto, ideal para trabajos de construcción y reparaciones."},
        "Guantes de Seguridad": {"name": "Guantes de Seguridad", "image": "guante.jpg", "price": 8000.00, "description": "Guantes resistentes, ideales para trabajos de protección en construcción."}
    }

    product = products.get(product_name)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Producto no encontrado", 404

# Página de contacto
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Página de inicio de sesión
@app.route('/login')
def login():
    return render_template('login.html')

# Página del carrito
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

# Ruta para agregar productos al carrito
@app.route('/add_to_cart/<product_name>')
def add_to_cart(product_name):
    products = [
        {"name": "Taladro Percutor Bosch", "image": "taladro.jpg", "price": 89090.99, "description": "Taladro percutor de alta potencia Bosch."},
        {"name": "Cemento Portland", "image": "cemento.jpg", "price": 1499.99, "description": "Cemento Portland para construcción."},
        {"name": "Casco de Seguridad", "image": "casco.jpg", "price": 2499.99, "description": "Casco resistente para seguridad industrial."},
        {"name": "Sierra", "image": "sierra.jpg", "price": 45000.00, "description": "Sierra de alta calidad, ideal para cortar madera y otros materiales."},
        {"name": "Martillo", "image": "martillo.jpg", "price": 20000.00, "description": "Martillo robusto, ideal para trabajos de construcción y reparaciones."},
        {"name": "Guantes de Seguridad", "image": "guante.jpg", "price": 8000.00, "description": "Guantes resistentes, ideales para trabajos de protección en construcción."}
    ]

    selected_product = next((p for p in products if p["name"] == product_name), None)

    if selected_product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(selected_product)
        session.modified = True

    return redirect(url_for('cart'))

if __name__ == "__main__":
    app.run(debug=True)
