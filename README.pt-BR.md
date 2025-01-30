<div align="center">
   <img height="30" width="40" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-ico.svg">
   <a href="./README.md">
      <img height="30" width="120" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-en.svg">
   </a>
   <a href="./README.ja.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-ja.svg">
   </a>
   <a href="./README.hi.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-hi.svg">
   </a>
   <a href="./README.pt-BR.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-pt-br.svg">
   </a>
</div>

# Mock CSV Generator

**Mock CSV Generator** é uma aplicação desktop, desenvolvida em Python e Tkinter, que permite criar arquivos CSV personalizados com base em configurações definidas pelo usuário. Ideal para gerar dados fictícios para testes e prototipagem.

![alt text](https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/sampling.png)

![alt text](https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/screenshot.png)

## Funcionalidades

1. **Geração de CSVs personalizados**:
   - Permite configurar colunas com cabeçalhos e valores personalizados.
   - Define o número de linhas a serem geradas.

2. **Gerenciamento de configurações**:
   - **Salvar Configurações**: Salva a configuração atual (cabeçalhos e valores das colunas) em um arquivo JSON.
   - **Carregar Configurações**: Carrega configurações previamente salvas de um arquivo JSON ou do módulo `DATA_CONFIG.py`.
   - **Limpar Configurações**: Restaura todas as colunas ao estado inicial.

3. **Interface gráfica amigável**:
   - Interface intuitiva usando Tkinter.
   - Suporte para até 8 colunas configuráveis.

## Como Funciona

1. **Configuração de Colunas**:
   - Adicione um cabeçalho para cada coluna.
   - Preencha os valores possíveis que cada coluna pode assumir.

2. **Geração de CSV**:
   - Insira o número de linhas desejado.
   - Clique em "Generate CSV" para gerar o arquivo `mokup-00.csv` na mesma pasta do programa.

3. **Gerenciamento de Configurações**:
   - Use o menu "Configuration" para salvar ou carregar suas configurações:
     - "Load from JSON" para carregar do arquivo JSON.
     - "Load from DATA_CONFIG.py" para carregar do módulo Python (se disponível).
     - "Save Configuration" para salvar a configuração atual.
     - "Clear All" para limpar todas as configurações.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.8 ou superior.
   - Bibliotecas padrão (`tkinter`, `json`, `csv`).

2. **Execução**:
   - Baixe o código.
   - Execute o arquivo `main.py`:
     ```bash
     python main.py
     ```

3. **Arquivos gerados**:
   - Configurações salvas serão armazenadas no arquivo `column_config.json`.
   - O arquivo CSV gerado será salvo como `mokup-00.csv`.

## Tecnologias Utilizadas

- **Python 3.13.1**: Lógica e backend.
- **Tkinter**: Interface gráfica simples e responsiva.

## Estrutura do Projeto

- `main.py`: Código principal da aplicação.
- `column_config.json`: (opcional) Armazena as configurações salvas pelo usuário.
- `DATA_CONFIG.py`: (opcional) Permite carregar configurações customizadas via módulo Python.

## Autor

- **Desenvolvedor**: Hipolito Rodrigues
- **Data de Criação**: 23/01/2025
- **Última Atualização**: 27/01/2025
- **Versão Atual**: 1.3.4

---

## Licença

Este projeto está sob a licença [CC0 1.0 Universal (Domínio Público)](https://creativecommons.org/publicdomain/zero/1.0/). Isso significa que você pode copiar, modificar, distribuir e executar o trabalho, mesmo para fins comerciais, tudo sem pedir permissão.
