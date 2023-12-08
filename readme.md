# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/albertojunior12/multistack-ediaristas-python.git`

#### Criar venv
`python -m venv .venv`

#### Acessar venv (ambiente virtual)
- Caso utilize MAC/Linux:
`source nome_do_ambiente_virtual/bin/activate` ou `. nome_do_ambiente_virtual/bin/activate`

- Caso utilize Windows:
`nome_do_ambiente_virtual\Scripts\Activate`

#### Instalar dependências
`pip install -r requirements.txt`


#### Alterar configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd',
    }
}
```

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`