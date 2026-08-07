---
name: campagne-lot
description: Boucle d'orchestration produisant un lot de posts LinkedIn (les posts de la semaine) avec l'agent Copy. Deux points d'arrêt : cadrage groupé puis validation groupée. Ne publie jamais.
sources: [chat]
---

# Workflow — Campagne en lot (agent Copy)

## Ce que ce workflow est

Il produit un **lot de 2 à 8 posts LinkedIn** (cible : 5 posts / semaine) en une
seule session, avec **deux interventions humaines groupées** au lieu d'un arrêt
par post.

**Le principe directeur** : une boucle d'orchestration ne supprime pas l'humain,
elle **regroupe** ses interventions. Au lieu de s'arrêter cinq fois pour cinq
posts, elle s'arrête **deux fois pour tout le lot** — une fois pour cadrer
l'ensemble, une fois pour valider l'ensemble.

## Ce que ce workflow n'est pas

- Il **n'orchestre que l'agent Copy** (agent 02).
- Il **ne fait pas de veille** — c'est l'agent Research (01).
- Il **ne produit aucun visuel** — c'est l'agent Visual (03). Il produit
  seulement le brief visuel de chaque post, pour l'étape ultérieure.
- Il **ne publie jamais.** Il rend un lot de brouillons ; un humain valide et
  publie à la main.

**Règle cardinale** : regrouper les arrêts, jamais les supprimer. **Toutes les
règles du SKILL de Copy restent intégralement applicables à chaque post du
lot** — ce workflow les orchestre, il ne les réécrit pas et ne les allège pas.
En cas de doute sur une règle de fond, la source de vérité reste
`agents/copy-social/SKILL.md`, jamais ce fichier.

---

## La séquence en trois temps

### Temps 1 — Cadrage groupé (premier et unique arrêt d'entrée)

L'orchestrateur ne produit encore **aucun post**. Il prépare le lot entier et le
soumet en une fois.

1. **Déterminer la composition du lot.** À partir de la demande (« les 5 posts de
   la semaine ») et de la répartition mensuelle des formats de
   `agents/copy-social/references/formats.md`, proposer une composition
   **équilibrée** : quels formats (F1 à F6), quels personas, quels territoires.
   Ne pas produire cinq posts du même format — la variété est une règle, pas une
   option (voir « déséquilibre à corriger » du SKILL : privilégier F1 et F2, le
   cœur technique aujourd'hui absent).

2. **Proposer un plan de lot** sous forme de tableau :

   ```markdown
   | # | Sujet pressenti | Format | Persona | Territoire | Angle proposé (1 ligne) | Matière disponible ? |
   |---|---|---|---|---|---|---|
   ```

   La colonne « Matière disponible ? » applique la **Porte n°1 en amont, pour
   chaque post** : indiquer si la matière factuelle existe (source vérifiée,
   anecdote réelle fournie, chiffre traçable — y compris depuis
   `shared/retours-experience.md`) ou si le post partira avec des `[À FOURNIR]`.

3. **Signaler les manques en une demande groupée.** Pour les posts dont la
   matière est incomplète, lister ce qui manque — **un bloc par post**, chaque
   élément nommé avec un exemple du format de réponse attendu, exactement comme
   la section « Demander ce qui manque — au moment des angles » du SKILL de Copy
   le prévoit pour un post unique. Une seule demande groupée pour tout le lot,
   pas un message par post.

4. **⏸ ARRÊT.** L'orchestrateur attend que l'humain :
   - valide ou corrige la composition du lot (sujets, formats, angles) ;
   - fournisse la matière manquante qu'il peut fournir ;
   - accepte que les posts encore incomplets partent avec leurs `[À FOURNIR]`.

   Cet arrêt **remplace les cinq arrêts « choix de l'angle »** qu'on aurait eus
   en produisant les posts un par un. Le choix d'angle passe de
   bloquant-par-post à validé-en-lot. Aucun post n'est rédigé avant cet arrêt.

### Temps 2 — Production en série

Une fois le lot cadré et validé, l'orchestrateur produit chaque post, en série,
**sans nouvel arrêt**. Il enchaîne, il ne s'arrête pas entre deux posts.

Pour **chaque** post du lot, il applique le SKILL de Copy dans son intégralité :

- **Porte n°1 réexécutée pour ce post précis.** Le fait qu'un autre post du lot
  ait sa matière ne dispense pas celui-ci de l'inventaire des faits. Un manque
  sur un post **ne contamine pas les autres** et **ne bloque pas le lot** : le
  post concerné sort avec ses `[À FOURNIR]`, les autres continuent.
- Rédaction au format retenu, hook sous 200 caractères, CTA précis.
- Deux hooks alternatifs.
- Brief visuel pour l'agent Visual (produit même si Visual n'est pas orchestré
  ici — il servira à l'étape ultérieure).
- Toutes les règles de fond : formulations bannies, réflexes hérités, personnes
  et sujets sensibles, posts de circonstance proscrits, une seule offre par
  post, aucun client identifiable, aucun chiffre non sourcé.

### Temps 3 — Validation groupée (second et dernier arrêt)

L'orchestrateur rend le **lot entier en une fois**, précédé d'un tableau de
synthèse :

```markdown
## Synthèse du lot — [semaine du …]

| # | Sujet | Format | Persona | Statut | Points d'attention |
|---|---|---|---|---|---|
| 1 | … | F2 | P2 | ✅ complet | — |
| 2 | … | F1 | P1 | ⚠️ incomplet | [À FOURNIR : chiffre X] |
| … | | | | | |
```

Statuts possibles :
- `✅ complet` — publiable après relecture humaine ;
- `⚠️ incomplet` — attend un fait marqué `[À FOURNIR]` ;
- `🔶 à trancher` — un doute que l'orchestrateur signale explicitement.

Sous le tableau, les posts complets, chacun au **format de livraison standard du
SKILL de Copy** (`output/drafts/post-AAAA-MM-JJ-<slug>.md` : version finale,
hooks alternatifs, déclinaisons, brief visuel, éléments à fournir, contrôle
qualité).

**⏸ ARRÊT.** L'humain valide le lot et renvoie ses corrections **en bloc**. Ces
corrections alimentent la boucle de feedback N2 si `agents/copy-social/decisions.md`
est en place (une entrée par amendement réel, selon les règles de ce journal).

---

## Les conditions d'arrêt — le garde-fou anti-emballement

La boucle doit savoir s'interrompre. Elle ne saute jamais un contrôle « pour
avancer » : le faire produirait cinq posts défaillants d'un coup au lieu d'un
seul.

| Condition | Comportement de l'orchestrateur |
|---|---|
| Un sujet ne peut pas être cadré (persona indéterminable, aucun angle légitime au sens du filtre de légitimité) | Le mettre de côté, continuer les autres, le signaler dans la synthèse comme « écarté au cadrage — raison » |
| Trop de posts manquent de matière (seuil : la moitié du lot ou plus) | S'arrêter au Temps 1 et consulter l'humain avant de produire — inutile de produire du vide en série |
| Le lot demandé dépasse 8 posts | Refuser et proposer de scinder en plusieurs lots — au-delà, la validation groupée n'est plus gérable |
| Le lot demandé est de 1 post | Ne pas activer la boucle : renvoyer vers le mode normal du SKILL de Copy (un post = process en 5 temps classique) |

---

## Ce que la boucle ne fait jamais

- **Publier.** La boucle produit un lot de brouillons. Elle ne met rien en ligne.
- **Sauter le cadrage groupé** sous prétexte que c'est une commande de lot.
- **Uniformiser.** Cinq posts du même format et du même angle sont un échec. La
  variété de formats et de territoires est obligatoire.
- **Inventer pour combler.** Un post sans matière sort avec ses `[À FOURNIR]`,
  jamais avec un fait fabriqué pour « faire complet ». La Porte n°1 prime sur la
  complétude du lot.
- **Produire sans validation d'entrée.** Aucun post n'est rédigé avant l'arrêt
  du Temps 1.

---

## Rappel de dépendance

Cette boucle n'a de valeur que si la **production unitaire est fiable**. Elle
multiplie ce que l'agent Copy sait faire sur un post — ses qualités comme ses
défauts. À n'utiliser qu'une fois la production unitaire rodée : orchestrer une
production défaillante ne fait que produire cinq fois le défaut.
