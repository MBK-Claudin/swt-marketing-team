# Brand Kit — SUNWISE TALENTS

> Lu par l'agent **Visual (03)**.
> Aucun visuel, slide ou export ne sort de ce cadre sans validation explicite.

---

## 1. Identité de marque

| Élément | Valeur |
|---|---|
| Nom officiel | SUNWISE TALENTS |
| Écriture en post | « Sunwise Talents » (capitales réservées au logo et aux titres) |
| Baseline fonctionnelle | Intégrateur Salesforce transcontinental — France & Gabon |
| Fondation | 2021 |
| Siège | Villeneuve-le-Roi (France) |
| Autres implantations | Paris (France), Libreville (Gabon) |
| Site | https://sunwisetalents.com/ |
| LinkedIn | https://www.linkedin.com/company/sunwise-talents/ |

**Étymologie à exploiter en création** : *Sun* (soleil, lumière, chaleur, Afrique) + *wise* (sagesse, expertise, discernement) + *Talents* (l'humain avant la techno). Le champ lexical solaire est légitime et distinctif — à utiliser sans le sur-jouer.

---

## 2. Palette de couleurs

### Couleurs primaires (extraites du logo officiel)

| Rôle | Nom interne | HEX | RGB | Usage |
|---|---|---|---|---|
| Primaire | Bleu Sunwise | `#002C6A` | 0, 44, 106 | Texte fort, aplats de fond, logo, titres |
| Secondaire | Sable Sunwise | `#F8D99B` | 248, 217, 155 | Fond de visuel, accents, highlights, aplats chauds |

Ces deux couleurs sont **non négociables**. Elles proviennent directement du fichier logo et forment le contraste signature de la marque (marine profond / sable lumineux).

### Couleurs de support (dérivées — usage limité)

| Nom | HEX | Usage autorisé |
|---|---|---|
| Bleu profond | `#001B42` | Fonds très sombres, ombres, dégradés vers le bas |
| Bleu clair | `#1E5AA8` | Liens, hover, éléments secondaires, dataviz |
| Sable clair | `#FCEDD1` | Fonds de section, cartes, zones de respiration |
| Sable foncé | `#E0B96E` | Accents, soulignements, bordures, dataviz |
| Blanc | `#FFFFFF` | Texte sur fond bleu, respirations |
| Gris texte | `#3A4553` | Corps de texte sur fond clair (jamais du noir pur) |
| Gris léger | `#E8EAED` | Séparateurs, bordures fines, fonds neutres |

### Règles d'usage couleur

- **Ratio cible** : 60 % bleu ou blanc / 30 % sable / 10 % accents.
- Le sable est un **accent chaud**, pas un fond par défaut sur tous les visuels — sinon la marque devient monotone.
- **Jamais** : rouge, vert vif, violet, néon, dégradés multicolores.
- Un seul dégradé autorisé : `#002C6A` → `#001B42` (vertical ou diagonal).
- **Contraste** : `#002C6A` sur `#F8D99B` = ratio ~9.7:1 → conforme WCAG AAA. C'est la combinaison à privilégier partout.
- Texte blanc sur `#002C6A` = conforme. Texte sable `#F8D99B` sur bleu = utilisable pour les titres uniquement, jamais pour du corps de texte long.
- **Interdit** : bleu `#002C6A` sur `#1E5AA8` (contraste insuffisant), sable sur blanc.

### Palette dataviz (graphiques)

Ordre imposé pour les séries :
1. `#002C6A` — série principale
2. `#E0B96E` — série de comparaison
3. `#1E5AA8` — troisième série
4. `#F8D99B` — quatrième série
5. `#5C7A9E` — au-delà (rare : si tu as plus de 4 séries, le graphique est mauvais)

---

## 3. Logo

### Fichiers disponibles

| Fichier | Usage |
|---|---|
| `shared/assets/Color logo.png` | Logo « S » sur fond sable arrondi, 526 × 605 px — avatar, favicon, coin de visuel |
| `shared/assets/Color logo with background.pdf` | Version vectorielle avec fond — print, grands formats, slides |

Les deux noms de fichier contiennent des espaces : les échapper ou les guillemeter dans
toute commande. Ne pas les renommer sans mettre à jour cette section.

### Description
Monogramme « S » stylisé en bleu `#002C6A`, formé de deux courbes qui s'entrelacent, posé sur un carré à coins arrondis `#F8D99B`. La forme évoque le lien, la connexion, le flux — cohérent avec « bridge entre deux continents ».

### Règles d'utilisation

- **Zone de protection** : espace vide minimum autour du logo = ½ de la hauteur du logo. Rien ne rentre dans cette zone.
- **Taille minimale** : 32 px de large en digital, 12 mm en print.
- **Placement standard** : coin inférieur droit des visuels social, coin supérieur gauche des slides.
- **Sur fond bleu** : utiliser le monogramme sable ou blanc, pas le bloc sable complet.
- **Sur photo** : uniquement sur une zone calme et sombre, avec le monogramme blanc.

### Interdits absolus
- Déformer, étirer, incliner ou faire pivoter le logo
- Recolorer hors palette de marque
- Ajouter ombre portée, contour, effet 3D, biseau, lueur
- Placer sur un fond chargé qui nuit à la lisibilité
- Recréer ou redessiner le « S » à la main — toujours utiliser le fichier fourni
- Combiner le logo avec un autre logo sans séparateur vertical clair

---

## 4. Typographie

Aucune police de marque n'étant formalisée à ce jour, le référentiel ci-dessous est **la recommandation à valider par la direction**. Une fois validée, cette section devient prescriptive et cesse d'être une proposition.

### Recommandation

| Rôle | Police | Alternative système | Poids |
|---|---|---|---|
| Titres / Hooks | **Poppins** | Montserrat, Arial Bold | 600–700 |
| Corps de texte | **Inter** | Source Sans Pro, Helvetica | 400–500 |
| Chiffres / données | **Inter** (tabular nums) | — | 600 |
| Code / technique | **JetBrains Mono** | Consolas, monospace | 400 |

**Pourquoi ce couple** : Poppins a des formes géométriques rondes qui rappellent la courbe du logo et apportent une chaleur cohérente avec le sable. Inter est neutre, très lisible en petit corps, et sérieux — équilibre nécessaire pour une marque qui vend de l'expertise technique.

### Échelle typographique — Visuels social (base 1080 px)

| Niveau | Taille | Interlignage | Usage |
|---|---|---|---|
| Hook carrousel slide 1 | 72–96 px | 1.1 | 6 mots max |
| Titre de slide | 56–64 px | 1.15 | |
| Sous-titre | 36–40 px | 1.3 | |
| Corps | 28–32 px | 1.5 | Jamais en dessous de 28 px |
| Légende / source | 20–22 px | 1.4 | |

### Échelle typographique — Slides (16:9, 1920×1080)

| Niveau | Taille |
|---|---|
| Titre de slide | 40–44 pt |
| Sous-titre | 24–28 pt |
| Corps / bullet | 18–20 pt |
| Note de bas de slide | 12–14 pt |

### Règles typo
- Maximum **2 familles** de police par visuel.
- Jamais de texte en italique pour de l'emphase — utiliser le gras ou la couleur.
- Jamais de MAJUSCULES sur plus de 5 mots.
- Alignement à gauche par défaut. Le centré est réservé aux slides de citation et aux slides de titre.
- Pas de justification (crée des rivières blanches).

---

## 5. Style visuel

### Principes directeurs

1. **Clarté avant décoration.** Un visuel Sunwise doit se lire en 2 secondes sur un écran de téléphone.
2. **Chaleur maîtrisée.** Le sable apporte l'humain, le bleu apporte la crédibilité. On ne renonce ni à l'un ni à l'autre.
3. **Pas de stock photo générique.** Ni poignées de main, ni « équipe multiculturelle qui rit devant un ordinateur », ni globe terrestre avec réseau bleu.
4. **Le lien comme motif.** Le « S » du logo est fait de deux courbes qui se rejoignent. Ce motif de connexion (arc, flux, pont) est le langage graphique de la marque.

### Éléments graphiques autorisés

| Élément | Spécification |
|---|---|
| Coins arrondis | Rayon 16–24 px sur les cartes et blocs (écho au logo) |
| Formes de fond | Arcs et courbes larges, jamais d'angles agressifs |
| Séparateurs | Trait 2–3 px en `#E0B96E` |
| Icônes | Style linéaire, trait 2 px, coins arrondis, monochrome bleu ou sable |
| Ombres | Très douces uniquement : `0 4px 24px rgba(0,44,106,0.10)` |
| Motif de fond | Grille de points ou lignes courbes très faible opacité (≤ 8 %) |

### Interdits visuels
- Ombres portées dures, effets 3D, biseaux, reflets
- Cliparts, émojis intégrés dans le design du visuel
- Dégradés arc-en-ciel ou multicolores
- Photos de personnes non contractualisées (droit à l'image)
- Logos de clients sans autorisation écrite — voir `shared/offres.md`
- Toute IP tierce : logos de marques, personnages sous licence, visuels de films/séries
- Captures d'écran Salesforce contenant de la donnée client réelle (même floutée — refaire dans un org de démo)

---

## 6. Formats et dimensions

### Réseaux sociaux

| Plateforme | Format | Dimensions | Ratio |
|---|---|---|---|
| LinkedIn — image de post | Paysage | 1200 × 627 | 1.91:1 |
| LinkedIn — carrousel (PDF) | Carré | 1080 × 1080 | 1:1 |
| LinkedIn — carrousel portrait | Portrait | 1080 × 1350 | 4:5 |
| LinkedIn — bannière page | — | 1128 × 191 | — |
| Instagram — feed | Portrait | 1080 × 1350 | 4:5 |
| Instagram — story / reel cover | Vertical | 1080 × 1920 | 9:16 |
| Facebook — post | Paysage | 1200 × 630 | 1.91:1 |
| X / Twitter — image | Paysage | 1600 × 900 | 16:9 |

### Documents

| Usage | Format |
|---|---|
| Slides internes / client | 16:9 — 1920 × 1080 |
| One-pager | A4 portrait — 210 × 297 mm |
| Page web / landing | Responsive, breakpoint mobile 375 px |

### Règles de format
- **Carrousel LinkedIn** : entre 5 et 10 slides. Slide 1 = le hook. Dernière slide = CTA + logo.
- **Max 12 mots par slide** de carrousel.
- Toujours vérifier la lisibilité à 30 % de zoom (simulation mobile) avant export.
- Zone de sécurité : 80 px de marge sur les visuels 1080 px, rien d'important au bord.
- Export : PNG pour les visuels avec aplats, PDF pour les carrousels LinkedIn.

---

## 7. Voix visuelle par type de contenu

| Type de post | Traitement visuel |
|---|---|
| Retour d'expérience | Fond bleu, texte blanc, accent sable sur un mot clé |
| Cas client | Fond sable clair, chiffre en très gros en bleu |
| Veille / décryptage | Fond blanc, structure éditoriale, titre bleu, filet sable |
| Coulisses / équipe | Photo réelle de l'équipe (avec accord) + bandeau bleu bas |
| Recrutement | Fond sable plein, titre bleu, logo bien visible |
| Chiffre / stat | Le chiffre occupe 60 % de la surface. Rien d'autre. |

---

## 8. Checklist avant export (agent Visual)

- [ ] Couleurs strictement dans la palette de la section 2
- [ ] Logo présent, non déformé, zone de protection respectée
- [ ] Aucun texte sous 28 px sur un visuel 1080 px
- [ ] Contraste texte/fond vérifié (≥ 4.5:1 pour le corps, ≥ 3:1 pour les grands titres)
- [ ] Aucune donnée client réelle visible
- [ ] Aucun logo tiers non autorisé
- [ ] Bonnes dimensions pour la plateforme cible
- [ ] Lisible en miniature (test à 30 %)
- [ ] Nom de fichier : `AAAA-MM-JJ-plateforme-slug.png`

---

## 9. À faire valider

Ces points ne sont pas encore arbitrés et bloquent une partie de la production :

| Point | Qui décide | Impact si non tranché |
|---|---|---|
| Polices officielles | Direction / marketing | Incohérence typo entre visuels |
| Baseline officielle en français | Direction | Chaque visuel invente sa formule |
| Banque de photos équipe (avec accords signés) | RH | Aucun contenu « coulisses » possible |
| Liste des clients citables publiquement | Direction commerciale | Aucun cas client publiable |
| Version anglaise du kit (cible France + international ?) | Direction | Ambiguïté sur la langue des visuels |