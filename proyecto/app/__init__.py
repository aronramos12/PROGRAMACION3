from flask import Flask,request
from flask import render_template

app = Flask(__name__)

'''Esta ruta es el inicio del banco'''
@app.route('/')
def index():
   return render_template('home.html')

'''Esta ruta es para logearse en el banco'''
@app.route('/login')
def login():
    return render_template('login.html')


'''Esta ruta es la que te direcciona a la seccion de opciones del banco'''
@app.route('/service',methods=['POST'])
def Service():
    ''':var cuenta1 almacena el nombre de la cuenta de los usuarios'''
    cuenta1 = ['2900101935', '4729444810']
    ''':var: password1 almacena las contraseñas de los usuarios'''
    password1 = ['12345', '12345']
    ''':param cuenta obtiene el valor del html login'''
    cuenta=request.form.get('cuenta')
    ''':param password obtiene la contraseña del html login'''
    password=request.form.get('password')
    ''' se validan que los datos sean verdaderos'''
    if ((cuenta == cuenta1[0]) and (password == password1[0]) or (cuenta == cuenta1[1]) and (password == password1[1])):
        return render_template('Service.html')
    else:
        ''' :var vec sirve por si el usuario inserta una contraseña incorrecta'''
        vec = 1
        '''retorna el html login'''
        return render_template('login.html', vec=vec)

    return render_template("Service.html")

'''la ruta withdraw es para el retiro'''
@app.route('/withdraw',methods=['POST'])
def withdraw():
    return render_template("withdraw.html")


'''la ruta deposit es para depositar '''
@app.route('/deposit',methods=['POST'])
def deposit():
    '''este return devuelve al html deposit'''
    return render_template("deposit.html")

''' la lista plata sirve para guardar los depositos del usuario'''
plata = []
''' la ruta vista es para ver el deposito ingresado'''
@app.route('/vista',methods=['POST'])
def vista():
    ''':var deposito es la que obtiene el dato de los depositos de los usuarios'''
    deposito = float(request.form.get('deposito'))
    ''' este for esta guardando la cantidad que se deposita dentro de una lista'''
    for n in range(1):
        plata.append(deposito)
    '''var suma es donde se suma los valores dentro de la lista de plata'''
    suma=0
    for n in plata:
        suma+=n
        print(suma)
    return render_template("vista.html", dep=deposito,plata=plata,suma=suma)
'''var cantidad es el dinero fictioso que ya tiene depositado cada usuario '''
cantidad = 1000

''' esta ruta es para imprimir los resultados de las transacciones '''
@app.route('/vista1',methods=['POST'])
def vista1():
    '''var retirar resive el dato del html withdraw'''
    retirar = float(request.form.get('retirar'))
    if (retirar < 0):
        resultado = 'no tiene fondos'
        return render_template("vista1.html", ret=resultado)
    elif(retirar > 1000):
        resultado = 'no tiene la cantidad suficiente para retirar'
        return render_template('vista1.html',ret=resultado)
    else:
        '''var resultado sirve para el total de la resta de la transacciones que se han efectuado'''
        resultado = cantidad - retirar
        return render_template('vista1.html',ret=resultado,retirar=retirar)

if __name__=='__main__':
    app.run()