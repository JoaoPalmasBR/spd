# Servidor Python com Comunicação Segura

Este projeto é um servidor Python que utiliza `socket`, `threading`, `json` e `pycryptodome` para comunicação segura entre cliente e servidor.

## 📌 Pré-requisitos

Certifique-se de ter o Python instalado. Você pode verificar a instalação com:

```sh
python --version
```

Caso não tenha o Python instalado, baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/).

## 📦 Instalação das Dependências

As bibliotecas `socket` e `threading` já estão incluídas no Python padrão. No entanto, você precisa instalar `pycryptodome` para criptografia. Execute:

```sh
pip install pycryptodome
```

## 🚀 Como Executar o Servidor

1. Navegue até o diretório onde está o script do servidor.
2. Execute o seguinte comando:

```sh
python servidor.py
```

O servidor será iniciado e aguardará conexões dos clientes.

## 🖥️ Como Executar o Cliente

1. Em outro terminal, vá até o diretório onde está o script do cliente.
2. Execute o seguinte comando:

```sh
python cliente.py
```

O cliente se conectará ao servidor e poderá enviar mensagens criptografadas.

## 🛠️ Estrutura do Projeto

```
📂 meu_servidor
 ├── servidor.py   # Código do servidor
 ├── cliente.py    # Código do cliente
 ├── README.md     # Este arquivo
```

## 📚 Tecnologias Utilizadas

- `socket` → Comunicação entre cliente e servidor.
- `threading` → Permite múltiplas conexões simultâneas.
- `json` → Estruturação de mensagens.
- `Crypto.Cipher` (PyCryptodome) → Criptografia para mensagens seguras.

## 📞 Integrantes

@Emmanuel de Oliveira Peralta
@Felipe Nobrega
@João Antonio dos Santos Ilario
@Nathan Aguiar Silva

Caso tenha dúvidas ou sugestões, entre em contato!

---

Este README fornece um guia rápido para instalação, execução e explicação das bibliotecas utilizadas no projeto.
