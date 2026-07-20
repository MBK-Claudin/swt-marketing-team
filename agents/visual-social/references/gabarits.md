# Gabarits visuels — SUNWISE TALENTS

> Référence de l'agent 03 Visual. Six gabarits, un par format de post.
> Toutes les valeurs de couleur et de taille viennent de `shared/brand-kit.md`.

---

## Rappel palette

| Rôle | HEX | Usage |
|---|---|---|
| Bleu Sunwise | `#002C6A` | Primaire — texte fort, aplats, titres |
| Sable Sunwise | `#F8D99B` | Secondaire — fonds, accents |
| Bleu profond | `#001B42` | Dégradé, ombres |
| Bleu clair | `#1E5AA8` | Éléments secondaires, dataviz |
| Sable clair | `#FCEDD1` | Fonds de section, cartes |
| Sable foncé | `#E0B96E` | Accents, filets, dataviz |
| Blanc | `#FFFFFF` | Texte sur bleu, respirations |
| Gris texte | `#3A4553` | Corps sur fond clair |

**Combinaison signature** : `#002C6A` sur `#F8D99B` — contraste 9.7:1.

---

## G1 — Visuel de retour d'expérience (post F1)

**Base 1080 × 1080 ou 1200 × 627**

```
┌────────────────────────────────┐
│  #002C6A plein                 │
│                                │
│  [Titre 72-96px blanc]         │  ← le hook, 6 mots max
│  [mot clé en #F8D99B]          │  ← un seul mot en accent
│                                │
│                                │
│                          [logo]│  ← monogramme sable, 64px
└────────────────────────────────┘
```

- Fond : bleu plein `#002C6A`
- Titre : blanc, 72–96 px, aligné à gauche, marge 80 px
- Un seul mot en `#F8D99B` — celui qui porte la tension
- Logo : monogramme en sable, coin inférieur droit
- Rien d'autre. Pas de sous-titre, pas de décor.

**Le piège** : vouloir mettre le contexte sur le visuel. Le contexte est dans
le post. Le visuel porte le hook, point.

---

## G2 — Visuel de décryptage technique (post F2)

**Base 1080 × 1080, ou carrousel 5-8 slides**

```
┌────────────────────────────────┐
│  #FFFFFF                       │
│  ─────  ← filet #E0B96E 3px    │
│  [Titre 56-64px #002C6A]       │
│                                │
│  [Structure : comparaison,     │
│   étapes, ou arbre]            │
│   • #002C6A pour les blocs     │
│   • #FCEDD1 pour les fonds     │
│                                │
│  [source si chiffre]     [logo]│
└────────────────────────────────┘
```

- Fond blanc — c'est le format le plus « éditorial »
- Filet sable foncé `#E0B96E` 3 px au-dessus du titre
- Structure claire : max 4 blocs, jamais plus
- Corps de texte `#3A4553`, jamais noir pur

**Variante carrousel** — la plus efficace pour ce format :
- Slide 1 : le hook sur fond bleu (reprend G1)
- Slides 2 à N-1 : fond blanc, une idée par slide, 12 mots max
- Slide finale : CTA + logo, fond sable `#F8D99B`

---

## G3 — Visuel de cas client (post F3)

**Base 1080 × 1080**

```
┌────────────────────────────────┐
│  #FCEDD1                       │
│                                │
│      [CHIFFRE 200px #002C6A]   │  ← le résultat, énorme
│      [légende 32px #3A4553]    │
│                                │
│  [secteur + taille, 28px]      │  ← jamais le nom du client
│                          [logo]│
└────────────────────────────────┘
```

⚠️ **Bloqué en l'état** : `shared/offres.md` § 8 est vide, aucun client n'a
donné d'autorisation. Ce gabarit ne peut être utilisé que si :
- Le chiffre est validé par la direction
- Le client est identifié uniquement par secteur + taille
- Le post complet est relu par la direction avant publication

---

## G4 — Visuel de chiffre (post F4)

**Base 1080 × 1080** — le plus partagé, le plus simple

```
┌────────────────────────────────┐
│  #002C6A plein                 │
│                                │
│                                │
│      [CHIFFRE 260px #F8D99B]   │  ← 60 % de la surface
│      [légende 36px blanc]      │
│                                │
│  [source 20px, blanc 70%] [logo]│
└────────────────────────────────┘
```

- Le chiffre occupe 60 % de la surface. Rien ne le concurrence.
- La légende tient en une ligne, 8 mots max
- **La source est obligatoire et lisible** — organisme + année, en bas à gauche
- Aucun élément décoratif

**Règle stricte** : pas de chiffre sans source affichée sur le visuel lui-même.
Un chiffre sans source qui circule seul en capture d'écran devient une
affirmation non sourcée attribuée à Sunwise.

---

## G5 — Visuel d'équipe / recrutement (post F5)

**Base 1080 × 1350 (portrait, plus visible dans le fil)**

**Variante A — avec photo** *(indisponible à ce jour)*
```
┌────────────────────────────────┐
│  [photo équipe]                │
│                                │
│                                │
├────────────────────────────────┤
│  #002C6A bandeau bas 30%       │
│  [titre 56px blanc]      [logo]│
└────────────────────────────────┘
```
⚠️ Aucune photo avec accord de droit à l'image n'est disponible
(`shared/brand-kit.md` § 9). Utiliser la variante B.

**Variante B — typographique**
```
┌────────────────────────────────┐
│  #F8D99B plein                 │
│                                │
│  [Intitulé du poste 64px       │
│   #002C6A]                     │
│                                │
│  — Libreville / Paris          │  ← filet + localisation
│  — [3 mots-clés du poste]      │
│                                │
│                          [logo]│
└────────────────────────────────┘
```

- Fond sable plein — c'est le seul gabarit où le sable domine
- Le territoire 2 (France ↔ Afrique) s'exprime ici : mentionner les deux sites
  est un différenciateur, pas un détail logistique

---

## G6 — Visuel d'engagement (post F6)

**Base 1080 × 1080**

```
┌────────────────────────────────┐
│  #FFFFFF                       │
│                                │
│  [Titre 48px #002C6A]          │  ← factuel, au passé
│  [sous-titre 28px #3A4553]     │
│                                │
│  ─────  ← filet #E0B96E        │
│  [partenaire, 24px]            │
│                          [logo]│
└────────────────────────────────┘
```

- Le plus sobre de tous. Aucun effet, aucune emphase.
- Fond blanc uniquement
- **Aucune photo de bénéficiaire identifiable.** Règle de dignité, non négociable.
- Partenaire citable : « Rayons d'Espoir et d'Amour »
- Pas de chiffre de don tant qu'il n'est pas validé par la direction

**Le test** : ce visuel serait-il produit même s'il ne rapportait rien
commercialement ? Si non, il ne sort pas.

---

## Structure d'un carrousel LinkedIn

**5 à 10 slides. Export PDF. 1080 × 1080 ou 1080 × 1350.**

| Slide | Rôle | Gabarit |
|---|---|---|
| 1 | Le hook | G1 — fond bleu, une phrase |
| 2 | La mise en tension | Fond blanc, le problème |
| 3 à N-1 | Une idée par slide | Fond blanc, 12 mots max |
| N | CTA + logo | Fond sable `#F8D99B` |

**Règles**
- 12 mots maximum par slide. Compte-les.
- Une idée par slide. Si une slide en contient deux, c'est deux slides.
- Numérotation discrète en bas : `3/7`, 20 px, opacité 50 %
- Le logo apparaît sur la slide 1 et la slide finale, pas sur toutes
- Cohérence de mise en page : la position du titre ne bouge pas d'une slide
  à l'autre

**Le piège du carrousel** : vouloir y mettre tout le post. Le carrousel n'est
pas une version illustrée du texte — c'est un contenu autonome qui doit tenir
debout sans le post.

---

## Dataviz — palette imposée

Ordre des séries dans un graphique :

1. `#002C6A` — série principale
2. `#E0B96E` — comparaison
3. `#1E5AA8` — troisième série
4. `#F8D99B` — quatrième série

**Au-delà de 4 séries, le graphique est mauvais.** Simplifier plutôt qu'ajouter
une cinquième couleur.

**Règles**
- Jamais de camembert au-delà de 3 parts
- Axes en `#3A4553`, grille en `#E8EAED` très légère
- Étiquettes de données directement sur le graphique, pas de légende séparée
  quand c'est évitable
- Toujours doubler la couleur d'un second marqueur (hachure, trait, forme) —
  une information ne doit jamais dépendre de la couleur seule

---

## Ce qui n'est pas produisible

| Besoin | Réalité | Alternative |
|---|---|---|
| Photo d'équipe | Aucun accord de droit à l'image collecté | G5 variante B, typographique |
| Photo réaliste d'illustration | L'agent produit du vectoriel, pas de la photo | Banque externe (licence à vérifier) ou composition graphique |
| Capture d'écran Salesforce | Interdit avec de la donnée client | Refaire dans un org de démo |
| Logo client | Aucune autorisation | Mention secteur + taille uniquement |
| Portrait d'un collaborateur | Accord individuel requis | Visuel typographique |

**Ne jamais promettre un visuel qu'on ne peut pas produire.** Le dire d'emblée
et proposer l'alternative.

---

## À faire valider

| Point | Qui décide | Impact |
|---|---|---|
| Polices officielles (recommandation : Poppins / Inter) | Direction | Incohérence typo entre visuels |
| Accords de droit à l'image de l'équipe | RH | Débloque G5 variante A |
| Autorisations clients | Direction commerciale | Débloque G3 |
| Chiffres officiels de l'entreprise | Direction | Débloque G4 sur nos propres données |
| Banque d'images sous licence | Marketing | Débloque les visuels avec photo |