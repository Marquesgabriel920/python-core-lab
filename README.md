# 🚀 Trilha Dev Junior 2026

Projeto de estudos progressivo para conquistar uma vaga de desenvolvedor Junior.
Crie um arquivo `.py` para cada desafio. Resolva sozinho antes de pedir ajuda.

---

## 🎯 O que um Dev Junior precisa saber

- [ ] Lógica de programação
- [ ] Estruturas de dados (listas, dicionários)
- [ ] Funções e modularização
- [ ] Orientação a Objetos (POO)
- [ ] Git e GitHub
- [ ] Consumir e criar APIs REST
- [ ] Banco de dados básico (SQL)
- [ ] Tratamento de erros

---

## 🧠 MÓDULO 1 — Lógica de Programação

> Fundação de tudo. Se errar aqui, vai errar em tudo.

- [x] **D01** — Leia um número e diga se é par ou ímpar *(já feito no day01.py)*
- [x] **D02** — Leia dois números e exiba o maior. Se forem iguais, informe isso.
- [x] **D03** — Leia 3 notas de um aluno e calcule a média. Exiba se foi aprovado (≥7), em recuperação (≥5 e <7) ou reprovado (<5).
- [x] **D04** — Exiba todos os números de 1 a 100 que sejam divisíveis por 3 ou por 5, mas não pelos dois ao mesmo tempo.
- [x] **D05** — Crie um jogo de adivinhar: o programa sorteia um número de 1 a 10 e o usuário tem 3 tentativas para acertar. Informe se errou pra cima ou pra baixo.
- [x] **D06** — Calcule o fatorial de um número digitado pelo usuário usando um loop (sem recursão).
- [x] **D07** — Verifique se um número é primo.
- [x] **D08** — Exiba os primeiros N termos da sequência de Fibonacci, onde N é digitado pelo usuário.

---

## 📦 MÓDULO 2 — Estruturas de Dados (Listas e Dicionários)

> Você vai usar isso em toda entrevista técnica.

**Listas**
- [x] **D09** — Crie uma lista com 5 números digitados pelo usuário. Exiba o maior, o menor e a média.
- [ ] **D10** — Leia uma lista de nomes e exiba em ordem alfabética.
- [ ] **D11** — Remova os valores duplicados de uma lista sem usar `set()`.
- [ ] **D12** — Dado uma lista de números, retorne uma nova lista apenas com os pares.
- [ ] **D13** — Implemente uma fila (FIFO): o usuário adiciona nomes e remove sempre o primeiro da fila.
- [ ] **D14** — Implemente uma pilha (LIFO): o usuário empilha e desempilha itens, sempre removendo o último.

**Dicionários**
- [ ] **D15** — Crie um dicionário representando um produto (nome, preço, estoque). Permita atualizar o estoque.
- [ ] **D16** — Leia uma frase e conte a frequência de cada palavra usando dicionário.
- [ ] **D17** — Crie uma agenda: adicionar contato, buscar por nome, listar todos, remover contato.
- [ ] **D18** — Dado uma lista de dicionários representando alunos (`nome`, `nota`), exiba os aprovados ordenados por nota.

---

## 🔧 MÓDULO 3 — Funções e Modularização

> Código sem funções não vai passar em code review.

- [ ] **D19** — Crie uma função `calcular_desconto(preco, percentual)` que retorna o preço final.
- [ ] **D20** — Crie uma função `validar_cpf(cpf)` que verifica se o CPF tem 11 dígitos numéricos (não precisa validar os dígitos verificadores).
- [ ] **D21** — Crie uma função `celsius_para_fahrenheit(c)` e outra `fahrenheit_para_celsius(f)`. Crie um menu para o usuário escolher a conversão.
- [ ] **D22** — Crie uma função `contar_vogais(texto)` e outra `contar_consoantes(texto)`. Use as duas em um programa que analisa uma frase.
- [ ] **D23** — Crie um módulo `matematica.py` com as funções `soma`, `subtracao`, `multiplicacao`, `divisao`. Importe e use em outro arquivo.
- [ ] **D24** — Crie uma função recursiva para calcular o fatorial (agora com recursão). Compare com a versão do D06.
- [ ] **D25** — Crie uma função que recebe uma lista de números e retorna `(maior, menor, media)` como tupla.

---

## 🚨 MÓDULO 4 — Tratamento de Erros

> Todo sistema quebra. Um Junior que trata erros se destaca.

- [ ] **D26** — Peça um número ao usuário. Trate o erro caso ele digite uma letra.
- [ ] **D27** — Tente abrir um arquivo que não existe e trate o erro com mensagem amigável.
- [ ] **D28** — Crie uma função `dividir(a, b)` que trata divisão por zero e retorna `None` com mensagem de erro.
- [ ] **D29** — Crie uma exceção personalizada chamada `SaldoInsuficienteError` e use em uma função `sacar(saldo, valor)`.
- [ ] **D30** — Crie um programa que lê um arquivo CSV simples (você cria o arquivo) e trata todos os possíveis erros: arquivo não encontrado, linha mal formatada, valor inválido.

---

## 🏗️ MÓDULO 5 — Orientação a Objetos (POO)

> Sem POO, você não passa da triagem em 90% das vagas.

- [ ] **D31** — Crie uma classe `Pessoa` com atributos `nome` e `idade` e um método `apresentar()`.
- [ ] **D32** — Crie uma classe `ContaBancaria` com `depositar()`, `sacar()` e `ver_saldo()`. O saldo não pode ficar negativo.
- [ ] **D33** — Crie uma classe `Animal` com método `falar()`. Crie subclasses `Cachorro` e `Gato` que sobrescrevem `falar()` com sons diferentes (herança + polimorfismo).
- [ ] **D34** — Refaça a `ContaBancaria` usando encapsulamento: saldo deve ser privado (`__saldo`) e acessível apenas por métodos.
- [ ] **D35** — Crie uma classe `Produto` e uma classe `Carrinho` que armazena produtos, calcula o total e aplica desconto.
- [ ] **D36** — Crie um sistema de cadastro de funcionários com classes: `Funcionario`, `Gerente` (herda de Funcionario com bônus), `Estagiario` (herda com carga horária). Liste todos com seus salários calculados.

---

## 🌐 MÓDULO 6 — Consumir e Criar APIs REST

> É o que separa quem "sabe Python" de quem "trabalha com Python".

**Consumir APIs (requests)**
- [ ] **D37** — Instale a lib `requests`. Faça uma requisição GET para `https://viacep.com.br/ws/01001000/json/` e exiba o endereço formatado.
- [ ] **D38** — Consuma a API pública `https://api.coindesk.com/v1/bpi/currentprice.json` e exiba o preço atual do Bitcoin em USD.
- [ ] **D39** — Consuma `https://jsonplaceholder.typicode.com/users` e exiba nome e email de cada usuário.
- [ ] **D40** — Faça uma requisição que pode falhar (timeout, 404). Trate todos os erros possíveis.

**Criar APIs (Flask)**
- [ ] **D41** — Instale o `Flask`. Crie uma rota GET `/` que retorna `{"status": "ok"}`.
- [ ] **D42** — Crie uma API com rota GET `/usuarios` que retorna uma lista de usuários em JSON.
- [ ] **D43** — Adicione uma rota POST `/usuarios` que recebe um JSON com `nome` e `email` e adiciona à lista.
- [ ] **D44** — Implemente o CRUD completo: GET (listar), GET por ID, POST (criar), PUT (atualizar), DELETE (remover). Use uma lista em memória como "banco de dados".
- [ ] **D45** — Adicione validação: retorne erro 400 se os campos obrigatórios não forem enviados.

---

## 🗄️ MÓDULO 7 — Banco de Dados (SQL)

> Toda aplicação real tem banco de dados.

- [ ] **D46** — Instale o `sqlite3` (já vem no Python). Crie um banco, uma tabela `usuarios` e insira 3 registros.
- [ ] **D47** — Faça um SELECT que filtra usuários por nome. Exiba os resultados formatados.
- [ ] **D48** — Implemente UPDATE para alterar o email de um usuário pelo ID.
- [ ] **D49** — Implemente DELETE para remover um usuário pelo ID.
- [ ] **D50** — Crie duas tabelas relacionadas: `usuarios` e `pedidos` (um usuário tem muitos pedidos). Faça um JOIN para listar os pedidos com o nome do usuário.
- [ ] **D51** — Integre o banco de dados com a API Flask do D44: substitua a lista em memória pelo SQLite.

---

## 🐙 MÓDULO 8 — Git e GitHub

> Sem Git, você não existe para o mercado.

- [ ] **G01** — Instale o Git. Rode `git init` neste projeto e faça o primeiro commit com todos os arquivos.
- [ ] **G02** — Crie uma conta no GitHub. Crie um repositório público chamado `trilha-dev-junior` e suba o projeto.
- [ ] **G03** — Crie uma branch chamada `feature/calculadora`, adicione um arquivo novo, faça commit e merge na main.
- [ ] **G04** — Escreva um `README.md` no GitHub explicando o projeto (o que é, como rodar, tecnologias usadas).
- [ ] **G05** — Simule um conflito: edite o mesmo arquivo em duas branches diferentes e resolva o conflito manualmente.

---

## 🏆 PROJETO FINAL — API Completa com Banco de Dados

> Se você chegar aqui e entregar isso, está pronto para entrevistas.

- [ ] **FINAL** — Construa uma API REST com Flask + SQLite para gerenciar uma lista de tarefas (To-Do List):
  - CRUD completo de tarefas (`id`, `titulo`, `descricao`, `status`, `criado_em`)
  - Filtrar tarefas por status (pendente / concluída)
  - Marcar tarefa como concluída via PATCH
  - Tratar todos os erros (404, 400, 500)
  - Código organizado em arquivos separados (modularização)
  - Projeto no GitHub com README explicando como rodar

---

## 💡 Regras da Trilha

1. Resolva cada desafio sozinho antes de pedir ajuda
2. Se travar por mais de 30 minutos, peça uma dica — não a solução
3. Suba cada desafio resolvido no GitHub (módulo 8 primeiro se quiser)
4. Ao terminar um módulo inteiro, marque o item correspondente no checklist do topo

---

*Consistência > Intensidade. Um desafio por dia já te leva longe.*

Registro do Dia 3: prática de branches, diff e merge.