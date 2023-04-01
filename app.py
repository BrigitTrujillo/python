from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from producto import Producto

db = dbase.dbConnection()

app = Flask(__name__)

#routes del crud
@app.route('/')
def home():
    productos = db['productos']
    productosReceived = productos.find()
    return render_template('index.html', productos = productosReceived)
@app.route('/productos', methods=['POST'])
def addProducto():
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    marca = request.form['marca']
    
    if nombre and precio and marca:
       producto = Producto(nombre, precio, marca)
       productos.insert_one(producto.toDBCollection())
       Response = jsonify({
           'nombre': nombre,
            'precio': nombre,
            'marca': marca
           
       })
       return redirect(url_for('home'))
    else:
       return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado' + request.url,
        'status' : '404 Not Found'
    }
    response = jsonify(message)
    response.status_code=404
    return response


@app.route('/delete/<string:producto_nombre>')
def delete(producto_nombre):
    productos = db['productos']
    productos.delete_one({'name': producto_nombre})
    return redirect(url_for('home'))
    
#metodo put modificar

@app.route('/edit/<string:producto_nombre>', methods=['POST'])
def edit(producto_nombre):
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    marca = request.form['marca']
    
    if nombre and precio and marca:
        productos.update_one({'nombre': producto_nombre},{'$set':{'nombre': nombre, 'precio': precio,'marca': marca}})
        response  = jsonify({'massage':'Producto' + producto_nombre + 'actualizado exitosamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado' + request.url,
        'status' : '404 Not Found'
    }
    response = jsonify(message)
    response.status_code=404
    return response
        
    
           

if __name__ == '__main__':
    app.run(debug=True, port=4000)




