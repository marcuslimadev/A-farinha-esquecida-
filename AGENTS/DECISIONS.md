# DECISÕES

[D001]
ASSUNTO: Modelo operacional padrão
DECISAO: Usar Luna/modelo não-Pro disponível; Astra somente para exceções explicitamente marcadas.
MOTIVO: Reduzir consumo sem perder continuidade.
REABRIR_SE: Mudança de arquitetura ou incapacidade recorrente.

[D002]
ASSUNTO: Limite de contexto por asset
DECISAO: Ler apenas arquivos necessários ao asset atual.
MOTIVO: Evitar consumo e inconsistências.
REABRIR_SE: Problema real de continuidade exigir ampliação.

[D003]
ASSUNTO: Aprovação de imagens
DECISAO: PNG no Git não equivale a aprovação; todo asset requer QA explícito.
MOTIVO: Separar produção de validação.
REABRIR_SE: Fluxo editorial formalmente alterado.

[D004]
ASSUNTO: Primeiro asset pendente
DECISAO: Continuar por E01-P07-A01, proporção 3:2 e sete pessoas.
MOTIVO: Páginas 01–06 possuem imagens; P07 é a primeira lacuna.
REABRIR_SE: Auditoria identificar ausência, reprovação ou ordem diferente.

