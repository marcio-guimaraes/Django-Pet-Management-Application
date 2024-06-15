# Django Pet Management Application

Este é um projeto Django para gerenciar animais de estimação atrávés de um CRUD.

## Funcionalidades

- **Listar Pets:** Exibe uma lista de todos os pets cadastrados.
- **Cadastrar Pets:** Permite adicionar novos pets ao sistema.
- **Editar Pets:** Permite atualizar as informações dos pets cadastrados.
- **Deletar Pets:** Permite remover registros de pets.

## Estrutura do Projeto

### Views

- **index:** Renderiza a página inicial.
- **bichos:** Exibe todos os pets cadastrados.
- **cad_pets:** Renderiza o formulário para cadastro de novos pets.
- **save_pets:** Salva um novo pet no banco de dados.
- **update:** Atualiza as informações de um pet existente.
- **deletar_animal:** Deleta um pet do banco de dados.

### Models

- **Bicho:** Modelo representando um animal de estimação com os campos:
  - `nome_dono`
  - `telefone`
  - `nome_animal`
  - `raca`
  - `caracteristicas`
  - `data`

### URLs

Mapeamento das URLs para as views correspondentes:
- `/` - Página inicial
- `/bichos` - Lista de pets
- `/pets/new` - Formulário para cadastro de novos pets
- `/pets/save` - Salvar novo pet
- `/pets/update/<int:pk>` - Atualizar informações de um pet
- `/delete/<int:pk>` - Deletar um pet

### Templates

- **index.html:** Página inicial com links para cadastro e listagem de pets.
- **bichos.html:** Lista de todos os pets cadastrados com opções para editar e deletar.
- **cad_pets.html:** Formulário para cadastro de novos pets.
- **edit_pets.html:** Formulário para edição das informações de um pet.

## Configuração do Projeto

### Pré-requisitos

- Python 3.6+
- Django 3.2+
- Virtualenv

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/marcio-guimaraes/django-pet-management.git
    cd django-pet-management
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No Linux/MacOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

6. Acesse o projeto no navegador em `http://127.0.0.1:8000/`

## Melhorias Futuras

- Implementação de uma interface gráfica para substituir o terminal.
- Desenvolvimento de um site para integração com o sistema atual.
- Adição de funcionalidades como upload de fotos dos pets.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

Projeto desenvolvido por [Márcio Guimarães](https://github.com/marcio-guimaraes).
