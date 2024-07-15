<h1 align="center" style="font-weight: bold;">Reserva Inteligente 💡</h1>
<p align="center">
 <a href="#tech">Tecnologias</a> • 
  <a href="#dev">Desenvolvimento</a> • 
 <a href="#started">Iniciando a aplicação</a> • 
 <a href="#routes">Dificuldades</a> •
 <a href="#colab">Colaboradores</a> 
</p>
<p align="center">
    <i>O sistema Reserva Inteligente foi desenvolvido para classificar reservas de hotéis em faixas de preço de acordo com dados recebidos através da API, utilizando Machine Learning com serviços da AWS.</i>
</p>

<h2 id="tech">💻 Tecnologias</h2>

- **Python** (v3.11)
- **FastAPI** (0.111.0)
- **Docker** (v25.0.3)
- **AWS SageMaker**
- **AWS RDS**
- **AWS S3**
- **Uvicorn** (v0.30.1)

### Bibliotecas
- **Boto3** (v1.34.144) 
- **Joblib** (v1.4.2)
- **Pandas** 
- **Pydantic** (v1.10.17)
- **Scikit-learn** 
- **XGBoost** 

<h3> Ferramentas de Desenvolvimento </h3>

- **Jupyter Notebook** (https://jupyter.org/)
- **Git** (https://git-scm.com/) 
- **VS Code** (https://code.visualstudio.com/)
- **Trello** (https://trello.com/)

<h2 id="dev">👩🏻‍💻  Desenvolvimento</h2>

### Coleta e Preparação de Dados

### Dataset:
- Utilizamos o Hotel Reservations Dataset do Kaggle.

### Processamento e Limpeza:
- Criamos uma nova coluna `label_avg_price_per_room` para classificação, com os seguintes critérios:
  - `1` quando `avg_price_per_room` ≤ 85
  - `2` quando `avg_price_per_room` > 85 e < 115
  - `3` quando `avg_price_per_room` ≥ 115
- Excluímos a coluna original `avg_price_per_room`.

### Armazenamento de Dados:
- Armazenamos o dataset original e o dataset alterado em um banco de dados AWS RDS para acesso eficiente e seguro.

## Desenvolvimento do Modelo

### Treinamento do Modelo:
- Utilizamos o AWS SageMaker para treinar um modelo de Machine Learning utilizando o algoritmo XGBoost.
- Ajustamos o modelo para atingir a melhor precisão possível.
- Avaliamos a taxa de assertividade do modelo.

### Armazenamento do Modelo:
- O modelo treinado foi salvo em um bucket AWS S3 para fácil acesso e gerenciamento.

## Implementação do Modelo

### Ambiente Docker:
- Criamos um ambiente Docker na AWS para implementar a API.

### Desenvolvimento da API:
- Desenvolvemos um serviço em Python utilizando o framework FastAPI.
- A API carrega o modelo treinado do S3 e expõe um endpoint para realizar a inferência.
- O endpoint é um POST com a rota `/api/v1/inference` e recebe um JSON no corpo da requisição.


<h2 id="pastas">📂 Organização de pastas</h2>

```
api
├── models
│   ├── InferenceRequest.py
│   ├── InferenceResponse.py
│   ├── MockModel.py
│   └── main.py
├── assets
│   ├── dataset_schema.png
│   └── sprint4-5.jpg
├── notebooks
│   ├── pre_processing.ipynb
│   ├── prediction.ipynb
│   └── training.ipynb
├── .gitignore
└── README.md
```

<h2 id="started">🚀 Iniciando a aplicação</h2>
Siga os passos abaixo para configurar e executar a API

### Pré-requisitos
Antes de começar, certifique-se de que você tem os seguintes itens instalados:

- Python
- Docker

### Clonando o repositório
```
git clone https://github.com/Compass-pb-aws-2024-MAIO-A/sprints-4-5-pb-aws-maio.git
```
### Configurando as variáveis .env
```
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
RDS_DB_NAME=your_rds_db_name
RDS_USERNAME=your_rds_username
RDS_PASSWORD=your_rds_password
RDS_HOSTNAME=your_rds_hostname
RDS_PORT=your_rds_port
```
### Iniciando
```
docker build -t hotel-reservation-api .
docker run -p 5000:5000 hotel-reservation-api
```

<h2 id="routes">⛔ Dificuldades</h2>
Maiores dificuldades encontradas durante o desenvolvimento do projeto:

- Persistir os dados no S3;
- Transformar colunas categóricas em binárias;
- Encontrar melhor maneira de treinar o modelo;
- Melhorar a acurácia do modelo;
- Lidar com as métricas do SageMaker.

<h2 id="colab">🤝 Colaboradores</h2>
<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="assets/cayo.png" width="100px;" /><br>
        <sub>
          <b>Cayo Bruno</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="assets/juliana.png" width="100px;" /><br>
        <sub>
          <b>Juliana Ferreira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="assets\madu.png" width="100px;" /><br>
        <sub>
          <b>Maria Eduarda</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="assets\olivia.png" width="100px;" /><br>
        <sub>
          <b>Olivia Oliva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h3 align="center">Obrigada pela leitura!</h3>
Versão 0.0.1
