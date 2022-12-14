"""
Relacionamento entre tabelas
    -Chave primária
    -Chave estrangeira

Cardinalidade
        -> O tipo de ligação entre as tabelas relacionadas
        1:1 -> Um para um
        1:N -> Um para N (Um para muitos)
        N:N -> N para N (Muitos para muitos)

Modelagem de sistema simples de blog
    - Quem fará a postagem será um usuário
    - Um usuário possui apenas 1 perfil associado a ele e vice-versa
    - Um usuário pode fazer 1 ou várias postagens
    - Pra cada postagem, podem estar associadas 1 ou mais categorias
    - Um categoria pode estar associada a várias postagens
    - Cada mensagem pode ter nenhum, 1 ou mais comentários
    - Cada comentário pertence a apenas 1 usuário

"""

import sqlite3

if __name__ == "__main__":
    # Criando a conexão com o banco
    # Se o arquivo não existir ele cria o arquivo e a conexão
    # Se já existir, apenas conecta com o banco
    conexao = sqlite3.connect("db.sqlite3")

    # Criação da tabela tb_usuarios

    comando = """
    CREATE TABLE IF NOT EXISTS tb_usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )  
    """

    conexao.execute(comando)

    # Garantindo que o sqlite utilize de forma correta foreign keys
    conexao.execute("PRAGMA foreign_keys = ON")

    # Criação da tabela tb_perfis
    # Como definimos a coluna id como chave primária da tabela tb_perfis
    # e, ao mesmo tempo, chave estrangeira da tabela tb_usuarios,
    # estabelecemos uma relação 1:1 entre as tabelas tb_usuarios e tb_perfis.
    comando = """
    CREATE TABLE IF NOT EXISTS tb_perfis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT,
        FOREIGN KEY (id) REFERENCES tb_usuarios (id)
    )
    """

    conexao.execute(comando)

    # Criação da tabela tb_postagens
    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        texto TEXT NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id)
    )
    """
    conexao.execute(comando)

    # Criação da tabela tb_postagens_categoria
    # Nesse caso, temos uma relação de N:N
    comando = """
    CREATE TABLE IF NOT EXISTS tb_categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """
    conexao.execute(comando)

    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
        id_postagem INTEGER NOT NULL,
        id_categoria INTEGER NOT NULL,
        PRIMARY KEY (id_postagem, id_categoria),
        FOREIGN KEY (id_postagem) REFERENCES tb_postagens (id),
        FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id)
    )
    """
    conexao.execute(comando)

    # Criação da tabela tb_comentarios
    # id (integer, primaria e autoincrementada),
    # id_usuario (integer, chave estrangeira not null)
    # e texto (texto comum not null)