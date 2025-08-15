# 1. Escolhe a imagem base do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências e instala pacotes
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 4. Copia todo o código do projeto para dentro do container
COPY . .

# 5. Comando padrão ao iniciar o container
CMD ["python", "src/main.py"]
