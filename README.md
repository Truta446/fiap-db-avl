# FIAP AVL ONG

## Introduction

>Foi realizado um algoritmo para armazenamento de dados em uma árvore AVL.

>Para popular rapidamente a árvore, é lido do arquivo 'to-read.json' alguns dados já preenchidos para facilitar a visualização.

>Categorias: Atendente, Doador, Funcionário, Visitante e Voluntário;

>Opções possíveis:
    - Listar nomes em formato de árvore;
    - Listar nomes em ordem alfabética;
    - Listar um usuário digitando um nome;
    - Criar um novo usuário;
    - Atualizar dados de um usuário;
    - Deletar um usuário;

## Quick start

Para executar o projeto, basta rodar o seguinte comando com Python:

> Instalando dependencias:

```sh
pip install snakeviz
```

> Executando projeto:

```sh
python3 main.py
```

> Para rodar o projeto e ver as métricas, execute esses comandos:

```sh
python3 -m cProfile -o profile.prof main.py
```

```sh
snakeviz profile.prof
```

> Vai abrir uma URL no navegador para checar as informações sobre a análise de desempenho do meu projeto.