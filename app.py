from flask import Flask, render_template, url_for
app=Flask(__name__) 

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/instalacion')
def instalacion():
    return render_template('instalacion.html')

@app.route('/arduino')
def arduino():
    return render_template('arduino.html')

@app.route('/github')
def github():
    return render_template('github.html')

@app.route('/estructura')
def estructura():
    return render_template('estructura.html')
if __name__=='__main__':
    app.run(debug=True)
    



