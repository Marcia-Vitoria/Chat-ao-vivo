# Título: PapoZap
# Botão de iniciar chat
# Popup para entrar no chat (modal/alerta/popup)
    # Título: Bem-vindo ao PapoZap
# Campo de texto: Escreva seu nome no chat
# Botão: Entrar no chat
# Quando entrar no chat: (aparece para todo mundo)
    # A mensagem que você entrou no chat ("nome do usuário entrou no chat")
    # O campo e o botão de enviar mensagem
# Some o título e o botão inicial
# Fecha o popup
# A cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

# Flet -> aplicativo/site/programa de computador (framework)
# pip install flet

# Frameworks para criar sites em Py: Flask(aplicativo), Django(aplicativo), Fast Api(API), Tornado(Pouco usado) e Flet(Novo).
# Socket -> túnel de comunicação
# Deploy -> Para mais de dois computadores

# Importar o Flet
import flet as ft

# Criar a função principal do seu sistema
# Toda função que é usada dentro de um botão ela tem que receber como parâmetro um evento
def main(pagina):
    # Criar alguma coisa
    # Criar o título
    titulo = ft.Text("PapoZap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # Cria o túnel de comunicação
    
    titulo_janela = ft.Text("Bem-vindo ao PapoZap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # Enviar a mensagem no chat
            # Usuário: mensagem do usuário
        chat.controls.append(ft.Text(texto))

        # Enviar uma mensagem no túnel
        pagina.pubsub.send_all("Vitória entrou no tunel") # Envia uma mensagem no túnel

        # Limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()
    # Colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        # Tirar o título da página
        pagina.remove(titulo)
        # Tirar o botão_iniciar
        pagina.remove(botao_iniciar)
        # Fechar popup/janela
        janela.open = False
        # Criar o chat
        pagina.add(chat)
        # Criar o campo de texto de enviar mensagem (fora da função)
        #pagina.add(texto_mensagem)
        # Criar o botao enviar mensagem (fora da função)
        #pagina.add(botao_enviar)
        # ADICIONAR A LINHA DE MENSAGEM
        pagina.add(linha_mensagem)

        # Escrever a mensagem: usuário entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_nome_usuario, 
        actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Colocar essa coisa na página
    # Adicionar título na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Executar o seu sistema
#ft.app(main) 
ft.app(main, view=ft.WEB_BROWSER)