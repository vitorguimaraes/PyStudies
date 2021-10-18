import functools 

# Um decorator é uma forma prática e reusável de adicionar funcionalidades à 
# funções/métodos/classes, sem precisar alterar o código delas.

# Retornar um texto em uppercase:

def uppercase(func):
    # Esse decorator faz uma cópia dos atributos da função 
    # deixando a função original intacta
    @functools.wraps(func) 
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper

@uppercase
def greet():
    return "Hello!"    

print(greet())

##############################################

# Aplicar negrito e ênfase em um texto html:
import functools 

def strong(func):
    # Esse decorator faz uma cópia os atributos da função 
    # deixando a função original intacta
    @functools.wraps(func) 
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper

def emphasis(func):
    @functools.wraps(func) 
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

# Os decorators são aplicados de baixo pra cima
@strong
@emphasis
def greet():
    return "Hello!"

print(greet())

##############################################


# Decorator
def requer_autenticacao(func):
    @wraps(func)
    def funcao_decorada(*args, **kwargs):
        # Verifica session['logado']
        if ("logado" not in session):
            # Retorna para a URL de login caso o usuário não esteja logado
            return redirect(url_for('index'))

        return func(*args, **kwargs)
    return funcao_decorada

@app.route('/admin/dashboard')
@requer_autenticacao
def admin_dashboard():    
    # Renderiza o template dashboard.html
    return render_template('admin/dashboard.html')


# https://pythonacademy.com.br/blog/domine-decorators-em-python
# https://dbader.org/blog/python-decorators