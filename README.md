# Câmera Jovi

Aplicação de linha de comando que simula uma câmera inteligente. O projeto
permite gerar fotos de exemplo, aplicar filtros, simular um modo de foco e
organizar as fotos em uma galeria persistida em arquivo texto.

## Funcionalidades

- Captura de fotos com nome informado pelo usuário.
- Geração de uma URL de imagem usando o serviço
  [Picsum Photos](https://picsum.photos/).
- Filtros:
  - Normal
  - Preto e branco
  - Desfocado
  - Preto e branco + desfocado
- Modo foco, que simula uma captura com qualidade 4K.
- Visualização da galeria.
- Exclusão de uma foto pelo índice ou da última foto.
- Persistência das fotos no arquivo `galeria.txt`.

> As fotos não são baixadas para o computador. A aplicação salva os dados da
> foto e a URL gerada pelo Picsum em `galeria.txt`.

## Estrutura do projeto

| Arquivo | Descrição |
| --- | --- |
| `main.py` | Ponto de entrada da aplicação. |
| `funcoesDeCamera.py` | Menus, captura simulada, filtros, galeria e persistência. |
| `galeria.txt` | Arquivo usado para armazenar as fotos salvas. |

O diretório `.idea/` contém configurações do projeto para o IntelliJ/PyCharm.
Arquivos dentro de `__pycache__/` são gerados automaticamente pelo Python.

## Requisitos

- Python 3 instalado. O projeto foi configurado no ambiente de desenvolvimento
  com Python 3.14.
- Acesso à internet para abrir as URLs de imagens geradas pelo Picsum Photos.
- Terminal compatível com os caracteres usados nos menus.

Não há dependências de terceiros para instalar.

## Como executar

No diretório do projeto, execute:

```bash
python main.py
```

Em ambientes nos quais o comando `python` aponta para outra versão, use:

```bash
py main.py
```

Ao iniciar, o menu principal oferece as opções:

| Opção | Ação |
| --- | --- |
| `1` | Tirar uma foto ou usar o modo foco. |
| `2` | Selecionar o filtro ativo. |
| `3` | Consultar ou apagar fotos da galeria. |
| `0` | Encerrar a aplicação. |

## Formato da galeria

As fotos comuns são gravadas em `galeria.txt` no formato:

```text
nome;filtro;url
```

Cada foto ocupa uma linha e os campos são separados por ponto e vírgula.
O arquivo é lido novamente sempre que o menu principal é exibido, permitindo
manter a galeria entre execuções.
