---
name: copy-decisions
description: Journal des amendements humains sur les productions de l'agent Copy. Capture automatique, promotion en règle manuelle. Lu par Copy au démarrage pour un apprentissage doux et réversible.
sources: [chat]
---

# Journal des décisions — agent Copy

> **La trace est automatique. La promotion en règle est humaine.**

Ce fichier trace les écarts entre ce que l'agent Copy a **produit** et ce que
l'humain a finalement **retenu** après amendement. Il sert d'apprentissage doux
et réversible.

**Règles du journal — à respecter sans exception :**

- **C'est une mémoire de travail, pas une source de vérité.** La vérité reste
  dans `SKILL.md`, `formats.md` et les fichiers `shared/`. En cas de
  contradiction entre ce journal et le SKILL, **le SKILL prime toujours**.
- **L'agent lit ce fichier au démarrage.** Les écarts récurrents encore non
  promus l'informent (« la dernière fois, l'humain a raccourci mes hooks ») et
  l'aident à se rapprocher de ce que l'humain tend à préférer — **sans que ces
  écarts soient des règles gravées**.
- **L'agent n'ajoute JAMAIS une entrée pour se complimenter.** Une entrée naît
  uniquement quand un humain **amende réellement** une production, ou demande
  explicitement de tracer une décision. Une production validée sans changement
  ne génère aucune entrée.
- **La promotion d'un écart récurrent en règle du SKILL est un acte humain
  délibéré.** Elle se fait lors du rituel de synthèse (voir la fin de ce
  fichier). L'agent ne promeut rien, ne modifie jamais le SKILL, ne change
  jamais un statut, ne supprime jamais d'entrée.

**Ce journal est qualitatif** (amendements humains). Il ne remplace pas la
boucle Analytics de `references/posts-valides.md`, qui est **quantitative**
(performance mesurée des posts publiés). Deux sources distinctes, à ne pas
confondre.

---

## Format d'une entrée

```markdown
### [AAAA-MM-JJ] — [type de production : post F2 / hook / déclinaison / commentaire] — [sujet court]

- **Produit par l'agent** : [extrait de ce que l'agent avait proposé — court]
- **Retenu par l'humain** : [extrait de la version finale après amendement]
- **Nature de l'écart** : [une seule catégorie principale — voir la taxonomie ci-dessous]
- **Raison** : [pourquoi la correction, si l'humain l'a donnée — sinon « non précisée »]
- **Récurrence** : [1re fois / déjà vu N fois — compte les occurrences de la même nature d'écart]
- **Statut** : non promu
```

Une entrée porte **une seule** nature principale. Si un amendement touche
plusieurs aspects, choisir le plus significatif et mentionner les autres dans la
raison.

---

## Taxonomie des écarts

Liste **fermée**. Toute entrée utilise exactement une de ces natures. Cette
liste doit rester identique à celle citée dans `SKILL.md` § « Tracer les
amendements ».

| Nature | Ce qu'elle recouvre |
|---|---|
| `ton` | L'humain a changé le registre, la chaleur, le niveau de formalité |
| `structure` | L'ordre, le découpage, la longueur des paragraphes |
| `longueur` | Trop long ou trop court |
| `hook` | La première ligne a été retravaillée |
| `véracité` | Un fait, un chiffre ou une formulation corrigé pour exactitude |
| `angle` | L'humain a réorienté le fond du propos |
| `CTA` | La question finale a été changée |
| `charte` | Une formulation bannie ou un réflexe hérité a échappé à l'agent |

---

## Journal

<!-- Les entrées d'amendement se placent ici, la plus récente en haut. -->
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
   - Écart vu **3 fois ou plus** → candidat à devenir une règle du SKILL.
4. Pour chaque candidat, trancher : **est-ce que ça mérite de devenir une règle
   générale, ou était-ce du cas particulier ?**
   - Question de contrôle : « si j'inscris ça comme règle, est-ce que ça
     améliorerait 8 productions sur 10, ou est-ce que ça sur-contraindrait
     l'agent sur un cas rare ? »
5. **Si promotion décidée** :
   - Modifier le SKILL **à la main**, ajouter la règle au bon endroit.
   - Ajouter une ligne à l'historique des versions du SKILL.
   - Dans le journal, passer le statut des entrées concernées de « non promu »
     à « promu v[N] — [date] ».
6. **Si non promu après examen** : marquer « examiné, non promu — [raison] »
   pour ne pas réexaminer indéfiniment le même écart.

### Garde-fous du rituel

- **Ne jamais promouvoir sur une seule occurrence.** Un amendement isolé est du
  contexte, pas un pattern.
- **Ne jamais laisser l'agent exécuter ce rituel.** La promotion en règle est un
  acte de contrôle éditorial humain.
- **Surveiller la contradiction avec la boucle Analytics** : si le journal
  pousse vers des hooks plus courts mais que l'agent Analytics montre que les
  posts à hook long performent mieux, le signal quantitatif prime — noter
  l'arbitrage.
- **Archiver, ne pas gonfler** : au-delà de ~40 entrées, résumer les entrées
  promues ou closes en une ligne de synthèse et purger le détail, pour garder le
  journal lisible.
