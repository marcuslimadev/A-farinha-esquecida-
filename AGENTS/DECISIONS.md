# DECISIONS

Este arquivo registra somente decisões duradouras que não devem ser reprocessadas a cada execução.

[D001]
ASSUNTO: Modelo operacional padrão
DECISAO: Usar Luna/modelo não-Pro disponível como coordenador e workers para tarefas operacionais; Astra somente para exceções explicitamente marcadas em `AGENTS/ASTRA_HANDOFF.md`.
MOTIVO: Reduzir consumo de modelos caros sem perder continuidade.
REABRIR_SE: A disponibilidade/arquitetura de modelos mudar ou Luna demonstrar incapacidade recorrente em tarefa essencial.

[D002]
ASSUNTO: Limite de contexto por asset
DECISAO: Ler apenas ficha, trecho canônico, personagens, cenário e objetos necessários ao asset atual; é proibida leitura ampla do repositório por padrão.
MOTIVO: Evitar consumo repetitivo de contexto e inconsistências por excesso de informação.
REABRIR_SE: Um problema real de continuidade exigir ampliar o contexto.

[D003]
ASSUNTO: Aprovação de imagens
DECISAO: A existência de PNG no Git não equivale a aprovação. Todo asset gerado precisa passar por QA explícito contra ficha e locks.
MOTIVO: Separar produção de validação e evitar consolidar inconsistências visuais.
REABRIR_SE: Nunca por conveniência; apenas se o fluxo editorial for formalmente alterado.

[D004]
ASSUNTO: Automação contínua
DECISAO: Goal/Loop não são habilitados por padrão. Cada comando curto do usuário conclui no máximo 1 página ou 2 assets e para com estado persistido atualizado.
MOTIVO: Evitar consumo descontrolado e manter supervisão sobre custo/progresso.
REABRIR_SE: O usuário pedir explicitamente um modo contínuo e houver limites seguros definidos.

[D005]
ASSUNTO: Diagramação
DECISAO: Texto, tipografia e composição final serão feitos posteriormente no Corel; imagens não devem conter texto gerado por IA e devem ser produzidas especificamente para seus slots editoriais.
MOTIVO: Preservar qualidade profissional e evitar forçar imagens genéricas na diagramação.
REABRIR_SE: O processo editorial for formalmente alterado pelo usuário.
