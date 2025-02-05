# Import
import mysql.connector
from playwright.sync_api import sync_playwright

# Conecta ao banco de dados MySQL.
conexao_bd = mysql.connector.connect(
    host='localhost',       
    user='root',            
    password='1234@Teste.',  
    database='Tarefas'
)

# Inicializa um cursor, que é usado para interagir com o banco de dados e executar comandos SQL.
cursor_bd = conexao_bd.cursor()

# Utlizando Playwright para capturar o título da primeira notícia.
with sync_playwright() as p:
    browser = p.chromium.launch()  # Abre o navegador Chromium em segundo plano para navegar no site de notícias e extrair informações.
    pagina_web = browser.new_page() # Cria uma nova página em branco no navegador para acessar um site específico.

    # Acessa a URL para extrair o título da notícia
    pagina_web.goto('https://www.cnnbrasil.com.br/internacional/argentina-anuncia-saida-da-organizacao-mundial-da-saude/')

    # Extrai o título da notícia que está na página web 
    noticia_titulo = pagina_web.locator('h1.single-header__title').text_content()

    # Imprime o título da notícia que foi capturado da página
    print(noticia_titulo)
    # Executa o comando SQL para salvar o título da notícia na tabela tbl_noticias
    cursor_bd.execute('INSERT INTO tbl_noticias (vl_noticias) VALUES (%s)', (noticia_titulo,))
    conexao_bd.commit()  # Salva a alteração no banco de dados
    print('Notícia armazenada com sucesso!')
    # Fecha o navegador após terminar a coleta da notícia
    browser.close()

# Fecha a conexão com o banco de dados após salvar a notícia, para liberar recursos
cursor_bd.close()
conexao_bd.close()
