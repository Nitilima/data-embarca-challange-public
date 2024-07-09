---

# Desafio AWS Step Functions com Serverless Framework e S3

Bem-vindo(a) ao desafio de orquestração de microserviços usando AWS Step Functions, Lambdas e S3. Aqui, você usará o Serverless Framework e Python para criar e gerenciar seus recursos AWS.

## Objetivo

O desafio envolve a criação de um fluxo orquestrado por uma *state machine* AWS Step Function, no qual:

1. **Lambda 1:** Esta função deve baixar um arquivo *csv* e salvar em um S3 Bucket.
2. **Lambda 2:** Esta função deve recuperar o *csv* salvo na *lambda* anterior, calcular uma métrica e salvá-la em um banco de dados relacional.

### Requisitos

1. **Lambda 1**:
   - Deve ser capaz de receber um *link* de arquivo como entrada. Os possíveis *links* encontram-se no `link.yml`.
   - Baixar o *csv* encontrado no *link* e salvá-lo em um S3 Bucket.
   - Transforme ou trate os dados conforme necessário.
   - Retorne as informações pertinentes para a segunda *lambda*.

2. **Lambda 2**:
   - Recebe as informações da primeira *lambda*.
   - Calcula o número de mortos em acidentes que envolveram os seguintes veículos: 'automovel', 'bicicleta', 'caminhao', 'moto' e 'onibus'.
   - Salve os dados em formato em uma tabela em um banco relacional.
   - Faça um retorno significativo para o usuário.

### Formato de Saída

Para a saída gerada pela segunda lambda, esperamos uma tabela que cumpra as seguintes especificações:

1. **Colunas**:
   - 'created_at', 'road_name', 'vehicle', 'number_deaths'

#### **Desenvolvimento**:

1. Escreva o código Python para ambas as lambdas seguindo os requisitos.
2. Fornceça um arquivo `serverless.yml`, contendo as informações para o *deploy* tanto dos recursos da *lambda*, quanto da Step Function.
3. Certifique-se de que todos os arquivos necessários, como Docker, estejam na sua entrega.

### Envio

1. Crie um novo repositório em sua conta GitHub.
2. Faça push do seu código para este repositório.
3. Envie o link do repositório para a equipe avaliadora.

## Critérios de Avaliação

1. **Código**: Qualidade, clareza e eficiência.
2. **Integração com S3**: As lambdas devem interagir corretamente com os recursos externos e devem executar o seu objetivo.
3. **Fluxo Orquestrado**: A state machine deve garantir a passagem correta de dados entre os Lambdas.
4. **Segurança**: As credenciais e variáveis de ambiente seguem as melhores práticas.
5. **Documentação**: Quaisquer suposições ou alterações feitas devem ser bem documentadas.

### Recursos

Não serão disponibilizados recursos de *cloud* para a execução deste desafio.

## Bônus de Avaliação

A implementação de um pipeline de integração contínua e entrega contínua (CI/CD) utilizando o GitHub Actions **não é obrigatória**, mas será considerada um extra positivo na avaliação. Se decidir implementar este aspecto, assegure-se de documentar o fluxo do pipeline, as ações tomadas em cada etapa e qualquer outro detalhe relevante que possa facilitar a compreensão e revisão do seu trabalho.

