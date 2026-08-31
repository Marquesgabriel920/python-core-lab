# Python Core Lab

Laboratório prático de estudos em Python, lógica, testes e Git.

## Objetivo

Este projeto foi criado para consolidar meus estudos práticos em Python e desenvolver minha capacidade de resolver problemas com código.

Ao longo do projeto, são praticados conceitos como lógica de programação, listas, dicionários, conjuntos, funções, manipulação de arquivos JSON, tratamento de erros, testes com `assert` e análise de complexidade de algoritmos.

O projeto também registra minha evolução na organização de código e no uso do Git, servindo como evidência prática do meu aprendizado para futuras oportunidades profissionais.

## Configuração do ambiente

A partir da raiz do projeto, execute no PowerShell:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python --version
python -m pip --version
```

Com o ambiente ativo, execute os desafios e os testes conforme as instruções deste README.

## Estrutura do projeto

- `challenges/`: desafios práticos de Python e lógica de programação.
- `tests/`: testes utilizados para verificar os resultados do código.
- `docs/`: registros de complexidade e documentação técnica.
- `data/`: arquivos JSON utilizados como dados de apoio nos desafios.

## Como executar

Com o ambiente virtual ativado e a partir da raiz do projeto:

```powershell
python .\challenges\desafio_18.py

```

## Executar os testes

```powershell
python -m tests.testes_valor_final
```

## Status

O projeto está em construção e atualmente possui 19 desafios, testes automatizados básicos, documentação de complexidade e organização em pastas.

Próximos passos:

- ampliar a quantidade de desafios;
- adicionar mais testes;
- configurar `pytest`;
- publicar o projeto no GitHub.