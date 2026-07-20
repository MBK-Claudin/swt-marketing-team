# Visuel — Quand Salesforce est surdimensionné pour le besoin

**Mode de rendu** : B — texte + visuel
**Post associé** : `output/drafts/post-2026-07-20-crm-surdimensionne.md`
**Format** : image de post — 1200 × 627 px (1.91:1)
**Plateforme** : LinkedIn
**Fichiers exportés** :
- `output/visuals/2026-07-20-linkedin-crm-surdimensionne.png`
- `output/visuals/2026-07-20-linkedin-crm-surdimensionne.build.py` — script de composition,
  conservé pour pouvoir régénérer le visuel à l'identique le jour où les polices officielles
  seront arbitrées

> **Note sur le mode** : le mode B a été demandé explicitement. Pour mémoire, les critères
> du SKILL recommandaient le mode A — un F2 dont la valeur est dans le raisonnement, sans
> chiffre ni structure à clarifier. Le visuel produit ne porte donc pas d'information : il
> porte le hook, ce qui reste sa fonction légitime.

## Direction retenue

Direction 2 — « le bleu signature ». Fond bleu plein, hiérarchie de titre à deux niveaux
(acquis A2 de `exemples.md`), bloc logo en en-tête haut gauche (acquis A1).

## Texte intégré

| Élément | Texte exact |
|---|---|
| Bloc logo | Sunwise Talents |
| Niveau 1 (blanc, 40 px) | Est-ce que l'outil peut le faire ? |
| Niveau 2 (sable, 96 px) | Mauvaise question. |

Sentence case partout. Aucune capitale longue. Le visuel ne reprend aucune phrase du post :
il pose la question que le post démonte, rien d'autre.

## Sources des données affichées

| Élément | Valeur | Source |
|---|---|---|
| — | — | **Aucun chiffre sur ce visuel.** Aucune donnée vérifiée n'était disponible sur ce sujet — voir `research-2026-07-20.md`, section « écarté ». |

## Composition technique

| Élément | Valeur |
|---|---|
| Fond | `#002C6A` — exact, vérifié par échantillonnage |
| Accent | `#F8D99B` — exact |
| Filet | `#E0B96E`, 3 px, 96 px de long |
| Texte secondaire | `#FFFFFF` |
| Police | **Arial** (Bold + Regular) — alternative système prévue par `brand-kit.md` § 4 |
| Marge de sécurité | 72 px, respectée sur les quatre bords |
| Logo | Compositée depuis `shared/assets/Color logo.png`, hauteur 64 px, non déformée, non redessinée |
| Espacement du bloc logo | Moitié de la largeur du monogramme, conforme à A1 |

## Éléments à fournir

- [ ] **Polices officielles** — blocage 🟠 de `CLAUDE.md` § 8. Poppins et Inter ne sont
      qu'une recommandation en attente d'arbitrage, et ni l'une ni l'autre n'est installée
      sur la machine de production. Le visuel est composé en Arial. Le jour où la direction
      tranche, relancer le script joint en changeant les deux chemins de police en tête de
      fichier — le rendu sera identique par ailleurs.

## Deux points à arbitrer

**1. Le bloc logo sur fond bleu.** `brand-kit.md` § 3 dit : « sur fond bleu, utiliser le
monogramme sable ou blanc, pas le bloc sable complet. » Or le seul fichier officiel
disponible est précisément le bloc complet — un « S » bleu sur carré sable — et
`exemples.md` § A1 décrit ce même bloc comme la signature reconnaissable de la marque sur
les visuels existants. Les deux fichiers se contredisent.

J'ai utilisé le fichier officiel tel quel, parce que le brand-kit interdit par ailleurs de
redessiner ou de recolorer le logo à la main. **C'est un arbitrage à trancher** : soit
`brand-kit.md` § 3 est amendé, soit la direction fournit une déclinaison monogramme sable
seul en fichier.

**2. Le ratio couleur.** Répartition mesurée : 95 % bleu, 3,3 % sable, 0,6 % blanc.
`brand-kit.md` § 2 fixe une cible de 60 % bleu ou blanc / 30 % sable / 10 % accents — le
sable est donc très en dessous. Mais `exemples.md` § « Direction visuelle retenue » demande
l'inverse : « accent sable sur un seul élément par visuel ». Une direction typographique
sobre produit mécaniquement peu de sable.

Je n'ai pas coché la ligne du ratio dans le contrôle ci-dessous : le visuel suit
`exemples.md` contre la lettre de `brand-kit.md` § 2, et c'est un choix assumé, pas un
oubli. À trancher entre les deux fichiers.

## Contrôle

**Droits et véracité**
- [x] Chaque chiffre affiché est traçable — aucun chiffre affiché
- [x] Aucun chiffre sur l'entreprise
- [x] Aucun logo tiers, aucune IP — pas de logo Salesforce (dérive D1 du corpus)
- [x] Aucune personne identifiable, aucune personne générée (dérive D5)
- [x] Aucune donnée client réelle, aucune interface, aucun mockup chiffré (dérive D2)

**Charte**
- [x] Couleurs strictement dans la palette § 2 — vérifiées par échantillonnage
- [ ] Ratio 60/30/10 — **non conforme, volontairement.** Voir « points à arbitrer »
- [x] Une seule famille typographique
- [x] Logo présent, non déformé, zone de protection respectée
- [x] Sentence case, aucune capitale longue (dérive C3)

**Lisibilité**
- [x] Texte le plus petit : 27 px sur un visuel 627 px de haut — au-dessus du seuil
- [x] Contraste : sable sur bleu 9.7:1, blanc sur bleu 13.6:1
- [x] Lisible en miniature — deux blocs seulement
- [x] Zone de sécurité 72 px respectée, jambage du « q » compris
- [x] Aucun glyphe manquant ni déformé (dérive C5) — l'espace fine insécable a été
      remplacée par une insécable classique, absente d'Arial sous sa forme fine

**Cohérence**
- [x] Le visuel ne répète pas le texte du post
- [x] Trois blocs d'information maximum — il y en a deux (dérive C4)
- [x] Bonnes dimensions pour LinkedIn
- [x] Nom de fichier au format `AAAA-MM-JJ-plateforme-slug`
