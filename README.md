# Sistema de Matrícula — versão monolítica

Exercício da aula *Estilos Arquiteturais II: Arquitetura em Camadas*.

Um arquivo só, funcionando. Nada aqui está errado do ponto de vista funcional:
interface de terminal, regras de negócio e acesso ao banco convivem no mesmo
módulo, e é isso que vocês vão resolver.

## Como rodar

Requer apenas Python 3.8+ (o `sqlite3` já vem na biblioteca padrão).

```
python matricula_monolito.py
```

O programa cria `escola.db` na pasta atual e semeia dois alunos e duas turmas:

| Aluno | id | Faltas |
|---|---|---|
| Ana Ribeiro | 42 | 1 |
| Bruno Lima | 43 | 4 |

| Turma | Código | Vagas |
|---|---|---|
| Engenharia de Software II | ES2 | 2 |
| Arquitetura de Software | AS1 | 0 |

Apague `escola.db` para voltar ao estado inicial.

### Roteiro de teste

Rode esta sequência antes de começar e anote as respostas do programa. Ao
terminar a refatoração, rode de novo: as respostas devem ser as mesmas.

1. `1` → `42, ES2`
2. `1` → `42, ES2` (de novo)
3. `1` → `43, ES2`
4. `1` → `42, AS1`
5. `2` → `42`
6. `3`

## A atividade

Separem o código em três camadas — apresentação, negócio e persistência — **sem
alterar o comportamento observável do programa**.

Antes de mover qualquer linha, leiam o arquivo inteiro e marquem, para cada
função, quais responsabilidades ela acumula.

### Entregas

1. Árvore de pastas e arquivos.
2. Tabela de imports permitidos: quem pode importar quem, e quem nunca importa quem.
3. Uma frase justificando cada decisão que gerou discussão no grupo.
4. A declaração de se as camadas ficaram fechadas ou abertas, e por quê.

### Tabela de imports

| Módulo | Pode importar | Nunca importa |
|---|---|---|
| | | |
| | | |
| | | |

### Perguntas para responder na apresentação

- Onde ficou a validação do formato do texto digitado? Por quê ali?
- A camada de negócio devolve texto pronto para exibir ou dados? Qual das duas
  opções o grupo escolheu, e o que isso custa?
- Se amanhã o sistema virasse uma API web, quantos arquivos precisariam mudar?

### Desafio extra

Se terminarem antes: troquem a persistência por um dicionário em memória **sem
alterar uma linha da camada de negócio**.
