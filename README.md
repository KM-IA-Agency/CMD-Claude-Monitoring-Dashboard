# CMD — Claude Monitoring Dashboard (`cmdash`)

Module « Optimiser l'usage de Claude » : audit des transcripts Claude Code, grille
de prix éditable, garde-fou de contexte, vue contexte et vue mémoire avec actions
proposées, reprise de session en un clic, rollup OTLP générique.

**Principe non négociable : l'utilisateur garde la main.** Seuils, plafonds,
fenêtres et grille de prix vivent dans `~/.cmdash/settings.json` ; aucune action
automatique n'est activée par défaut ; une alerte propose, elle n'exécute pas.

État : amorçage (0.0.0). Le socle (lot 0), le produit autonome (lot 1A) et le
Cockpit AAP (lot 1B) sont pilotés par l'Epic « CMD V1 » du dépôt
`KM-IA-Agency/augmented-agent-platform` (`docs/proposals/cmd/`). Tout est en
français pour le moment ; version anglaise ultérieure.

## Installation (développement)

```bash
python -m pip install -e .[dev]
```

```bash
cmdash --version
```

## Règles du dépôt

- Aucun contenu de prompt ni de résultat d'outil capturé ; fixtures synthétiques.
- Aucun secret ni chemin personnel : `python scripts/check_personal_strings.py`.
- Métrique OU événement de coût, jamais la somme ; absence de donnée ≠ zéro.
- Un item = un commit = une PR de lot ; contrat de lot sous `.aap/task-contracts/`.

Licence : Apache-2.0.
