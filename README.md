# Papa's Pizzeria

## Configuração do projeto

Após clonar o repositório, execute na raiz do projeto:

- Crie um ambiente virtual para o projeto
`mkdir env`
`virtualenv env/papaspizzeria`

- Ative o ambiente virtual (faça isso sempre antes de executar o projeto)
`source env/myshop/bin/activate`

- Instale o Django e o Livesync no ambiente virtual 
`pip install Django==2.1.5`
`pip install django-livesync`

- Execute as migrations para que o seu banco de dados local seja criado (faça isso sempre para manter o seu banco atualizado)
`python manage.py migrate`

- Popule o banco de dados com os produtos
`python manage.py loaddata dados_produto.json`

- Execute o server 
`python manage.py runserver`