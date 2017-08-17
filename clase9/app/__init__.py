from flask import Flask, redirect, url_for, request

app =Flask(__name__)

@app.route('/exito/<nombre>')
def exito(nombre):
    return 'Bienvenido, %s' % nombre

@app.route('/login',methods=['Post','GET'])
def login():
    if request.method =='POST':
        usuario = request.form['nm']
        return redirect(url_for('exito',nombre=usuario))
    else:
        usuario = request.args.get('nm')
        return redirect(url_for('exito', nombre=usuario))

if __name__ =='__main__':
    app.run(port=8000)


