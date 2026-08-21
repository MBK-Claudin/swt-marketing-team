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

Chaque agent tient aussi un **journal de décisions** (`agents/<agent>/decisions.md`) : les
corrections humaines apportées à ses productions y sont tracées automatiquement, et
peuvent être promues en règle dure par un humain — un apprentissage doux et réversible, lu
par l'agent à chaque démarrage. L'agent Copy sait en plus produire un **lot de 2 à 8 posts**
en une seule session (« les posts de la semaine », « une campagne ») via
[`workflows/campagne-lot.md`](workflows/campagne-lot.md), sans alléger aucune règle de fond.

## Structure

```
shared/     Référentiel commun : ligne éditoriale, personas, brand kit, offres, retours d'expérience
agents/     Les trois agents (SKILL.md + références + journal de décisions)
workflows/  Orchestrations multi-posts (campagne en lot pour l'agent Copy)
output/     Productions des agents — jamais une source de vérité
```

## Statut

Le corpus existant (11 posts, 7 visuels) a été jugé non reproductible en l'état ; ces agents
visent à relever le niveau, pas à industrialiser l'existant. Plusieurs données bloquantes
(autorisations clients, chiffres officiels, liste des concurrents…) restent à fournir par la
direction — voir [CLAUDE.md § 8](CLAUDE.md#8-état-des-blocages). Les anecdotes de projet, elles,
ne bloquent plus : `shared/retours-experience.md` fournit depuis le 7 août 2026 une matière
anonymisée qui débloque le format F1.

## Vérifications demandées

Ce qui suit n'est pas une nouvelle proposition : c'est un résumé,
de ce qui est déjà configuré dans les agents et qui reste marqué « à valider » ou bloquant
dans les fichiers de référence. Les tableaux ci-dessous sont la copie exacte de ce qui est
déjà en place — l'objectif est de faire vérifier et trancher ces points, pas de les
redéfinir ici.

### 1. Les personas — à valider

Cinq cibles définies à partir du positionnement de l'entreprise, détaillées dans
[`shared/personas.md`](shared/personas.md). La répartition proposée (30/30/15/15/10 %)
détermine 60 % du calendrier éditorial — voir la section « À faire valider » de ce fichier.

| # | Persona | Qui | Objectif |
|---|---|---|---|
| P1 | Décideur transformation | DSI, Directeur Digital, DG de PME/ETI | Générer des leads |
| P2 | Responsable CRM opérationnel | Head of CRM, Admin Salesforce, RevOps | Crédibilité technique |
| P3 | Directeur commercial / marketing | CCO, CMO, Directeur relation client | Sensibiliser sur l'expérience client |
| P4 | Talent tech | Consultant/Dev Salesforce, profils en reconversion | Recrutement |
| P5 | Écosystème & partenaires | Partenaires Salesforce, ESN, associations | Réseau et notoriété |

### 2. Les formats de post — à valider

Sept formats détaillés dans
[`agents/copy-social/references/formats.md`](agents/copy-social/references/formats.md).
Chaque post doit correspondre à l'un d'eux ; les statuts ci-dessous reflètent les contraintes
bloquantes déjà documentées dans ce fichier.

| # | Format | Persona | Statut |
|---|---|---|---|
| F1 | Retour d'expérience | P1, P2 | ✅ Produisible — matière anonymisée dans `shared/retours-experience.md` |
| F2 | Décryptage technique | P2 | ✅ Produisible immédiatement |
| F3 | Cas client anonymisé | P1, P3 | 🔴 Bloqué en nominatif — anonymisation stricte possible, relecture direction obligatoire |
| F4 | Chiffre / donnée | P1, P3 | 🟠 Dépend de la veille |
| F5 | Coulisses & équipe | P4 | 🟠 Bloqué en version photo |
| F6 | Engagement & RSE | P5, P4 | ✅ Produisible |
| F7 | Circonstance & moments d'équipe | P4, P5 | ✅ Produisible sous conditions — substance + 2/mois max (voir § 6) |

### 3. Recommandation — génération des visuels

**Le constat.** Les agents Claude produisent du vectoriel (SVG, HTML, PNG graphique). C'est
excellent pour les carrousels, les citations, les chiffres, les infographies et les schémas —
soit l'essentiel de nos besoins. Ils ne produisent pas de photographie. Or trois de nos six
gabarits en nécessitent une.

**La recommandation.** Ajouter un MCP de génération d'image à la chaîne, pour l'agent 03
Visual. Option : Nano Banana Pro (Google Gemini 3 Pro Image), disponible sous forme de
serveur MCP.

### 4. Recommandation — publication (agent 04)

C'est la décision la plus structurante pour la suite. Deux voies possibles.

**Voie A — MCP Zernio.** Plateforme d'agrégation multi-réseaux: https://zernio.com/.

Avantages :

| Point | Détail |
|---|---|
| Disponible immédiatement | Le connecteur est déjà en place, aucun développement |
| Multi-plateformes | LinkedIn, Instagram, X, Facebook avec la même interface |
| Programmation native | Files d'attente, créneaux récurrents, publication différée |
| Recommandation de créneau | Outil intégré de meilleur moment de publication |
| Validation avant envoi | Vérification de longueur et de conformité |
| Modération | Gestion des commentaires et mentions |
| Aucun processus d'approbation | Pas de dossier à déposer, pas d'attente |

Inconvénients :

| Point | Détail |
|---|---|
| Dépendance à un tiers | Notre chaîne de publication repose sur un prestataire externe |
| Coût récurrent | Abonnement à la plateforme |
| Données transitant par un tiers | À vérifier au regard du RGPD |
| Fonctionnalités bornées | Nous sommes limités à ce que l'outil expose |
| Risque de discontinuité | Si le service ferme ou change ses tarifs, il faut tout refaire |

**Voie B — API LinkedIn en direct.** Développement d'une intégration propre avec l'API
officielle.

Avantages :

| Point | Détail |
|---|---|
| Maîtrise complète | Aucun intermédiaire entre nous et LinkedIn |
| Pas d'abonnement tiers | Seul le coût de développement et de maintenance |
| Souveraineté des données | Rien ne transite par un prestataire |
| Capitalisation interne | Compétence d'intégration acquise et réutilisable |

Inconvénients:

| Point | Détail |
|---|---|
| Délai d'accès | Le scope de publication sur page entreprise requiert un accès Marketing API, dont la revue prend typiquement de deux à quatre semaines — sans garantie d'acceptation |
| Le carrousel PDF n'est pas publiable | Les posts document, les carrousels PDF et les sondages ne sont pas supportés par l'API en 2026 |
| Pas de mention cliquable | L'API ne supporte pas les mentions dans le texte du post : écrire @NomEntreprise produit du texte simple, pas un lien |
| Gestion des jetons | Les jetons expirent au bout de 60 jours, il faut gérer le rafraîchissement |
| Plateforme restrictive | LinkedIn est la plateforme la plus restrictive en matière d'accès API : la plupart des endpoints demandent une approbation |
| Mono-plateforme | Il faudrait développer autant d'intégrations que de réseaux |
| Maintenance à notre charge | Chaque évolution de l'API est un chantier |



### 5. Points complémentaires à arbitrer (le but étant de rendre l'agent plus performant)

**5.1 Les clients citables — 🔴 bloquant.** Aucun client n'a donné d'autorisation écrite.
Conséquence directe : aucun cas client publiable, alors que c'est le format qui convertit le
mieux auprès de P1.
*Action* : identifier 2 ou 3 clients susceptibles d'accepter, et obtenir un accord écrit
précisant ce qui peut être dit.

**5.2 Les chiffres officiels — 🔴 bloquant.** Aucun chiffre sur l'entreprise n'est
disponible : nombre de collaborateurs, de clients, de projets livrés, taux de satisfaction,
montant reversé aux associations. Les agents sont configurés pour refuser d'inventer un
chiffre, y compris quand l'utilisateur leur en fournit un qui n'est pas au référentiel. C'est
une garantie voulue, mais elle rend le contenu déclaratif tant que ces données manquent.
*Action* : valider une liste de chiffres communicables.

**5.3 Les anecdotes de projet — ✅ résolu le 7 août 2026.** `shared/retours-experience.md`
fournit désormais des retours d'expérience projet anonymisés (secteur + profil, sans nom),
ce qui débloque le format F1 et alimente F3 en version anonymisée. Reste distinct de 5.1 :
faire passer un de ces projets en cas client **nominatif** exige toujours un accord écrit du
client (`offres.md` § 8).

**5.4 Les accords de droit à l'image — 🟠 haute.** Aucune photo d'équipe utilisable. Cela
bloque le format F5 en version photo et tout contenu de marque employeur illustré.
*Action* : faire signer les accords de droit à l'image aux collaborateurs volontaires.

**5.5 Les concurrents identifiés — 🟠 haute.** L'analyse concurrentielle de l'agent Research
reste théorique sans les noms des concurrents réellement rencontrés en appel d'offres.
*Action* : direction commerciale — les 5 concurrents les plus fréquents, et les motifs de
gain et de perte des derniers deals.

### 6. Une règle déjà tranchée — posts de circonstance sous conditions

Jusqu'au 7 août 2026, les agents refusaient catégoriquement tout post de circonstance. **La
direction a depuis tranché** (voir `shared/ligne-editoriale.md` § 5 bis et
[CLAUDE.md règle 5](CLAUDE.md#5-les-règles-absolues)) : ce refus est levé, remplacé par une
règle à deux cas.

- **Cas A — autorisé sous deux conditions.** Vœux, fêtes de fin d'année, fête du travail,
  moments d'équipe génériques : substance obligatoire (ancrage sur un fait ou un bilan,
  jamais un vœu creux) **et** quota de 2 posts de circonstance par mois maximum.
- **Cas B — refus maintenu.** Fêtes ou journées liées à un critère protégé (religion,
  genre, origine, handicap…) dès qu'elles conduisent à nommer ou rendre identifiable une
  personne sur ce critère. Cette protection n'est pas assouplie.

Ce qui n'a pas bougé — les agents continuent de refuser, y compris sur consigne de la
direction :

- Les posts nommant une personne en l'associant à un critère protégé (cas B ci-dessus)
- L'ajout d'un logo tiers sur un visuel
- L'affichage de chiffres non sourcés

Ces refus restent volontaires. Ce sont des règles issues des fichiers de référence, et une
consigne donnée en conversation ne suffit pas à les lever : il faut modifier le fichier
concerné.

Concrètement : en décembre, si quelqu'un demande un post de vœux, l'agent ne le refuse plus
par principe — il le rédige avec un ancrage concret (bilan factuel de l'année) et signale
s'il pense que le quota mensuel est déjà atteint. C'est le comportement attendu depuis la
décision du 7 août 2026, pas un relâchement de la ligne éditoriale.

Si tu souhaites ajuster l'une de ces règles, la discussion doit porter sur la ligne
éditoriale — pas se régler post par post.

## Déploiement

Aujourd'hui les agents tournent via Claude Code, en local, dans ce dépôt. Pour qu'une
personne non technique puisse les utiliser, deux options selon le plan claude.ai
de l'organisation. Les `SKILL.md` ont déjà le frontmatter `name` / `description` attendu par
les Skills personnalisées — pas de reformatage de contenu nécessaire.

### Option A — Team/Enterprise : Skills personnalisées

1. Un admin du workspace active les Skills personnalisées (Settings → Capabilities).
2. Chaque dossier d'agent (`agents/research-marketing/`, `agents/copy-social/`,
   `agents/visual-social/`) est packagé en zip avec son `SKILL.md`, son dossier
   `references/`, `decisions.md`, **et** l'ensemble de `shared/` — les Skills n'ont pas de
   dossier commun entre elles, donc `shared/` doit être dupliqué dans chaque zip. Le zip de
   `copy-social/` embarque en plus `workflows/campagne-lot.md`, sans quoi le mode lot casse
   une fois packagé.
3. L'admin upload les trois zips (Settings → Capabilities → Skills → Upload) et les active
   pour le groupe/les utilisateurs marketing.
4. Usage : chat normal sur claude.ai — le bon agent s'active tout seul selon la demande,
   grâce à sa `description`.

### Option B — Pro : Projets

1. Créer trois Projets distincts (pas un seul pour les trois agents, sinon le routage entre
   eux devient flou pour Claude) : *SWT — Research*, *SWT — Copy*, *SWT — Visual*.
2. Dans chaque Projet, ajouter en connaissances le `SKILL.md` de l'agent, son
   `references/`, et l'ensemble de `shared/`.
3. Instructions personnalisées du Projet : demander à Claude de lire entièrement son
   `SKILL.md` et les fichiers de `shared/` avant de répondre, et d'appliquer les règles
   absolues à la lettre.
4. Usage : le marketing ouvre le bon Projet et chatte normalement.

### Point commun aux deux options

Ni claude.ai ni un Projet n'a accès au système de fichiers ou à Git : la sortie arrive en
message de chat, pas dans `output/`. Il faut soit qu'une personne copie-colle le livrable
dans le dépôt, soit accepter que `output/` ne soit alimenté que depuis Claude Code — à
trancher selon qui doit rester la source de vérité.

### Annexe

```
swt-marketing-team/
├── CLAUDE.md                      Point d'entrée du projet
├── shared/
│   ├── ligne-editoriale.md
│   ├── personas.md                ← à valider
│   ├── brand-kit.md
│   ├── offres.md
│   └── retours-experience.md      Matière anonymisée F1/F3, depuis le 7 août 2026
├── agents/
│   ├── research-marketing/       SKILL.md + decisions.md + sources + concurrents
│   ├── copy-social/               SKILL.md + decisions.md + formats ← à valider + posts-valides
│   └── visual-social/             SKILL.md + decisions.md + gabarits + exemples
└── workflows/
    └── campagne-lot.md            Orchestration d'un lot de posts pour l'agent Copy
```
