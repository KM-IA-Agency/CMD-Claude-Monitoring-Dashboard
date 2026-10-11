# Contrats de lot (schéma `aap-dev-task-v0.1`)

Un contrat par lot, nommé `issue-<n>.json` où `<n>` est le numéro de l'Issue de
lot dans `KM-IA-Agency/augmented-agent-platform`. Le contrat est posé par Kamel
dans une PR de proposition séparée, après ouverture de la PR d'intégration
(`authorized_pr`). La PR d'implémentation ne modifie jamais son contrat. La CI
valide les contrats contre `schema.json` (`scripts/validate_contract_schema.py`).
