# AIO-CHAT - A QUIC CHAT APP

Implementação de um chat simples utilizando o protocolo QUIC. Este projeto foi baseado no repositório [aioquic](https://github.com/aiortc/aioquic), que é uma implementação do protocolo QUIC em Python.

## Pré-requisitos

- Python >=3.7
- Pipenv >=2023.6.18
- OpenSSL >=1.1.1

## Observação

Espera-se que todos os comandos sejam executados na raíz do projeto, isto é, no mesmo diretório deste arquivo:

- aio-chat
  - certificates
  - src
  - tests
  - Pipfile
  - Pipfile.lock
  - `README.md`

```
$ ls
LICENSE.md  Pipfile  Pipfile.lock  README.md  certificates src  tests
```

## Como usar

Para executar o servidor, primeiro é necessário instalar as dependências do projeto.

Entre no ambiente virtual e instale as dependências:

```
$ pipenv shell
$ pipenv install
```

Com isso, será possível executar o servidor:

```
python3 src/quic/http3_server.py \
  --certificate certificates/ssl_cert.pem \
  --private-key certificates/ssl_key.pem
```

Após iniciar o servidor, é possível executar uma ou mais instâncias do cliente:

```
python3 src/quic/http3_client.py \
  --print-response \
  --ca-certs certificates/pycacert.pem \
  --username test \
  wss://localhost:4433/ws
```

- O parâmetro `--username` é opcional e, caso não seja informado, o cliente será identificado como `anonymous-*`, sendo `*` um `id` único.

## TCP

Para executar o servidor TCP, os mesmos passos anteriores são necessários, porém, com a execução do arquivo `src/tcp/tcp_server.py`:

```
python3 src/tcp/tcp_server.py
```

E, para executar o cliente TCP, o arquivo `src/tcp/tcp_client.py`:

```
python3 src/tcp/tcp_client.py
```

## Testes

Para executar os testes, é necessário estar o servidor a ser testado em execução. Para isso, basta seguir os passos anteriores.

```bash
# Executar os testes do QUIC.
python3 tests/http3_random.py
```

```bash
# Executar os testes do TCP.
python3 tests/tcp_random.py
```

Com isso, será enviado uma quantidade de mensagens aleatórias para o servidor. Para um aumento na quantidade de mensagens, basta executar o mesmo comando em outra janela do terminal.
