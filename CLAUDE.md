# Instructions Claude pour CMD

- Lire d'abord `README.md`, puis `docs/` ; la source d'autorité est l'Issue de
  lot dans `KM-IA-Agency/augmented-agent-platform` et le contrat
  `.aap/task-contracts/issue-<n>.json` (posé par Kamel, jamais modifié par la PR
  d'implémentation).
- Rester dans `allowed_paths` du contrat ; un commit par item ; jamais de merge,
  jamais de force-push, jamais de « Ready for review ».
- Avant commit : `python -m pytest -q`, `python -m ruff check cmdash tests`,
  `git diff --check`, `python scripts/check_personal_strings.py`.
- Aucune action automatique activée par défaut ; toute écriture dans
  `~/.claude/settings.json` passe par `cmdash install` avec sauvegarde.
- Tout en français (code commenté, docs, messages) ; version anglaise plus tard.
