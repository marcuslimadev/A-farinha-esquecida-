# INSTRUÇÕES MESTRAS — A FARINHA ESQUECIDA

Este arquivo é o ponto único de entrada operacional do projeto.

Quando o usuário disser algo como **“atualize o git e siga as instruções em instrucoes.md”**, execute este protocolo sem pedir que ele repita contexto já persistido.

## 1. Sincronize o Git com segurança

1. Confirme que está neste repositório.
2. Rode `git status --short`.
3. Rode `git fetch origin`.
4. Descubra a branch atual com `git branch --show-current`.
5. Se a árvore estiver limpa e a branch puder avançar em fast-forward, rode `git pull --ff-only`.
6. Se houver alterações locais, NUNCA use automaticamente `reset`, `checkout .`, `restore .`, `clean`, `stash` ou qualquer comando que descarte/oculte trabalho. Compare o que mudou localmente com o remoto e atualize somente se for seguro. Se houver conflito real, preserve o trabalho e registre o bloqueio em `AGENTS/PROJECT_STATE.md`.
7. Nunca force push.

## 2. Leia o mínimo necessário

Depois da sincronização leia, nesta ordem:

1. `AGENTS/PROJECT_STATE.md`
2. `AGENTS/OPERATING_RULES.md`
3. `AGENTS/DECISIONS.md` somente se a tarefa tocar uma decisão já registrada
4. a ficha e os locks estritamente necessários ao próximo asset

NÃO leia o repositório inteiro.
NÃO reconstrua o histórico do projeto.
NÃO reabra decisões aprovadas sem evidência de erro.

## 3. Modelo e subagentes

O coordenador operacional padrão deve ser **Luna / modelo não-Pro de menor custo disponível**.

Se a ferramenta `agents` estiver disponível:
- normalmente use até 2 workers Luna em paralelo;
- máximo 3 workers ativos;
- papéis lógicos: `CANON`, `LOCKS` e, depois, `QA`;
- reutilize worker sleeping quando o histórico dele for pequeno e relevante;
- crie worker novo quando o histórico antigo estiver grande ou irrelevante;
- use `reasoning_effort=low` por padrão e `medium` apenas quando necessário;
- não invente slug de modelo: use um modelo realmente disponível na conta.

Nunca crie worker Astra/Pro para trabalho rotineiro.
Nunca use Goal ou Loop por iniciativa própria.

## 4. Astra

Astra é excepcional, não operacional.

Só use Astra se `AGENTS/ASTRA_HANDOFF.md` contiver explicitamente:

`ASTRA_REQUIRED: SIM`

Se estiver executando como Astra e o arquivo disser `ASTRA_REQUIRED: NÃO`, não faça leitura ampla nem revisão geral. Encerre a atuação cara e deixe Luna continuar.

Astra serve somente para contradição canônica importante, decisão estrutural, conflito de locks sem solução clara ou falha persistente que Luna não conseguiu resolver.

## 5. Fluxo do próximo asset

1. Pegue `PROXIMA_ACAO` e `PROXIMO_ASSET` de `AGENTS/PROJECT_STATE.md`.
2. Leia apenas a ficha desse asset.
3. `CANON` verifica roteiro/cronologia/falas/personagens da cena.
4. `LOCKS` verifica referências faciais, fases, figurino, cenário e objetos recorrentes.
5. O coordenador monta/ajusta o prompt final sem reescrever o projeto inteiro.
6. Gere a imagem se a capacidade de geração estiver disponível. Se não estiver, marque `GERACAO_PENDENTE`; nunca finja que um arquivo foi gerado.
7. `QA` compara a imagem com a ficha e responde somente `APROVADO` ou `REPROVADO` + correção mínima.
8. Em reprovação, corrija apenas o erro apontado; preserve o que já está certo.
9. Salve na pasta da página com o nome canônico.
10. Atualize `AGENTS/PROJECT_STATE.md`.
11. Registre em `AGENTS/DECISIONS.md` apenas decisões duradouras novas.
12. Atualize `AGENTS/ASTRA_HANDOFF.md` somente se surgir exceção real.
13. Faça um commit lógico e descritivo e envie ao remoto se houver permissão.

## 6. Limite por execução

Por chamada curta do usuário, conclua no máximo:
- 1 página; ou
- 2 assets;

o que vier primeiro.

Depois pare com o estado persistido atualizado. Não continue em loop automático.

## 7. Regras editoriais essenciais

- O texto literário é protagonista; as imagens são cenas cinematográficas, não quadrinhos convencionais.
- Nunca inserir texto, letras, logos, balões ou numeração dentro das imagens geradas.
- A diagramação/tipografia é feita depois no Corel.
- Gerar cada asset para o espaço que ele realmente ocupará; não produzir imagem genérica para depois forçar corte.
- Respeitar proporção, sangria e área negativa previstas na ficha.
- Preservar identidade facial, idade/fase, figurino, cenário, época e objetos bloqueados.
- Amazônia brasileira vivida e digna: sem exotização turística, fantasia regional genérica ou animais decorativos inventados.
- Não tratar uma imagem como `APROVADA` apenas porque existe no Git.

## 8. Saída final de cada execução

Responda de forma curta:

`CONCLUIDO:`
`ESTADO:`
`PROXIMO:`
`ASTRA_REQUIRED: SIM|NAO`
`COMMIT:`

Não escreva ensaio nem recapitule o projeto inteiro.
