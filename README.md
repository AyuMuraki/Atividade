Primeira tarefa: O objetivo foi realizar uma busca em um site de notícias, escolher uma notícia e, em seguida, capturar o primeiro título da notícia principal e salvá-lo em uma tabela em um banco de dados.

1. Passo a passo para executar o script e criação de um banco de dados:
2. Banco de dados MySQL: Utilizamos o MySQL para armazenar os dados.
Criação do banco de dados: O banco de dados foi criado com o seguinte comando
CREATE DATABASE TAREFAS;
3.Criação da tabela: Em seguida, foi criada uma tabela para armazenar os títulos das notícias

CREATE TABLE tbl_noticias (
   id_tbl_noticias INT AUTO_INCREMENT PRIMARY KEY,
   vl_noticias VARCHAR(1000) NOT NULL
);


4.  Instalação do Playwright: Para utilizar os recursos de automação web, foi necessário instalar a biblioteca Playwright.
5.  Desenvolvimento do script em Python: O script foi desenvolvido para se conectar ao banco de dados utilizando o mysql.connector e ao Playwright utilizando from playwright.sync_api import sync_playwright.
6.  Uso do Playwright: O Playwright foi utilizado para capturar o primeiro título da notícia escolhida.
7.  Acesso à URL: O script acessa a URL do site de notícias para extrair o título.
8.  Extração do título: O título da notícia foi extraído da página web.
9.  Exibição do título: O título da notícia capturado foi impresso no terminal.
10. Inserção no banco de dados: O comando SQL a seguir foi executado para salvar o título da notícia na tabela tbl_noticias:
cursor_bd.execute('INSERT INTO tbl_noticias (vl_noticias) VALUES (%s)', (noticia_titulo,))


11. Confirmação das alterações: As alterações foram salvas no banco de dados com o comando adequado.
12. Conclusão: Com isso, o script está pronto para ser utilizado.

  Essa tarefa permite entender como funciona o Playwright e, de forma assíncrona, como integrar o processo de captura de dados com um banco de dados,
  salvando os dados em uma tabela.
