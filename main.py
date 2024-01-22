from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1ª página do site
# route -> É o link da página. É o caminho que vem depois do domínio, o nome depois da barra.
# função -> É o que a pessoa quer exibir naquela página.
#template

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)

    # servidor do heroku



