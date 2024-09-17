## Terminal Hax-Elixir

**O Terminal Hax-Elixir é um terminal de comandos focado em automações e manipulação de dados. Ele suporta uma linguagem de script própria chamada Hax-Elixir para execução de comandos simplificados, como listagem de diretórios, cópia e movimentação de arquivos, e agendamento de tarefas.**

## Funcionalidades

**Manipulação de Arquivos: Crie, copie, mova, renomeie e delete arquivos e diretórios.**

**Execução de Comandos: Execute comandos do sistema diretamente do terminal.**

**Agendamento de Tarefas: Programe a execução de comandos em intervalos regulares de tempo.**

**Comandos Personalizados: Suporte para comandos personalizados definidos em um arquivo JSON externo.**


## Comandos Suportados

```mkdir |> {diretorio}```: **Cria um novo diretório.**

```cpy > {origem} < {destino}```: **Copia um arquivo de origem para o destino.**

```del | {arquivo}```: **Deleta um arquivo.**

```exe $ {comando}```: **Executa um comando do sistema.**

```ren > {origem} < {destino}```: **Renomeia um arquivo.**

```mov > {origem} < {destino}```: **Move um arquivo de origem para o destino.**

```cat > {saida} < {entrada1} {entrada2}```: **Concatena o conteúdo de vários arquivos em um arquivo de saída.**

```schd $ {intervalo} {comando}```: **Agenda um comando para ser executado em intervalos regulares de tempo.**


## Configuração

**1. Instalação de Dependências: Certifique-se de que o módulo schedule está instalado. Você pode instalá-lo usando:**

```pip install schedule```


**2. Arquivo de Comandos: O arquivo cmds.exs deve estar no mesmo diretório do script Python. Este arquivo contém comandos personalizados e suas descrições.**


**3. Executando o Terminal: Execute o script Python para iniciar o terminal**


## Exemplo de Uso

_**Para criar um diretório e agendar a listagem desse diretório a cada 10 segundos, você pode usar o seguinte código em Hax-Elixir**_

```
mkdir |> {teste_dir}
schd $ {10} {lst |> {teste_dir}}
```
**Contribuições**

**Sinta-se à vontade para contribuir com melhorias ou correções. Abra uma issue ou um pull request para discutir mudanças.**
