from app import app
from bottle import request, template, static_file

# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@app.route('/') # @get('/')
def login():
	return template('login')
	
@app.route('/Cadastro') # @get('/Cadastro')
def Cadastro():
	return template('Cadastro')

@app.route('/Cadastro', method='POST') # @post('/')
def acao_Cadastro():
	username = request.forms.get('username')
	password = request.forms.get('password')
	insert_user(username,password)
	return template('verificacao_Cadastro', nome=username)
	
@app.route('/', method='POST') # @post('/')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso=True, nome=username)

@app.error(404)
def error404(error):
	return template('pagina404')