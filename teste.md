<h1 align="center" style="font-weight: bold;">Hotel Reservation Price Classification 💻</h1>
<p align="center">
 <a href="#colab">Colaboradores</a> •
 <a href="#tech">Tecnologias</a> • 
  <a href="#tech">Desenvolvimento</a> • 
 <a href="#started">Iniciando a aplicação</a> • 
 <a href="#routes">Dificuldades</a> •
</p>
<p align="center">
    <b>Esta API foi desenvolvida para classificar reservas de hotéis em faixas de preço, utilizando machine learning com serviços AWS.</b>
</p>
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
<h2 id="tech">💻 Tecnologias</h2>
Python
Flask / FastAPI
Docker
AWS SageMaker
AWS RDS
AWS S3
<b> Ferramentas de desenvolvimento </b>

Jupyter Notebook
Git
VS Code
<h2 id="started">🚀 Iniciando a aplicação</h2>
Siga os passos abaixo para configurar e executar a API

<h3>Pré-requisitos</h3>
Antes de começar, certifique-se de que você tem os seguintes itens instalados:

Python
Docker
<h3>Clonando o repositório</h3>
bash
Copiar código
git clone https://github.com/Compass-pb-aws-2024-MAIO-A/sprints-4-5-pb-aws-maio.git
<h3>Configurando as variáveis .env</h2>
Use o arquivo .env.example como referência para criar seu arquivo de configuração .env.

env
Copiar código
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
RDS_DB_NAME=your_rds_db_name
RDS_USERNAME=your_rds_username
RDS_PASSWORD=your_rds_password
RDS_HOSTNAME=your_rds_hostname
RDS_PORT=your_rds_port
<h3>Iniciando</h3>
bash
Copiar código
docker build -t hotel-reservation-api .
docker run -p 5000:5000 hotel-reservation-api
<h2 id="routes">Dificuldades Encontradas</h2>