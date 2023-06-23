# AIO-CHAT - A QUIC CHAT APP

Implementação de um chat simples utilizando o protocolo QUIC. Este projeto foi baseado no repositório [aioquic](https://github.com/aiortc/aioquic), que é uma implementação do protocolo QUIC em Python.

## Pré-requisitos

- Python >=3.7
- Pipenv >=2023.6.18

## Como usar

Para executar o servidor, primeiro é necessário instalar as dependências do projeto:

Entre no ambiente virtual e instale as dependências:

```
$ pipenv shell
$ pipenv install
```

Com isso, será possível executar o servidor:

```
python http3_server.py \
  --certificate certificates/ssl_cert.pem \
  --private-key certificates/ssl_key.pem
```

Após iniciar o servidor, é possível executar uma ou mais instâncias do cliente:

```
python http3_client.py \
  --print-response \
  --ca-certs certificates/pycacert.pem \
  --username test \
  wss://localhost:4433/ws
```

- O parâmetro `--username` é opcional e, caso não seja informado, o cliente será identificado como `anonymous-*`, sendo `*` um `id` único.
