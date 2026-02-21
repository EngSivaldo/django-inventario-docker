# Sistema de Inventário 📦
Projeto de estudo focado em arquitetura profissional com Docker e CI/CD.

## Tecnologias
* Python / Django
* PostgreSQL
* Docker & Docker Compose
* GitHub Actions (CI/CD)


Perfeito! Como um engenheiro, agora que temos o **Blueprint** (documentação) assinado, vamos para a fase de **Execução Técnica**.

Para mantermos a organização profissional que planejamos, vamos criar os três módulos (apps) que dividirão as responsabilidades do sistema.

### 🛠️ Passo 1: Execução no Terminal

Com a sua `venv` ativa e na pasta do projeto, execute estes três comandos em sequência:

```powershell
python manage.py startapp produtos
python manage.py startapp usuarios
python manage.py startapp api

```

### 📂 Passo 2: Registro no Setup

O Django só reconhece os apps se eles estiverem listados no arquivo de configuração principal.

1. Abra o arquivo `setup/settings.py`.
2. Procure pela lista `INSTALLED_APPS`.
3. Adicione os nomes dos apps que acabamos de criar (não esqueça da vírgula no final):

```python
INSTALLED_APPS = [
    # ... apps padrão do django ...
    'produtos',
    'usuarios',
    'api',
]

```



* **Modularidade**: Se no futuro você quiser trocar a interface Web por um aplicativo mobile, a lógica já está separada no app `api`.
* **Manutenção**: Se houver um erro no login, você sabe exatamente que o problema está na pasta `usuarios`, sem afetar o cálculo de estoque em `produtos`.

Próximos Passos: Criação dos Apps
Seguindo o plano de engenharia, vamos iniciar a Fase de Implementação criando a estrutura modular de apps:

1. App `produtos`: Responsável pelo core business (Produtos, Categorias e Movimentações).

2. App `usuarios`: Gestão de autenticação e níveis de acesso (Operador/Gerente).

3. App `api`: Interface de comunicação REST para integrações futuras.

Comandos para execução no terminal:

```

python manage.py startapp produtos

python manage.py startapp usuarios

python manage.py startapp api
