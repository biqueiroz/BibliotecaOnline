# BibliotecaOnline
Esse é um projeto desenvolvido simulando uma biblioteca online, baseado em Python e Django.

O projeto tem como objetivo ser avaliado para a tarefa dissertativa da disciplina de Laboratório de Desenvolvimento de Software, e foi realizado em um curso período de tempo, mantendo-se ao básico.

Tendo em vista todas as limitações aqui expostas, seguem orientações sobre a execução do projeto:

-> Para realização desse projeto foi utilizado o framework Django, baseado em Python. Dessa forma, para rodar o projeto é preciso ter o Python instalado em sua máquina, assim como Django.
-> Não foi configurado um banco de dados fixo, mas aproveitada a facilidade de criação de banco de dados próprio do Django, que pode ser verificado e acessado pelo arquivo db.sqlite3;
-> Para rodar o projeto, após clonado o repositório, será preciso rodar as seguintes comandos:
  .Para criação do ambiente virtual do projeto:
    $ python3 -m venv venv 
  .Para instalação do framework:
    $ python3 install django
  .Para instalação da biblioteca:
    $ python3 install pillow
  .Para realizar a migração das alterações para o banco de dados:
    $ python3 manage.py makemigrations
  .Para efetivar as migrações:
    $ python3 manage.py migrate
  .Para, finalmente, rodar o projeto e visualizá-lo no seu local:
    $ python3 manage.py runserver

Após essas orientações, você conseguirá acessar o projeto e realizar ações como: criar novo usuário, realizar login de usuário, cadastrar categorias, cadastrar livros, realizar empréstimos, etc.


**Esse projeto foi baseado e desenvolvido com as aulas e orientações do canal Pythonando: https://www.youtube.com/@pythonando
