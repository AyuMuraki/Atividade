Primeira Tarefa: Captura de Título de Notícia e Armazenamento em Banco de Dados
Objetivo: Realizar uma busca em um site de notícias, escolher uma notícia e, em seguida, capturar o primeiro título da notícia principal e salvá-lo em uma tabela em um banco de dados MySQL.

Passo a Passo para Executar o Script e Criação do Banco de Dados
Banco de Dados MySQL
Utilizamos o MySQL para armazenar os dados.

Criação do Banco de Dados
O banco de dados foi criado com o seguinte comando:
CREATE DATABASE TAREFAS;

Criação da Tabela
Em seguida, foi criada uma tabela para armazenar os títulos das notícias:
CREATE TABLE tbl_noticias ( id_tbl_noticias INT AUTO_INCREMENT PRIMARY KEY, vl_noticias VARCHAR(1000) NOT NULL );

Instalação do Playwright
Para utilizar os recursos de automação web, foi necessário instalar a biblioteca Playwright.

Desenvolvimento do Script em Python
O script foi desenvolvido para se conectar ao banco de dados utilizando o mysql.connector e ao Playwright.

Uso do Playwright
O Playwright foi utilizado para capturar o primeiro título da notícia escolhida. O processo consiste em abrir o navegador, acessar o site e extrair o título da primeira notícia.

Acesso à URL
O script acessa a URL do site de notícias para extrair o título da notícia.

Extração do Título
O título da notícia foi extraído da página web utilizando o Playwright.

Exibição do Título
O título da notícia capturado foi impresso no terminal para verificar o resultado.

Inserção no Banco de Dados
O comando SQL foi executado para salvar o título da notícia na tabela tbl_noticias.

Confirmação das Alterações
As alterações foram salvas no banco de dados utilizando o comando adequado para garantir que os dados fossem persistidos.

Conclusão
Com isso, o script está pronto para ser utilizado, realizando a captura do título da notícia e o armazenamento no banco de dados.

Resumo
Essa tarefa permite entender como funciona o Playwright e, de forma assíncrona, como integrar o processo de captura de dados com um banco de dados, salvando as informações em uma tabela no MySQL.
