---
name: research-decisions
description: Journal des décisions de tri humaines sur les propositions de l'agent Research. Capture automatique, promotion en règle manuelle. Lu par Research au démarrage pour affiner son filtrage des sujets.
sources: [chat]
---

# Journal des décisions — agent Research

> **La trace est automatique. La promotion en règle est humaine.**

Ce fichier trace les **décisions de tri éditorial** de l'humain sur les
propositions de l'agent Research : quels sujets il garde, lesquels il écarte,
quels rattachements persona/territoire il corrige, quels chiffres il rejette,
quels angles il préfère. C'est ce qui apprend à l'agent à mieux **filtrer en
amont**. Contrairement aux journaux de Copy et Visual, il capte surtout des
décisions de tri, pas des réécritures.

**Règles du journal — à respecter sans exception :**

- **C'est une mémoire de travail, pas une source de vérité.** La vérité reste
  dans `SKILL.md`, `references/research-sources.md` et les fichiers `shared/`.
  En cas de contradiction entre ce journal et le SKILL, **le SKILL prime
  toujours**.
- **L'agent lit ce fichier au démarrage.** Les écarts récurrents encore non
  promus l'informent (« la dernière fois, l'humain a écarté les sujets de veille
  généralistes ») et l'aident à filtrer plus juste — **sans que ces écarts
  soient des règles gravées**.
- **L'agent n'ajoute JAMAIS une entrée pour se complimenter.** Une entrée naît
  uniquement quand un humain **décide réellement** sur une proposition (écarte,
  corrige, rejette, réoriente), ou demande explicitement de tracer une décision.
  Un livrable accepté tel quel ne génère aucune entrée.
- **La promotion d'un écart récurrent en règle est un acte humain délibéré.**
  Elle se fait lors du rituel de synthèse (voir la fin de ce fichier). L'agent
  ne promeut rien, ne modifie jamais le SKILL, ne change jamais un statut, ne
  supprime jamais d'entrée.

**Ce journal est qualitatif** (décisions de tri humaines). Il ne remplace pas la
boucle Analytics quantitative de `agents/copy-social/references/posts-valides.md`
(quels posts publiés performent). Deux sources distinctes, à ne pas confondre.

---

## Format d'une entrée

```markdown
### [AAAA-MM-JJ] — [mission : veille / concurrence / sourcing / signaux] — [sujet ou lot concerné]

- **Proposé par l'agent** : [le sujet, l'angle, le chiffre ou le rattachement proposé]
- **Décidé par l'humain** : [gardé / écarté / corrigé en…]
- **Nature de l'écart** : [une seule catégorie de la taxonomie Research ci-dessous]
- **Raison** : [pourquoi, si donnée — sinon « non précisée »]
- **Récurrence** : [1re fois / déjà vu N fois — compte les occurrences de la même nature d'écart]
- **Statut** : non promu
```

Une entrée porte **une seule** nature principale. Si une décision touche
plusieurs aspects, choisir le plus significatif et mentionner les autres dans la
raison.

---

## Taxonomie des écarts

Liste **fermée**. Toute entrée utilise exactement une de ces natures. Cette
liste doit rester identique à celle citée dans `SKILL.md` § « Tracer les
décisions de tri ».

| Nature | Ce qu'elle recouvre |
|---|---|
| `sujet-écarté` | L'humain a rejeté un sujet proposé (noter pourquoi : hors cible, déjà traité, trop générique…) |
| `légitimité` | Le filtre de légitimité était trop faible : sujet proposé sans vraie raison que Sunwise soit crédible dessus |
| `rattachement` | Le persona ou le territoire attribué était incorrect, l'humain l'a corrigé |
| `source` | Un chiffre/source retenu a été jugé insuffisamment fiable — ou l'inverse : une source valable écartée à tort |
| `angle-préféré` | Sur un même sujet, l'humain a retenu un angle différent de celui mis en avant par l'agent |
| `fraîcheur` | Sujet trop ancien proposé, ou actualité récente pertinente ratée |
| `priorité` | L'ordre de priorité des sujets ne correspondait pas au besoin réel |
| `doublon` | Sujet déjà traité reproposé (le journal de veille n'a pas été consulté) |

---

## Journal

<!-- Les entrées de décision se placent ici, la plus récente en haut. -->
<!-- Aucune entrée pour l'instant. -->

---

## Rituel de synthèse

> Procédure **humaine** (Claudin). L'agent ne l'exécute jamais. Elle est
> documentée ici pour ne pas être oubliée.

### Quand

Au premier des deux événements qui survient :
- une fois par mois, **ou**
- tous les 10 amendements enregistrés.

### Comment

1. Relire le journal, regrouper les entrées par nature d'écart.
2. Pour chaque nature, compter les occurrences.
3. Appliquer la règle de seuil :
   - Écart vu **1 ou 2 fois** → reste au journal, c'est du contexte, statut inchangé.
   - Écart vu **3 fois ou plus** → candidat à devenir une règle.
4. Pour chaque candidat, trancher : **est-ce que ça mérite de devenir une règle
   générale de filtrage, ou était-ce du cas particulier ?**
   - Question de contrôle : « si j'inscris ça, est-ce que ça améliorerait 8
     veilles sur 10, ou est-ce que ça sur-contraindrait l'agent sur un cas
     rare ? »
5. **Si promotion décidée**, choisir la cible selon la nature de l'écart :

   | Nature de l'écart | Où promouvoir |
   |---|---|
   | `légitimité`, `rattachement`, `priorité` | `SKILL.md` (règles de filtrage) |
   | `source`, `fraîcheur` | `SKILL.md` ou `references/research-sources.md` |
   | `sujet-écarté` récurrent sur un même thème | signale un territoire à préciser dans `shared/ligne-editoriale.md` — **mais c'est une décision éditoriale de la direction, pas une simple promotion : le noter comme « à remonter »**, ne pas modifier soi-même la ligne éditoriale |
   | `doublon` récurrent | renforcer la tenue du journal de veille (`output/drafts/journal-veille.md`), **pas** le SKILL |

   Puis, quand c'est le SKILL ou `research-sources.md` qui change :
   - Modifier à la main le fichier cible.
   - Ajouter une ligne à l'historique des versions du SKILL si c'est le SKILL
     qui change.
   - Dans le journal, passer le statut des entrées concernées de « non promu »
     à « promu v[N] — [date] » (ou « promu research-sources.md — [date] »,
     « à remonter direction — [date] », etc.).
6. **Si non promu après examen** : marquer « examiné, non promu — [raison] »
   pour ne pas réexaminer indéfiniment le même écart.

### Garde-fous du rituel

- **Ne jamais promouvoir sur une seule occurrence.** Un écart isolé est du
  contexte, pas un pattern.
- **Ne jamais laisser l'agent exécuter ce rituel.** La promotion en règle est un
  acte de contrôle éditorial humain.
- **Surveiller la contradiction avec la boucle Analytics** : si le journal
  pousse à écarter un type de sujet mais que l'agent Analytics montre que ce
  type performe, le signal quantitatif prime — noter l'arbitrage.
- **Archiver, ne pas gonfler** : au-delà de ~40 entrées, résumer les entrées
  promues ou closes en une ligne de synthèse et purger le détail, pour garder le
  journal lisible.
