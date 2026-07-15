# 📑 Leitor de Notas Fiscais (XML ➔ Excel)

Este projeto automatiza a leitura de arquivos XML de Notas Fiscais Eletrônicas (NF-e), extrai os dados essenciais e os consolida em uma planilha Excel de forma organizada e incremental.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.13+**
* **Pandas & Openpyxl**: Para manipulação de dados e exportação para Excel.
* **xmltodict**: Para converter os arquivos XML das notas em dicionários Python.
* **python-dotenv**: Para gerenciamento seguro de variáveis de ambiente (caminhos de pastas).
* **OS & Sys**: Manipulação de arquivos do sistema e fluxos de erro.

---

## 🚀 Como Executar o Projeto na Sua Máquina

Siga o passo a passo abaixo para configurar e rodar a aplicação localmente.

### 1. Clonar o Repositório
Abra o seu terminal e clone este projeto:
```bash
git clone [https://github.com/larigeorgia/leitor-de-notas-fiscais-xml.git](https://github.com/larigeorgia/leitor-de-notas-fiscais-xml.git)
cd leitor-de-notas-fiscais-xml
```

---

### 2. Configurar o Ambiente Virtual (venv)
Crie e ative o seu ambiente isolado para garantir que as dependências não conflitem com seu sistema:
- No Windows (PowerShell):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
- No Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instalar as Dependências
Com o ambiente virtual ativo, instale os pacotes necessários rodando:
- No Windows (PowerShell):
```bash
pip install pandas openpyxl xmltodict python-dotenv
```

---
### 4. Configurar as Variáveis de Ambiente (.env)
1 - Na raiz do projeto, crie um arquivo chamado .env.

2 - Adicione a variável apontando para a pasta onde você salvará suas notas fiscais. Exemplo:

```bash
CAMINHO_PASTA_NOTAS = 'C:/Users/Usuario/Desktop/NotasFiscais'
```
3 - Crie a pasta correspondente (neste caso, uma pasta chamada NotasFiscais na raiz do projeto) e coloque seus arquivos .xml lá dentro.

--- 

### 5. Rodar a Aplicação
Execute o script principal:

```bash
python script.py
```

--- 

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

Este projeto foi desenvolvido utilizando práticas modernas de desenvolvimento de software, contando com o apoio de Inteligência Artificial Gemini como copiloto para a estruturação desta documentação e otimização de boas práticas de código.