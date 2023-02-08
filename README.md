# HBM+ Api

Api simples para simular o padrão de batimentos cardíacos.
Para uma visualização mais clara dos dados enviados pelo websocket, clone e rode o repositório: https://github.com/ferdinandbr/hbm-front

## Tecnologias
- Python 3.7
- Fastapi
- Uvicorn

## Features
- Endpoint para receber inputs e devolver o valor calculado
- Possibilidade de definir quantas casas decimais o output terá
- Transmissão de eventos em realtime utilizando websocket

## Instalação

Clonar repositório e preparar o ambiente

```sh
git https://github.com/ferdinandbr/hbm-api.git

```

Criar e ativar virtualenv

```sh
cd hbm-api
python3 -m venv virtualenv
source virtualenv/bin/activate
```

Instalar dependências

```sh
pip install -r requirements/requirements.txt

```

Iniciar api:
```sh
 uvicorn main:app                            
```


## Rotas

| Rota | Método |
| ------ | ------ |
| /calculate/{time}/{accuracy} | GET |
| /ws | WS |


## Parametros

/calculate
| Parâmetro | Obrigatório | Tipo |
| ------ | ------ | ------ |
| time | sim | inteiro |
| accuracy | sim | inteiro 


# Respostas
/calculate
```sh
{'sucess': true, 'value' : int}

```

/ws
```sh
{'value': float, 'time': datetime}

```

## License

MIT
