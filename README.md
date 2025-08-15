# Weather Pipeline (OpenWeatherMap)

Pipeline diário em Python para coletar o clima atual de uma lista de cidades usando a API do OpenWeatherMap.

## 
- Estrutura modular (`src/`)
- Configuração externa (`config.example.json` + `.env.example`)
- Logs simples
- Escrita em CSV ou Parquet (configurável)
- GitHub Actions básico (CI)

## Como usar (local)
1. **Clone o repositório** e entre na pasta:
   git clone https://github.com/fbaiao/weather-pipeline.git

2. **Crie e ative um virtualenv** (opcional):
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. **Instale as dependências**:
   pip install -r requirements.txt

4. **Prepare as configs**:
   - Edite `.env` e informe sua API key (`OWM_API_KEY`).
   - (Opcional) Ajuste `config.json` (cidades, formato, caminho de saída).
     
5. **Execute**:
   python src/main.py

## Testes
pytest -q

## Variáveis e Configurações
- **API Key** vem do `.env` (variável `OWM_API_KEY`).
- **Lista de cidades**, unidades, formato de saída e caminho são definidos em `config.json`.

## Docker
Aadicionar `Dockerfile` e instruções

