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

## Vérifications demandées avant mise en production

Ce qui suit n'est pas une nouvelle proposition : c'est un résumé, à l'usage de la direction,
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

Six formats détaillés dans
[`agents/copy-social/references/formats.md`](agents/copy-social/references/formats.md).
Chaque post doit correspondre à l'un d'eux ; les statuts ci-dessous reflètent les contraintes
bloquantes déjà documentées dans ce fichier.

| # | Format | Persona | Statut |
|---|---|---|---|
| F1 | Retour d'expérience | P1, P2 | 🔴 Bloqué — aucune anecdote projet collectée |
| F2 | Décryptage technique | P2 | ✅ Produisible immédiatement |
| F3 | Cas client anonymisé | P1, P3 | 🔴 Bloqué — aucune autorisation client |
| F4 | Chiffre / donnée | P1, P3 | 🟠 Dépend de la veille |
| F5 | Coulisses & équipe | P4 | 🟠 Bloqué en version photo |
| F6 | Engagement & RSE | P5, P4 | ✅ Produisible |

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

**Voie A — MCP Zernio.** Plateforme d'agrégation multi-réseaux, déjà connectée à notre
environnement Claude.

Avantages :

| Point | Détail |
|---|---|
| Disponible immédiatement | Le connecteur est déjà en place, aucun développement |
| Multi-plateformes | LinkedIn, Instagram, X, Facebook avec la même interface |
| Programmation native | Files d'attente, créneaux récurrents, publication différée |
| Recommandation de créneau | Outil intégré de meilleur moment de publication |
| Validation avant envoi | Vérification de longueur et de conformité |
| Analytics inclus | Alimente directement le futur agent 05 |
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

Inconvénients — c'est ici que le sujet se joue :

| Point | Détail |
|---|---|
| Délai d'accès | Le scope de publication sur page entreprise requiert un accès Marketing API, dont la revue prend typiquement de deux à quatre semaines — sans garantie d'acceptation |
| Le carrousel PDF n'est pas publiable | Les posts document, les carrousels PDF et les sondages ne sont pas supportés par l'API en 2026 |
| Pas de mention cliquable | L'API ne supporte pas les mentions dans le texte du post : écrire @NomEntreprise produit du texte simple, pas un lien |
| Gestion des jetons | Les jetons expirent au bout de 60 jours, il faut gérer le rafraîchissement |
| Plateforme restrictive | LinkedIn est la plateforme la plus restrictive en matière d'accès API : la plupart des endpoints demandent une approbation |
| Mono-plateforme | Il faudrait développer autant d'intégrations que de réseaux |
| Maintenance à notre charge | Chaque évolution de l'API est un chantier |

**Le point décisif : le carrousel PDF.** C'est l'élément qui doit orienter la décision, et il
est rarement anticipé. Les posts document permettent de garder le lecteur dans le fil
LinkedIn tout en délivrant un contenu multi-pages, ce qui explique que l'algorithme les
favorise. Chaque balayage compte dans le temps de lecture, une métrique que l'algorithme
pondère fortement dans sa décision de diffusion.

Le carrousel est le format le plus performant sur LinkedIn. Il n'est pas publiable par
l'API. Quelle que soit la voie retenue, ce format devra passer par une publication manuelle.
Cela réduit considérablement l'intérêt d'une automatisation complète.

**Notre recommandation : Voie A (Zernio) en phase 1**, pour trois raisons :

1. Le gain de l'API est marginal. Le carrousel — notre format le plus important — reste
   manuel dans les deux cas. L'API automatiserait les posts texte et image, soit une partie
   seulement du besoin.
2. Le délai est disqualifiant en phase de test. Attendre deux à quatre semaines une
   approbation pour valider une hypothèse éditoriale n'a pas de sens.
3. Le vrai enjeu n'est pas technique. Ce qui coûte du temps aujourd'hui, c'est produire un
   bon contenu, pas cliquer sur « publier ». Un humain qui copie-colle un post prend deux
   minutes.

Réévaluer en phase 3, si et seulement si :

- Le volume dépasse 15 posts par mois sur plusieurs plateformes
- Le coût de l'abonnement devient supérieur au coût de développement
- Un besoin apparaît que Zernio ne couvre pas

Dans tous les cas, nous recommandons de conserver la validation humaine avant publication.
Un post LinkedIn raté engage la marque publiquement et est irréversible. Le gain de temps
d'une publication automatique ne justifie pas ce risque.

### 5. Points complémentaires à arbitrer

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

**5.3 Les anecdotes de projet — 🔴 bloquant.** Le format F1 nécessite des situations réelles
vécues. Il n'en existe aucune au référentiel.
*Action* : recueillir auprès des consultants trois récits de projets ayant rencontré une
difficulté, avec ce qui en a été retiré. Anonymisation assurée ensuite.

**5.4 Les accords de droit à l'image — 🟠 haute.** Aucune photo d'équipe utilisable. Cela
bloque le format F5 en version photo et tout contenu de marque employeur illustré.
*Action* : faire signer les accords de droit à l'image aux collaborateurs volontaires.

**5.5 Les concurrents identifiés — 🟠 haute.** L'analyse concurrentielle de l'agent Research
reste théorique sans les noms des concurrents réellement rencontrés en appel d'offres.
*Action* : direction commerciale — les 5 concurrents les plus fréquents, et les motifs de
gain et de perte des derniers deals.

### 6. Une règle que nous te demandons de valider explicitement

Les agents sont configurés pour refuser certaines demandes, y compris lorsqu'elles viennent
de la direction :

- Les posts de circonstance (vœux, fêtes, journées internationales)
- Les posts nommant une personne en l'associant à un critère protégé
- L'ajout d'un logo tiers sur un visuel
- L'affichage de chiffres non sourcés

Ces refus sont volontaires. Ce sont des règles issues des fichiers de référence, et une
consigne donnée en conversation ne suffit pas à les lever : il faut modifier le fichier
concerné.

C'est ce qui distingue un agent qui fait progresser le niveau éditorial d'un agent qui
automatise les habitudes existantes. Si nous laissions une porte de sortie, l'ancienne
pratique reviendrait dès la première demande urgente.

Concrètement : en décembre, si quelqu'un demande un post de vœux, l'agent refusera et
proposera un bilan factuel de l'année à la place. C'est le comportement attendu, pas un
dysfonctionnement.

Si tu souhaites lever une de ces règles, la discussion doit porter sur la ligne éditoriale —
pas se régler post par post.

### Annexe

```
swt-marketing-team/
├── CLAUDE.md                      Point d'entrée du projet
├── shared/
│   ├── ligne-editoriale.md
│   ├── personas.md                ← à valider
│   ├── brand-kit.md
│   └── offres.md
└── agents/
    ├── research-marketing/        SKILL.md + sources + concurrents
    ├── copy-social/               SKILL.md + formats ← à valider + posts-valides
    └── visual-social/             SKILL.md + gabarits + exemples
```
