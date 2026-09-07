# Estrutura de produção

As páginas são recipientes editoriais. O roteiro decide quantas imagens cada página ou dupla exige. Não reutilizar/cortar imagens apenas para fazê-las caber.

Ordem obrigatória: roteiro V17 -> stylesheet/continuity locks -> planejamento da página/dupla -> dimensões e proporções dos quadros -> geração específica dos assets -> texto.txt -> diagramação posterior no Corel.

## Organização dos personagens

Cada personagem deve conter:

- `descricao.md`: cânone narrativo e lock visual.
- `fases/<fase>/candidatos/`: gerações ainda não aprovadas.
- `fases/<fase>/aprovadas/`: imagens-base validadas pelo autor.
- `referencias/`: material auxiliar que não é imagem-base de uma fase.

Uma imagem só pode sair de `candidatos/` e entrar em `aprovadas/` após aprovação explícita. A ausência de arquivo em `aprovadas/` significa que o lock daquela fase ainda não foi concluído.

Consulte `INVENTARIO_ASSETS.md` para o estado auditado de todos os personagens.
