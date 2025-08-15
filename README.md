# Weather Pipeline (OpenWeatherMap)

Pipeline diário em Python para coletar o clima atual de uma lista de cidades usando a API do OpenWeatherMap.

## ✨ O que já vem pronto
- Estrutura modular (`src/`)
- Configuração externa (`config.example.json` + `.env.example`)
- Logs simples
- Escrita em CSV ou Parquet (configurável)
- GitHub Actions básico (CI)
- Licença MIT

## 🚀 Como usar (local)
1. **Clone o repositório** e entre na pasta:
   ```bash
   git clone <SEU_REPO_URL>
   cd weather-pipeline
   ```
2. **Crie e ative um virtualenv** (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare as configs**:
   - Copie os ficheiros de exemplo:
     ```bash
     cp config.example.json config.json
     cp .env.example .env
     ```
   - Edite `.env` e informe sua API key (`OWM_API_KEY`).
   - (Opcional) Ajuste `config.json` (cidades, formato, caminho de saída).
5. **Execute**:
   ```bash
   python src/main.py
   ```

## 🧪 Testes
```bash
pytest -q
```

## 🔧 Variáveis e Configurações
- **API Key** vem do `.env` (variável `OWM_API_KEY`).
- **Lista de cidades**, unidades, formato de saída e caminho são definidos em `config.json`.

## 📦 Docker (adiar se preferir)
Você poderá adicionar depois um `Dockerfile` e instruções. O projeto já está pronto para isso.

## 📝 Licença
[MIT](LICENSE)
