## **📰  Captura de Título de Notícia e Armazenamento em Banco de Dados 🗃️**

##  **🎯 Objetivo**

O objetivo desta tarefa é realizar uma busca em um site de notícias, escolher uma notícia e capturar o título da notícia principal. Em seguida, o título é salvo em uma tabela no banco de dados MySQL. Tudo isso de forma automatizada e eficiente! 🚀



**🛠️ Passo a Passo para Executar o Script e Criação do Banco de Dados**

🗄️ Banco de Dados MySQL
Utilizamos o MySQL para armazenar os dados de forma organizada e segura.

**Criação do Banco de Dados**

O banco de dados foi criado com o seguinte comando:

🔹 **CREATE DATABASE TAREFAS;**

Criação da Tabela
Em seguida, criamos uma tabela para armazenar os títulos das notícias:


```bash

CREATE TABLE tbl_noticias (
    id_tbl_noticias INT AUTO_INCREMENT PRIMARY KEY,
    vl_noticias VARCHAR(1000) NOT NULL
);

```

**🎭 Instalação do Playwright**

Para automatizar a captura dos dados, utilizamos a biblioteca Playwright, que permite controlar um navegador de forma programática. Para instalá-la, basta rodar:

```bash
pip install playwright
playwright install

```
## **🐍 Desenvolvimento do Script em Python**

O script foi desenvolvido para:

Conectar ao banco de dados utilizando o **mysql.connector.**

Utilizar o **Playwright** para capturar o título da notícia.

**🧠 Uso do Playwright**

O Playwright abre o navegador, acessa o site de notícias e extrai o título da primeira notícia. Tudo isso de forma rápida e eficiente! 🕸️

Acesso à URL
O script acessa a URL do site de notícias para encontrar o título da notícia principal.

Extração do Título
O título é extraído da página web utilizando seletores do Playwright. 🎯

Exibição do Título
O título capturado é exibido no terminal para verificação. 🖥️

Inserção no Banco de Dados
O título é salvo na tabela tbl_noticias utilizando um comando SQL. 💾

Confirmação das Alterações
As alterações são confirmadas no banco de dados para garantir que os dados sejam persistidos. ✅

Com esse script, você pode automatizar a captura de títulos de notícias e armazená-los em um banco de dados MySQL de forma mais assertiva, sendo uma excelente maneira de integrar automação web junto com armazenamento de dados🚀


🎉 Espero que tenham gostado dessa tarefa! 🎉
Se surgirem dúvidas, sugestões ou precisarem de ajuda, estou à disposição para ajudar! 😊✨


