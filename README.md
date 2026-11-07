#  SOS Campo Grande

### Uma cidade melhor começa com a participação de todos.

O **SOS Campo Grande** é uma aplicação web desenvolvida em Python e Django, com o objetivo de facilitar o registro, a visualização e o acompanhamento de problemas urbanos na cidade de Campo Grande, Mato Grosso do Sul.

O projeto foi desenvolvido para um **Hackathon**, dentro do tema **Cidades Inteligentes e Sustentabilidade Local**, buscando demonstrar como a tecnologia pode incentivar a participação da população na melhoria dos espaços públicos.

---

##  Sobre o projeto

Problemas como buracos nas ruas, iluminação pública inadequada, descarte irregular de lixo e vazamentos de água afetam a qualidade de vida dos moradores.

O SOS Campo Grande propõe uma plataforma simples e acessível, onde os cidadãos podem registrar essas ocorrências e acompanhar seu status.

A aplicação também disponibiliza indicadores que ajudam a visualizar a quantidade de problemas cadastrados, pendentes e resolvidos.

> **Observação:** este é um protótipo acadêmico e não possui integração oficial com a Prefeitura de Campo Grande.

##  Funcionalidades

- **Registro de ocorrências:** cadastro de problemas urbanos com título, descrição, bairro e categoria.
- **Listagem de ocorrências:** visualização dos problemas registrados.
- **Filtros:** pesquisa de ocorrências por categoria e status.
- **Página inicial:** apresentação do projeto, indicadores gerais e registros recentes.
- **Painel de indicadores:** acompanhamento de ocorrências pendentes, em andamento e resolvidas.
- **Administração:** gerenciamento dos registros por meio do Django Admin.
- **Interface responsiva:** layout adaptado para computadores e dispositivos móveis.

##  Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Django | Framework web e backend |
| SQLite | Banco de dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |

##  Demonstração do sistema

###  Página inicial

Apresenta o objetivo do projeto, indicadores gerais e as ocorrências mais recentes.

![Página inicial do SOS Campo Grande](docs/images/home.png)


##  Estrutura do projeto

```text
soscg/
├── app/                  # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── ocorrencias/          # Aplicação principal
│   ├── migrations/
│   ├── static/
│   │   └── ocorrencias/
│   │       └── style.css
│   ├── templates/
│   │   └── ocorrencias/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── lista.html
│   │       ├── cadastrar.html
│   │       └── painel.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── docs/
│   └── images/           # Capturas de tela
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

Como executar o projeto

Pré-requisitos

Antes de começar, tenha instalado:

Python 3.12 ou superior, com versão compatível com as dependências do projeto

Git

Um editor de código, como o Visual Studio Code

1. Clonar o repositório

Abra um terminal e execute:

git clone https://github.com/114046PK/sos_campo_grande.git
cd sos_campo_grande

2. Criar o ambiente virtual

No Windows (PowerShell):

python -m venv .venv

3. Ativar o ambiente virtual

No PowerShell:

.\.venv\Scripts\Activate.ps1

Caso esteja usando CMD:

.venv\Scripts\activate.bat

No Linux ou macOS:

source .venv/bin/activate

4. Instalar as dependências

Com o ambiente virtual ativado:

python -m pip install -r requirements.txt

5. Verificar as configurações

python manage.py check

Se não houver problemas de configuração, continue.

6. Preparar o banco de dados

O projeto utiliza SQLite, portanto não é necessário instalar um servidor de banco de dados.

Execute:

python manage.py migrate

Esse comando cria o banco de dados local e aplica as migrações versionadas no repositório.

7. Criar um administrador (opcional)

python manage.py createsuperuser

Informe um nome de usuário e uma senha.

8. Executar o projeto

python manage.py runserver

Abra o navegador:

http://127.0.0.1:8000/

9. Acessar as funcionalidades

Página

Endereço

Início

/

Ocorrências

/ocorrencias/

Registrar ocorrência

/cadastrar/

Painel de indicadores

/painel/

Administração

/admin/

10. Executar os testes

Para executar os testes automatizados:

python manage.py test

Observações importantes

O arquivo db.sqlite3 não é enviado ao GitHub. Ele é criado localmente ao executar as migrações.

O ambiente virtual .venv também não é versionado.

Execute os comandos na pasta que contém manage.py.

A aplicação utiliza o servidor de desenvolvimento do Django. As configurações de produção exigem ajustes adicionais.

##  Banco de dados

O projeto utiliza SQLite para armazenar as ocorrências.

O modelo principal é `Ocorrencia`, contendo informações como:

- Título e descrição
- Bairro
- Categoria do problema
- Status da ocorrência
- Data de criação

Os dados são manipulados por meio do ORM do Django.

##  Melhorias futuras

- [ ] Autenticação de moradores
- [ ] Upload de fotografias das ocorrências
- [ ] Geolocalização dos problemas em um mapa
- [ ] Busca por bairro
- [ ] Gráficos interativos
- [ ] Sistema de notificações
- [ ] Moderação e validação de ocorrências
- [ ] Integração com serviços públicos

## Objetivo do Hackathon

Demonstrar como uma solução digital pode aproximar a população dos problemas urbanos e contribuir para decisões baseadas em informações organizadas.

O SOS Campo Grande busca incentivar a cidadania, a transparência e a participação comunitária.

##  Desenvolvimento

Projeto desenvolvido para fins acadêmicos e de apresentação em Hackathon.

**Grupo:** [Bar sem Lona]

**Desenvolvedor(es):** [Pedro Kawahata | Antônio Raquita | Kaemy Reis]

**Instituição:** [Unigran]

**Evento:** [Hackathon UniGran]

**Local:** Campo Grande — MS

---

**SOS Campo Grande — Tecnologia e participação por uma cidade melhor.**
