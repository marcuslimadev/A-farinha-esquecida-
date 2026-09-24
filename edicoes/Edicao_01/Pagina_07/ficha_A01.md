# E01-P07-A01 — conversa sobre Manaus

Fonte: V17, capítulo I; `texto.txt` desta página, `MAPA_EDITORIAL.md`, `memoria.md` e locks de personagem/cenário. Proporção 3:2 horizontal. Cena única, sem montagem nem texto embutido.

## Sete personagens, sete referências individuais

Usar as imagens-base aprovadas nas fases indicadas pelas chaves M, J, L, R, F, T e P em `edicoes/Edicao_01/manifesto_producao.json`. Conferir cada rosto antes de gerar e no QA; prancha coletiva não substitui as referências individuais.

| Pessoa | Parentesco e fase | Leitura visual |
| --- | --- | --- |
| Miguel (M) | Filho de Rosária e Francisco; neto de Jesuína; 8–10 anos | Camiseta marrom; escuta |
| Jesuína (J) | Mãe de Rosária; avó de Miguel; idosa firme | Vestido marrom escuro; observa |
| Luzia (L) | Irmã mais nova de Jesuína; tia-avó de Miguel | Blusa marrom; gesto expressivo |
| Rosária (R) | Mãe de Miguel, Teresa e João Paulo; filha de Jesuína | Blusa azul; esperança contida |
| Francisco (F) | Pai dos três filhos; marido de Rosária | Camisa cinza de botões; pragmático |
| Teresa (T) | Irmã mais velha de Miguel; adolescente | Blusa vinho; atenta |
| João Paulo (P) | Irmão mais velho de Miguel; adolescente | Camiseta ocre; inquieto |

Rosária é inequivocamente a mãe das três crianças. Jesuína é a avó e Luzia, a tia-avó. Preservar rostos, idades e silhuetas distintos entre as três mulheres. Cada uma das sete pessoas aparece uma única vez, sem reflexos, duplicações ou figuras extras.

## Ação e espaço

Conversa familiar informal durante o dia na sala da casa de Jesuína, junto à mesa de madeira marcada pelo uso. Rosária fala da possibilidade de Manaus; Francisco responde com pragmatismo. Teresa e João Paulo reagem segundo seus interesses. Jesuína observa, Luzia participa com gesto natural e Miguel escuta. Olhares trocados e pequenas ações simultâneas. Sem reunião formal, documentos de apresentação, fila simétrica ou retrato posado.

Enquadramento aberto o suficiente para tornar os sete reconhecíveis, com silhuetas separadas, mãos coerentes e margem para corte. Leitura principal: Rosária falando, Francisco respondendo, Miguel ouvindo. Casa no estado `01_infancia_miguel` de `LOC-CASA-JESUINA-01`: tábuas escurecidas, vigas reconhecíveis, mesa gasta, passagem da sala à cozinha dos fundos, espaço funcional e habitado. Luz diurna lateral, realismo fotográfico cinematográfico.

## Prompt de geração

Create one 3:2 horizontal photorealistic cinematic literary-novel image inside Dona Jesuína's lived-in timber home in the Brazilian Amazon, natural daytime sidelight and a scarred wooden table. Use **each of the seven supplied individual approved character references exactly once**, preserving distinct face, age, skin, hair and clothing: child Miguel (brown tee) quietly listening; his mother Rosária (blue blouse) speaking with restrained hope about Manaus; his father Francisco (grey button shirt) responding practically; his older teenage sister Teresa (burgundy blouse) attentive; his older teenage brother João Paulo (ochre tee) lively; his grandmother Jesuína (simple dark brown dress) firm and observant; Jesuína's younger sister Luzia (brown blouse) expressive. Rosária is the children's mother; Jesuína their grandmother; Luzia their great-aunt. Ordinary informal family conversation with natural gestures and exchanged glances, never a formal meeting or posed family portrait. Exactly seven separate recognizable people, no duplicate faces or extras. Human eye-level medium-wide frame, separated silhouettes, realistic hands, safe crop margin. Same modest maintained house: dark timber, functional room leading toward rear kitchen. No text, letters, logos, captions, speech balloons, writing on documents, collage, fantasy, tourist styling or anyone looking at camera.

## QA para aprovação

1. Contar sete pessoas e identificar cada rosto por sua referência individual; reprovar ausências, duplicações ou fusões.
2. Confirmar Rosária como mãe distinta de Jesuína (avó) e Luzia (tia-avó), com fases e roupas coerentes.
3. Confirmar conversa doméstica informal, luz diurna, mesa e casa conforme o lock.
4. Conferir mãos, corpos, olhares, respiro de corte 3:2 e ausência de texto.
5. Só registrar `GERADO` com PNG salvo; `AUDITADO` e `APROVADO` exigem inspeção visual efetiva.
