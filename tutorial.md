# Como rodar esse negócio?

---

### CLone o repositório
 - Dentro de uma pasta de sua escolha, dê git clone na url do projeto

### Criar ambiente virtual
 - Digite no prompt: python -m venv venv
 - Aguarde voltar a aparecer a opção de digitar a frente do nome da pasta
 - Digite venv\Scripts\activate para entrar no ambiente virtual

### Instalação do Framework
 - Dentro do ambiente virtual e ainda no prompt, digite pip install fastapi uvicorn
 - Aguarde a instalação.
 - Agora digite pip install sqlalchemy
 - Será baixado o ORM do python.

### Entre no projeto
 - Dentro da pasta do repositório clonado, acesse com o vs code ou dentro do terminal digite code .

### Como rodar o projeto
 - Após as instalações, dentro do terminal, na pasta do projeto digite uvicorn main:app --reload
 - O banco de dados será criado na primeira execução e você poderá acessar a api via navegador ou Postman/Insomnia.
