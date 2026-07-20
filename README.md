# SUNWISE TALENTS — Équipe marketing multi-agents

Agents Claude qui produisent le contenu social media de **SUNWISE TALENTS**, intégrateur
Salesforce transcontinental et offshore (Villeneuve-le-Roi, Paris, Libreville).

Ce dépôt ne publie rien. Il prépare des livrables — veille, textes, visuels — qu'un humain
valide avant publication.

## Les trois agents

| # | Agent | Rôle | Déclencheurs typiques |
|---|---|---|---|
| 01 | [Research](agents/research-marketing/SKILL.md) | Veille sujets, analyse concurrentielle, sourcing de chiffres vérifiés | « idées de sujets », « que fait la concurrence » |
| 02 | [Copy](agents/copy-social/SKILL.md) | Rédaction LinkedIn / Instagram / X / Facebook, hooks, brief visuel | « écris un post », « décline sur Instagram » |
| 03 | [Visual](agents/visual-social/SKILL.md) | Carrousels, images de post, citations, infographies | « fais un visuel », « un carrousel » |

Chaque agent lit son propre `SKILL.md` en entier avant de travailler. Le detail du
fonctionnement, des règles absolues et de la chaîne de production est dans [CLAUDE.md](CLAUDE.md).

## Structure

```
shared/     Référentiel commun : ligne éditoriale, personas, brand kit, offres
agents/     Les trois agents (SKILL.md + références)
output/     Productions des agents — jamais une source de vérité
```

## Statut

Le corpus existant (11 posts, 7 visuels) a été jugé non reproductible en l'état ; ces agents
visent à relever le niveau, pas à industrialiser l'existant. Plusieurs données bloquantes
(autorisations clients, chiffres officiels, anecdotes de projet…) restent à fournir par la
direction — voir [CLAUDE.md § 8](CLAUDE.md#8-état-des-blocages).
