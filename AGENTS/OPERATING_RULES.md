# REGRAS OPERACIONAIS

- Produzir no máximo 1 página ou 2 assets por turno.
- Fluxo: roteiro V17 -> ficha -> locks -> prompt -> geração -> QA.
- Ler somente arquivos necessários ao asset atual.
- Papéis: PRIME, CANON, LOCKS e QA; PROMPT apenas quando necessário.
- Workers Luna/modelo não-Pro, low por padrão; máximo 3, normalmente 2.
- Astra só quando ASTRA_HANDOFF.md disser ASTRA_REQUIRED: SIM.
- Não habilitar Goal ou Loop.
- Não executar ações destrutivas de Git nem sobrescrever terceiros.
- Estados: PLANEJADO -> PROMPT_PRONTO -> GERADO -> AUDITADO -> APROVADO.
- Antes de commit: verificar status e diff; nunca reset, clean, restore ou force push automaticamente.

