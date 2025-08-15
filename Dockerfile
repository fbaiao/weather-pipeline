# 1. Escolhe a imagem base do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Instala dependências do sistema, incluindo Git
RUN apt-get update && apt-get install -y \
    git \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

# 4. Copia o arquivo de dependências e instala pacotes Python
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# 5. Copia todo o código do projeto para dentro do container
COPY . .

# 6. Comando neutro para manter o container ativo
CMD ["sleep", "infinity"]
