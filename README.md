# case-elo

A ETL desse projeto foi desenvolvida em Python, pronta para deploy em uma ferramenta de orquestração como o Apache Airflow. A base de dados utilizada é um banco Postgres que subirá na mesma stack do Airflow, em um compose.


## Pré-requisitos
- Docker version 20.10.8
- docker-compose version 1.29.2, build 5becea4c
- Preferência por Ubuntu, mas pode ser qualquer distribuição Linux.

## Instruções de uso

1. Setup da stack Airflow + Postgres

O deploy da stack com o servidor Airflow e o banco Postgres é bem simples.
- Crie uma pasta "airflow";
- Mova o arquivo ```docker-compose.yml``` e ```init.sh``` para a pasta airflow;
- Crie os seguintes diretórios:
```mkdir -p ./dags ./logs ./plugins```
- Crie o .env do Airflow:
```echo -e "AIRFLOW_UID=$(id -u)" > .env```

- Baixe o arquivo docker-compose.yml para essa pasta;
- Execute o comando ```docker-compose up airflow-init```;
- Execute o comando ```docker-compose up -d```;
- Cheque se os containeres subiram corretamente com ```docker-compose ps```.

O usuário default do banco postgres é "postgres", com senha "processo-elo". Esse valor pode ser alterado no docker-compose.yml

Caso não haja erros, podemos prosseguir para a configuração inicial do airflow.

2. Configuração inicial do Airflow
É necessário apenas configurar a conexão com o banco Postgres.
- Acesse ```localhost:8080```;
- Insira o user "airflow" e a senha "airflow";
- Acesse a aba Admin > Connections;
- Insira uma nova conexão Postgres com nome "dw_elo", host "elo_db", usuário "postgres" e senha "processo-elo". Nota: o host "elo_db" é proveniente do networking interno do docker, mas estará disponível no localhost da máquina host;
- Teste a nova conexão e salve.

3. DAG e teste
Com tudo isso configurado, falta apenas inserir o script da DAG "gas" no Airflow:
- Mova o script "gas_dag.py" para airflow/dags;
- Mova a pasta "gas" para airflow/dags;
- Cheque a interface do Airflow, é para aparecer a nova DAG. Agora resta testar.

Com tudo isso feito, os dados deverão estar no banco Postgres, que é acessível através da url localhost:5431 (não é erro de digitação, é 5431 mesmo, de acordo com o setado no docker-compose.yml).
