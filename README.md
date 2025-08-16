## Weather Pipeline (OpenWeatherMap)

Pipeline diário em Python para coletar o clima atual de uma lista de cidades usando a API do OpenWeatherMap.

## Funcionalidades
- Estrutura modular (`src/`)
- Configuração externa (`config.example.json` + `.env.example`)
- Logs simples
- Escrita em CSV ou Parquet (configurável)
- GitHub Actions básico (CI)

## Como usar localmente
1. **Clone o repositório** e entre na pasta:
   git clone https://github.com/fbaiao/weather-pipeline.git
   cd weather-pipeline

2. **Instale as dependências**:
   pip install -r requirements.txt

3. **Prepare as configs**:
   - Edite `.env`, baseado no ficheiro `.env.example`, e informe sua API key (`OPENWEATHER_API_KEY`).
   - (Opcional) Ajuste `config.json` (cidades, formato, caminho de saída).
     
4. **Execute**:
   python src/main.py

## Executar com Docker
- Build da imagem:
   docker build -t weather-pipeline .

- Rodar o container:
   docker run --rm --env-file .env weather-pipeline

Nota: O .env não está incluído na imagem Docker por motivos de segurança.

## GitHub Actions

O projeto já vem com workflows automáticos:

1. **CI (ci.yml)**

   - Quando roda: em push ou pull request.
   - O que faz: instala dependências e executa os testes com pytest.
   - Onde ver resultados: GitHub → Actions → CI.

2. **Build e Push Docker (docker.yml)**
   - Quando roda: em push para a branch main.
   - O que faz: builda a imagem Docker e envia para o Docker Hub (fabriciobaiao/weather-pipeline:latest).
   - Segredos necessários: DOCKER_USERNAME e DOCKER_PASSWORD no GitHub Secrets.

Dica: é possível disparar manualmente qualquer workflow pelo botão Run workflow no GitHub Actions.

## Testes
pytest -q

## Variáveis e Configurações
- **API Key** vem do `.env` (variável `OPENWEATHER_API_KEY`).
- **Lista de cidades**, unidades, formato de saída e caminho são definidos em `config.json`.


## Estrutura do projeto

weather_pipeline/
│── src/
│   ├── main.py            # ponto de entrada
│   ├── fetch_weather.py   # chamada à API
│   ├── config.py          # leitura das configs
│   ├── save_data.py       # salvamento CSV/Parquet
│   └── utils.py           # funções auxiliares
│
│── .devcontainer/         # configuração de devcontainer (VS Code / Codespaces)
│   └── devcontainer.json
│
│── .github/
│   └── workflows/         # pipelines CI/CD
│       ├── ci.yml
│       └── docker.yml
│
│── config.json
│── .env.example
│── requirements.txt
│── Dockerfile
│── README.md
│── data/

