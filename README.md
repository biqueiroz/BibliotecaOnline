# BibliotecaOnline
Esse é um projeto desenvolvido simulando uma biblioteca online, baseado em Python e Django.
<br><br>
O projeto tem como objetivo ser avaliado para a **tarefa dissertativa da disciplina de Laboratório de Desenvolvimento de Software**, e foi realizado em um curso período de tempo e com pouco conhecimento em programação, mantendo-se ao básico.
<br><br>
Tendo em vista todas as limitações aqui expostas, seguem orientações sobre a execução do projeto:
<br><br>
- Para realização desse projeto foi utilizado o framework Django, baseado em Python. Dessa forma, para rodar o projeto é preciso ter o Python instalado em sua máquina, assim como Django.<br>
- Não foi configurado um banco de dados fixo, mas aproveitada a facilidade de criação de banco de dados próprio do Django, que pode ser verificado e acessado pelo arquivo db.sqlite3;<br>
- Para rodar o projeto, após clonado o repositório, será preciso rodar as seguintes comandos:<br><br>
  **- Para criação do ambiente virtual do projeto:**<br>
    *$ python3 -m venv venv <br><br>*
  **- Para instalação do framework:**<br>
    *$ python3 install django <br><br>*
  **- Para instalação da biblioteca:**<br>
    *$ python3 install pillow <br><br>*
  **- Para realizar a migração das alterações para o banco de dados:**<br>
    *$ python3 manage.py makemigrations <br><br>*
  **- Para efetivar as migrações:**<br>
    *$ python3 manage.py migrate <br><br>*
  **- Para, finalmente, rodar o projeto e visualizá-lo no seu local:**<br>
    *$ python3 manage.py runserver*
<br><br>

Após essas orientações, você conseguirá acessar o projeto e realizar ações como: criar novo usuário, realizar login de usuário, cadastrar categorias, cadastrar livros, realizar empréstimos, etc.

*O projeto está disponível na branch "master".*
<br><br><br><br>

*Esse projeto foi baseado e desenvolvido com as aulas e orientações do canal Pythonando: https://www.youtube.com/@pythonando*
