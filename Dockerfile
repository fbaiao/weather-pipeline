# 1. Escolhe a imagem base do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Instala dependências do sistema mínimas (git se for necessário)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Copia o arquivo de dependências e instala pacotes Python
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# 5. Copia o código do projeto
COPY . .

# 6. Comando padrão: executa o pipeline
CMD ["python", "src/main.py"]
