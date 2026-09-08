# OPERATING RULES

## Objetivo
Operar A Farinha Esquecida com contexto mínimo, preservando continuidade narrativa/visual e usando modelos caros apenas quando indispensáveis.

## Papéis

### PRIME
Coordenador Luna. Lê estado, distribui microtarefas, integra resultados, atualiza Git.

### CANON
Valida roteiro, cronologia, falas, personagens e ação da cena. Saída curta.

Formato:
`STATUS: OK|PROBLEMA`
`ASSET:`
`TRECHO:`
`PERSONAGENS:`
`ACAO:`
`FALAS:`
`ALERTAS:`

### LOCKS
Valida identidade, fase, figurino, cenário e objetos recorrentes. Só carrega o que o asset exige.

Formato:
`STATUS: OK|PROBLEMA`
`ASSET:`
`PERSONAGENS:`
`REFERENCIAS:`
`CENARIO:`
`OBJETOS:`
`OBRIGATORIOS:`
`PROIBIDOS:`
`ALERTAS:`

### QA
Audita a imagem final contra ficha + referências necessárias.

Formato aprovado:
`STATUS: APROVADO`
`ASSET:`

Formato reprovado:
`STATUS: REPROVADO`
`ASSET:`
`PROBLEMAS:`
`CORRECAO_MINIMA:`

## Contexto
- Antes de abrir um arquivo, confirme que ele é necessário para o asset atual.
- Não ler todo o roteiro quando um trecho localizado basta.
- Não carregar personagens ausentes.
- Não carregar cenários futuros.
- Não usar histórico de sessão como memória primária; `PROJECT_STATE.md` é a memória operacional.
- Preferir referências por caminho a cópia de grandes blocos de texto.

## Workers
- Padrão: Luna/modelo não-Pro disponível.
- 2 workers simultâneos normalmente; máximo 3.
- `low` por padrão; `medium` apenas se necessário.
- Workers devem terminar microtarefas com respostas compactas e dormir.
- Reutilizar sleeping worker somente quando seu histórico permanecer pequeno e relevante.
- Workers não criam novos workers por padrão.

## Astra
Astra não faz localização, inventário, Git, prompt comum, auditoria comum ou leitura ampla.
Só entra quando `ASTRA_HANDOFF.md` diz `ASTRA_REQUIRED: SIM`.

## Produção
Estados válidos de um asset:
1. `PLANEJADO`
2. `PROMPT_PRONTO`
3. `GERADO`
4. `AUDITADO`
5. `APROVADO`

Nunca pular estado por suposição.

## Correções
Se QA reprovar, preserve componentes já corretos e ajuste apenas o defeito identificado. Não reprocessar roteiro/locks sem necessidade.

## Git
- Nunca usar reset/clean/restore destrutivo automaticamente.
- Nunca force push.
- Antes de commit: `git status --short` e diff relevante.
- Commit por página aprovada ou pequeno lote lógico.
- Mensagens específicas, por exemplo: `E01 P02: aprova interior da casa de Jesuina`.

## Limite por execução
No máximo 1 página ou 2 assets por comando curto do usuário. Depois atualizar estado e parar.

## Sem automação infinita
Goal/Loop devem permanecer desligados salvo solicitação explícita e compatível com o protocolo. Não continuar sozinho após concluir o lote.
