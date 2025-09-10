from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        return f'Nome: {nome} | senha: {senha}'

    return render_template('login.html')

@app.route('/cadastrar',methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        return f'Nome: {nome} | Email: {email} | Senha: {senha}'
    return render_template('cadastrar.html')




if __name__=='__main__':
    app.run(debug=True)
