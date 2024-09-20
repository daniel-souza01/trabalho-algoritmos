# Como rodar o projeto?

- Instale as dependências
- Garanta que o arquivo `src/db/db.json`, inicialmente, contenha apenas um array vazio: "[]". Caso contrário poderá ocorrer erros na manipulação do arquivo.

# Executar as funcionalidades

## Criar agendamento

- `python3 src/main.py criar <documento> <telefone> <turno> <especialista>`
  - Ex.: `python3 src/main.py criar 121321132 99999 MANHÃ MÉDICO`

## Listar todos os agendamentos

- `python3 src/main.py listar`

# O Projeto

## Requisitos Funcionais

- [x] Deve ser possível cadastrar um agendamento
- [x] Deve ser possível visualizar todos os agendamentos cadastrados

## Regras de negócio

- [x] Não deve ser possível cadastrar mais de 12 agendamentos pra MÉDICO em um turno (manhã, tarde ou noite)
- [x] Não deve ser possível cadastrar mais de 8 agendamentos pra DENTISTA em um turno (manhã, tarde ou noite)
- [x] Não deve ser possível cadastrar um agendamento no sábado ou domingo
