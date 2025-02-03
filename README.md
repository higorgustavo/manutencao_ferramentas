# Projeto Manutenção de Ferramentas

Um pequeno sistema desenvolvido para a equipe de técnicos de manutenão de ferramentas da Natal Home Center possam gerenciar os serviços realizados nas máquinas da Stihl.

### Instalando o projeto

#### Clonar o projeto
`get clone https://github.com/higorgustavo/manutencao_ferramentas`

#### Instalar dependências
`pip install -r requirements.txt`

#### Gerar as migrações
`python manage.py makemigrate`

#### Migrar Banco de Dados
`python manage.py migrate`

#### Iniciar servidor
`python manage.py runserver`
