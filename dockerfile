FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# Construir a imagem:
#    docker build -t myapp .


# Executar o container: 
#    docker run -d -p 80:80 myapp