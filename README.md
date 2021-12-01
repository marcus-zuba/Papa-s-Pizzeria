# Papa's Pizzeria

Primeiro Trabalho Prático da Disciplina de Laboratório de Engenharia de Software, ministrada pelo professor Eduardo Campos, do Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG).

## Integrantes do Grupo 

- DANILO GONÇALVES CUSTÓDIO
    - matrícula: 20193016039
- EDUARDO MARTINS GOMES PEREIRA
    - matrícula: 20193001546
- FELIPE MARTINS LEMOS DE MORAIS
    - matrícula: 20193001045
- MARCUS VINICIUS DURÃES ZUBA FERNANDES
    - matrícula: 20193001822

## Configuração do projeto

Após clonar o repositório, execute os seguintes passos na raiz do projeto:

- Crie um ambiente virtual para o projeto
    - `mkdir env`
    - `pip install virtualenv`
    - `virtualenv env/papaspizzeria`

- Ative o ambiente virtual (faça isso sempre antes de executar o projeto)
    - `source env/papaspizzeria/bin/activate`
    - Obs: caso queira desativar o ambiente virtual, basta executar `deactivate`

- Instale os pacotes necessários no ambiente virtual 
    - `pip install -r requirements.txt`

- Execute as migrations para que o seu banco de dados local seja criado (faça isso sempre para manter o seu banco atualizado)
    - `python manage.py migrate`

- Popule o banco de dados com os dados do json
    - `python manage.py loaddata dados.json`

- Execute o server
    - `python manage.py runserver`

- O projeto será hosteado e poderá ser acessado em [localhost:8000](http://localhost:8000)

- Caso queira criar um usuário de administrador, basta executar:
    - `python manage.py createsuperuser`
    - Com esse usuário, você pode acessar [localhost:8000/admin](http://localhost:8000) 
    e controlar diversos aspectos do projeto!  
