---
name: visual-decisions
description: Journal des amendements humains sur les productions de l'agent Visual. Capture automatique, promotion en règle manuelle. Lu par Visual au démarrage pour un apprentissage doux et réversible.
sources: [chat]
---

# Journal des décisions — agent Visual

> **La trace est automatique. La promotion en règle est humaine.**

Ce fichier trace les écarts entre ce que l'agent Visual a **produit** et ce que
l'humain a finalement **retenu** après amendement (changement de mode, correction
de couleur, refonte de mise en page, remplacement de gabarit…). Il sert
d'apprentissage doux et réversible.

**Règles du journal — à respecter sans exception :**

- **C'est une mémoire de travail, pas une source de vérité.** La vérité reste
  dans `SKILL.md`, `shared/brand-kit.md`, `references/gabarits.md` et
  `references/exemples.md`. En cas de contradiction entre ce journal et le
  SKILL, **le SKILL prime toujours**.
- **L'agent lit ce fichier au démarrage.** Les écarts récurrents encore non
  promus l'informent (« la dernière fois, l'humain a réduit la densité de mes
  slides ») et l'aident à se rapprocher de ce que l'humain tend à préférer —
  **sans que ces écarts soient des règles gravées**.
- **L'agent n'ajoute JAMAIS une entrée pour se complimenter.** Une entrée naît
  uniquement quand un humain **amende réellement** un visuel, ou demande
  explicitement de tracer une décision. Un visuel validé sans changement ne
  génère aucune entrée.
- **La promotion d'un écart récurrent en règle est un acte humain délibéré.**
  Elle se fait lors du rituel de synthèse (voir la fin de ce fichier). L'agent
  ne promeut rien, ne modifie jamais le SKILL, ne change jamais un statut, ne
  supprime jamais d'entrée.

**Ce journal est qualitatif** (amendements humains). Il ne remplace pas la
boucle Analytics de `references/exemples.md` / agent 05, qui est **quantitative**
(quels formats visuels performent). Deux sources distinctes, à ne pas confondre.

---

## Format d'une entrée

```markdown
### [AAAA-MM-JJ] — [type : image post / carrousel / citation / chiffre / recadrage] — [sujet court]

- **Produit par l'agent** : [ce que l'agent avait proposé — description courte, la direction ou le rendu]
- **Retenu par l'humain** : [ce qui a été gardé après amendement]
- **Nature de l'écart** : [une seule catégorie de la taxonomie visuelle ci-dessous]
- **Raison** : [pourquoi, si donnée — sinon « non précisée »]
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
| `mode` | L'humain a changé le mode de rendu retenu (A texte seul / B texte + visuel / C visuel seul) — la recommandation de mode de l'agent est à revoir |
| `charte-couleur` | Une couleur hors palette a échappé à l'agent, ou une nuance de bleu/sable a dû être corrigée |
| `typographie` | Taille, casse, police, hiérarchie de titre |
| `composition` | Mise en page, densité, position des éléments, nombre de blocs |
| `gabarit` | L'humain a changé le gabarit choisi (G1 à G6) pour le format du post |
| `lisibilité` | Contraste, taille de texte en miniature, zone de sécurité |
| `véracité-visuelle` | Un chiffre affiché sans source, une donnée non traçable, un logo tiers, une personne générée, une interface chiffrée |
| `carrousel` | Structure du carrousel : nombre de slides, découpage, slide de hook ou de CTA |

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
   - Écart vu **3 fois ou plus** → candidat à devenir une règle.
4. Pour chaque candidat, trancher : **est-ce que ça mérite de devenir une règle
   générale, ou était-ce du cas particulier ?**
   - Question de contrôle : « si j'inscris ça, est-ce que ça améliorerait 8
     productions sur 10, ou est-ce que ça sur-contraindrait l'agent sur un cas
     rare ? »
5. **Si promotion décidée**, choisir la cible selon la nature de l'écart —
   c'est la spécificité du visuel, où tout ne se promeut pas au même endroit :

   | Nature de l'écart | Où promouvoir |
   |---|---|
   | `mode`, `véracité-visuelle` | `SKILL.md` (règle de comportement) |
   | `charte-couleur`, `typographie`, `lisibilité` | `SKILL.md` si c'est une règle générale, sinon `references/gabarits.md` |
   | `composition`, `gabarit`, `carrousel` | `references/gabarits.md` (correction de gabarit) |
   | Nouveau rendu validé, exemplaire | `references/exemples.md` (nouveau modèle validé) |

   Puis, dans tous les cas :
   - Modifier à la main le fichier cible.
   - Ajouter une ligne à l'historique des versions du SKILL si c'est le SKILL
     qui change.
   - Dans le journal, passer le statut des entrées concernées de « non promu »
     à « promu v[N] — [date] » (ou « promu gabarits.md — [date] », etc.).
6. **Si non promu après examen** : marquer « examiné, non promu — [raison] »
   pour ne pas réexaminer indéfiniment le même écart.

### Garde-fous du rituel

- **Ne jamais promouvoir sur une seule occurrence.** Un amendement isolé est du
  contexte, pas un pattern.
- **Ne jamais laisser l'agent exécuter ce rituel.** La promotion en règle est un
  acte de contrôle éditorial humain.
- **Surveiller la contradiction avec la boucle Analytics** : si le journal
  pousse vers des visuels plus sobres mais que l'agent Analytics montre que les
  visuels plus riches performent mieux, le signal quantitatif prime — noter
  l'arbitrage.
- **Archiver, ne pas gonfler** : au-delà de ~40 entrées, résumer les entrées
  promues ou closes en une ligne de synthèse et purger le détail, pour garder le
  journal lisible.
