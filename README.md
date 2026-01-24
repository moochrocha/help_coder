# 🤖 Help Coder AI

O **Help Coder AI** é um assistente de inteligência artificial focado em **programação Python**, desenvolvido para auxiliar estudantes e desenvolvedores iniciantes a compreender conceitos, exemplos práticos e boas práticas da linguagem.

A aplicação utiliza **Streamlit** para a interface web e a **API da Groq** para geração das respostas com modelos de linguagem de grande escala (LLMs).

---

## 🎯 Objetivo do Projeto

O principal objetivo deste projeto é:

- Auxiliar no aprendizado da linguagem Python
- Fornecer explicações claras e didáticas
- Apresentar exemplos de código bem comentados
- Direcionar o usuário para documentações oficiais
- Demonstrar, na prática, o uso de APIs de IA em aplicações web

---

## 🧠 Funcionalidades

- 💬 Chat interativo para perguntas sobre Python
- 🧑‍🏫 Respostas estruturadas com:
  - Explicação conceitual
  - Exemplos de código em Python
  - Detalhamento do funcionamento do código
  - Links para documentação oficial
- 📜 Histórico de mensagens durante a sessão
- 🔐 Uso seguro de API Key via campo protegido
- 🌐 Interface web simples e intuitiva

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.14**
- **Streamlit 1.53.1**
- **Groq API**
- **Modelos LLM (openai/gpt-oss-120b)**

---

## 📦 Instalação e Execução Local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/moochrocha/help_coder.git
cd seu-repositorio
```

### 2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate #Windows
source venv/bin/activate #Linux/Mac
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute a aplicação

```bash
streamlit run app.py
```

---

## 🗝️ Configuração da API Key (Groq)

Você pode inserir a API Key diretamente pela interface ou definir como variável de ambiente:

```bash
export GROQ_API_KEY="sua_chave_aqui" # Linux/Max
set GROQ_API_KEY="sua_chave_aqui" # Windows
```

- No Streamlit Cloud, a chave deve ser configurada via Secrets

---

## 💻 Deploy no Streamlit Cloud

1. Suba o projeto para um repo no GitHub
2. Acesse: https://streamlit.io/cloud
3. Conecte o repo
4. Informe o arquivo principal (app.py)
5. Configure a variável `GROQ_API_KEY` no Secrets (se houver)
6. Deploy

---

## ⚠️ Observações importantes

- Este projeto tem fins educacionais
- A IA pode cometer erros ou gerar respostas imprecisas
- Sempre consulte a documentação oficial para uso em produção

---

## Créditos

Este projeto foi desenvolvido com base no curso **Fundamentos da Linguagem Python - do Básico a aplicações com IA da Data Science Academy**, sendo expandido e adaptado com novas funcionalidades.

---

## Autor

Desenvolvido por **Moises Rocha**

📎Linkedin: https://www.linkedin.com/in/moises-rocha-irineu/
