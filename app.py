import os
import streamlit as st
from groq import Groq

# inicializa o tema
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def apply_theme():
    """Aplica o tema atual baseado na session_state"""
    if st.session_state.theme == "dark":
        st.markdown("""
        <style>
        /* Tema Escuro */
        .stApp {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
        
        header[data-testid="stHeader"] {
            background-color: #161B22 !important;
            color: #fafafa !important;
        }
        
        [data-testid="stBottom"] {
            background-color: #161b22 !important;
            border-top: 1px solid #333 !important;
        }
        
        [data-testid="stSidebar"] {
            background-color: #161b22 !important;
            color: #fafafa !important;
        }
                    
        .stChatInput {
            background-color: #161b22 !important;
            border-top: 1px solid #333 !important;
        }
        
        [data-testid="stChatInputTextArea"] {
            background-color: #262730 !important;
            color: #fafafa !important;
            border: 1px solid #444 !important;
        }
        
        [data-testid="stChatInputTextArea"]:focus {
            border-color: #1e88e5 !important;
            box-shadow: 0 0 0 2px rgba(30, 136, 229, 0.2) !important;
        }
        
        [data-testid="stMarkdownContainer"],
        label, p, span, h1, h2, h3, h4, h5, h6 {
            color: #fafafa !important;
        }
        
        .stChatMessage {
            background-color: transparent !important;
        }
        
        .stButton > button {
            background-color: #1e88e5 !important;
            color: white !important;
            border: none !important;
        }
        
        .stButton > button:hover {
            background-color: #1976d2 !important;
        }
        
        .stTextInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
            border: 1px solid #444 !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #1e88e5 !important;
            box-shadow: 0 0 0 2px rgba(30, 136, 229, 0.2) !important;
        }
        
        code {
            background-color: #1e1e1e !important;
            color: #fafafa !important;
        }
        
        pre {
            background-color: #1e1e1e !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
        }
        
        hr {
            border-color: #333 !important;
        }
        
        /* Estilo específico para o toggle */
        .stToggle {
            background-color: transparent !important;
        }
        
        [data-testid="stToggle"] > div {
            background-color: #444 !important;
        }
        
        [data-testid="stToggle"] > div > div {
            background-color: #1e88e5 !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        /* Tema Claro */
        .stApp {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border-bottom: 1px solid #e0e0e0 !important;
        }
        
        [data-testid="stBottom"] {
            background-color: #ffffff !important;
            border-top: 1px solid #e0e0e0 !important;
        }
        
        [data-testid="stBottomBlockContainer"] {
                    background-color: #FFFFFF !important;
                    color: #FFFFFF !important;
                    }

        [class="st-emotion-cache-jchovf e5ztmp71"] {
                    background-color: #F4F4F4 !important;
                    color: #FFFFFF !important;}

        [data-testid="stChatInputSubmitButton"] {
                    background-color: #6c757d !important;
                    color: #ffffff !important;}

        [data-testid="stSidebar"] {
            background-color: #f8f9fa !important;
            color: #000000 !important;
            border-right: 1px solid #e0e0e0 !important;
        }
        
        .stChatInput {
            background-color: #ffffff !important;
            border-top: 1px solid #e0e0e0 !important;
        }
        
        [data-testid="stChatInputTextArea"] {
            background-color: #f4f4f4 !important;
            color: #000000 !important;
            border: 1px solid #ddd !important;
        }
        
        [data-testid="stChatInputTextArea"]:focus {
            border-color: #1e88e5 !important;
            box-shadow: 0 0 0 2px rgba(30, 136, 229, 0.2) !important;
        }
        
        [data-testid="stMarkdownContainer"],
        label, p, span, h1, h2, h3, h4, h5, h6 {
            color: #000000 !important;
        }
        
        .stChatMessage {
            background-color: transparent !important;
        }
        
        .stButton > button {
            background-color: #1e88e5 !important;
            color: white !important;
            border: none !important;
        }
        
        .stButton > button:hover {
            background-color: #1976d2 !important;
        }
        
        .stTextInput > div > div > input {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #ddd !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #1e88e5 !important;
            box-shadow: 0 0 0 2px rgba(30, 136, 229, 0.2) !important;
        }
        
        code {
            background-color: #f5f5f5 !important;
            color: #000000 !important;
        }
        
        pre {
            background-color: #f5f5f5 !important;
            color: #000000 !important;
            border: 1px solid #ddd !important;
        }
        
        hr {
            border-color: #e0e0e0 !important;
        }
        
        /* Estilo específico para o toggle */
        .stToggle {
            background-color: transparent !important;
        }
        
        [data-testid="stToggle"] > div {
            background-color: #ddd !important;
        }
        
        [data-testid="stToggle"] > div > div {
            background-color: #1e88e5 !important;
        }
        
        [data-testid="stChatInput"] {
                    color: #6c757d !important;
                    opacity: 1px solid !important;
                    }

        [data-testid="stChatInputTextArea"]:: placeholder {
                    color: #6c757d !important;
                    opacity: 1px solid !important;
                    }

        /* Placeholder do chat input (texto "Qual sua dúvida sobre Python?") */
        [data-testid="stChatInputTextArea"]::placeholder {
                    color: #495057 !important; /* cinza escuro, ótima leitura */
                    opacity: 1 !important;
                    }
        </style>
        """, unsafe_allow_html=True)

def toggle_theme():
    # Função para alternar o tema
    if st.session_state.theme == "dark":
        st.session_state.theme = "light"
    else:
        st.session_state.theme = "dark"
    st.rerun()

st.set_page_config(
    page_title="IA helper",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()
    
CUSTOM_PROMPT ="""
Você é o "Code Helper", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

PROMPT_ESTUDO = """
Você é o Code Helper, um assistente especialista em Python para ESTUDO.

REGRAS DE OPERAÇÃO:
- Explique o conceito com clareza
- Use linguagem didática
- Mostre exemplos de código bem comentados
- Explique cada parte do código
- Inclua uma seção final chamada:
    📚 Documentação de Referência
    com links oficiais (docs.python.org ou da biblioteca usada)

Seja PACIENTE, CLARO e EDUCATIVO.
"""

PROMPT_RAPIDO = """
Você é o Code Helper, um assistente especialista em Python para RESPOSTAS RÁPIDAS.

REGRAS DE OPERAÇÃO:
- Seja DIRETO e OBJETIVO
- Prioriza o CÓDIGO
- Explique apenas se for NECESSÁRIO
- Não escreva textos longos
- Use exemplos simples e funcionais

Foque em PRODUTIVIDADE.
"""

PROMPT_PSEUDOCODIGO = """
Você é o Code Helper em MODO PSEUDOCÓDIGO.

OBJETIVO:
Ajudar o usuário a PENSAR na solução, não copiar código.

REGRAS OBRIGATÓRIAS:
- NÃO escreva código em Python, JavaScript ou qualquer linguagem de programação
- Use apenas PSEUDOCÓDIGO estruturado
- Use palavras como:
    INÍCIO, FIM, SE, SENÃO, ENQUANTO, PARA, FUNÇÃO
- Não use sintaxe de linguagem de programação real
- Não use imports, bibliotecas ou APIs reais

FORMATO DA RESPOSTA:
1. Explicação breve da LÓGICA
2. Pseudocódigo completo e organizado
3. Dicas para o usuário transformar isso em código real

IMPORTANTE:
Se o usuário pedir CÓDIGO diretamente, explique que neste modo você só gera PSEUDOCÓDIGO.
"""
with st.sidebar:
    st.title("🤖 Code Helper")

    st.markdown("Um assistente de IA focado em programação Python.")
    st.markdown("---")

    # tema escuro/claro
    st.markdown("### 🎨  Configuração de tema")

    # Toggle com callback
    current_theme = st.session_state.theme
    theme_label = "🌙 Tema escuro" if current_theme == "light" else "☀️ Tema claro"

    if st.button(theme_label, use_container_width=True, key="theme_toggle"): toggle_theme()
    st.markdown("---")

    # Campo para inserir a chave de API groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("## ⚙️ Modo de Resposta")
    modo_resposta = st.radio(
        "Escolha como deseja receber as respostas:",
        options=[
            "📖 Estudo", 
            "⚡ Rápido",
            "🧠 Pseudocódigo"
            ],
        index=0
    )

    st.session_state.modo_resposta = modo_resposta

    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. IA pode cometer erros!")

    st.markdown("---")
    st.markdown("### 🗑️ Conversa")
    if st.button("Limpar Conversa",use_container_width=True):
        if st.session_state.messages:
            st.session_state.messages = []
            st.success("Conversa limpa com sucesso!")
            st.rerun()
    
    st.markdown("---")
    st.markdown("📧 E-mail caso queira entrar em contato moochrocha@gmail.com")

    

st.title("CODE HELPER AI")

st.title("Assistente Pessoal de Programação Python 🤖")

st.caption("Faça sua pergunta sobre Linguagem Python e obtenha código, explicações e referências.")

st.caption(f"Modo ativo: {st.session_state.modo_resposta}")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:

    try:
        # Cria cliente Groq com a chave API fornecida
        client = Groq(api_key = groq_api_key)

    except Exception as e:

        # Exibe erro caso haja problema ao inicializar o client
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já exista mensagem, mostra aviso
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    # Se não houver cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role":"user", "content":prompt})

    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagem para enviar à API, incluindo prompt de sistema
    if st.session_state.modo_resposta == "📖 Estudo":
        system_prompt = PROMPT_ESTUDO
    elif st.session_state.modo_resposta == "⚡ Rápido":
        system_prompt = PROMPT_RAPIDO
    else:
        system_prompt = PROMPT_PSEUDOCODIGO

    messages_for_api = [{"role": "system", "content":system_prompt}]
    for msg in st.session_state.messages:

        messages_for_api.append(msg)

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):

            try:

                #Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-120b",
                    temperature= 0.7,
                    max_tokens = 2048
                )

                # Extrai a resposta gerada pela API
                help_coder_response = chat_completion.choices[0].message.content

                # Exibe a resposta no Streamlit
                st.markdown(help_coder_response)

                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content":help_coder_response})

            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")


st.markdown(
"""
<div style="text-align: center; color: gray;">
    <hr>
    <p>APP desenvolvido com base no curso Fundamento da Linguagem Python Data Science Academy</p>
</div
""",
unsafe_allow_html=True
)