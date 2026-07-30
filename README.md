# Euromillions Scraping

Sistema para raspagem e armazenamento de resultados do Euromilhões da Santa Casa.

## Instalação

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Executar o programa principal
```bash
python3 db_utils.py
```

### Testar o sistema
```bash
python3 test_sistema.py
```

## Funcionalidades

- Raspagem automática de resultados do site da Santa Casa
- Armazenamento em CSV e SQLite
- Interface de linha de comando para gestão de dados
- Atualização automática de novos sorteios

## Estrutura

- `db_utils.py` - Módulo principal com todas as funcionalidades
- `test_sistema.py` - Testes do sistema
- `data/resultados.csv` - Dados históricos em CSV
- `instance/euromilhoes.db` - Base de dados SQLite
- `requirements.txt` - Dependências do projeto