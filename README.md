# Requisitos Funcionais

- [x] Deve ser possível cadastrar um agendamento
- [ ] Deve ser possível marcar uma data de retorno para o paciente
- [x] Deve ser possível visualizar todos os agendamentos cadastrados

# Regras de negócio

- [ ] Não deve ser possível cadastrar mais de 12 agendamentos pra MÉDICO em um turno (manhã, tarde ou noite)
- [ ] Não deve ser possível cadastrar mais de 8 agendamentos pra DENTISTA em um turno (manhã, tarde ou noite)
- [x] Não deve ser possível cadastrar um agendamento no sábado ou domingo
- [ ] Os pacientes devem ser atendidos por ordem de chagada(agendamento)

# Rodar projeto

## Criar agendamento

- `python3 main.py criar <documento> <telefone> <turno> <especialista>`

  - Turno: "MANHA", "TARDE" ou "NOITE"

## Listar todos os agendamentos

- `python3 main.py listar`
