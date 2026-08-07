# Exemples visuels — analyse du corpus

> Référence de l'agent 03 Visual, à lire avec `gabarits.md`.
> Sept visuels publiés ont été analysés. Ce fichier dit ce qu'il faut
> **reprendre**, ce qu'il faut **corriger**, et ce qu'il faut **abandonner**.

---

## Statut du corpus

| Visuel | Sujet | Verdict |
|---|---|---|
| V1 | Recrutement développeur web | 🟠 Structure à reprendre, couleur à corriger |
| V2 | Expertise Salesforce | 🔴 Hors charte — bleu ardoise |
| V3 | Mains jointes / collaboration | 🔴 À abandonner — hors palette, cliché visuel |
| V4 | Vœux 2026 | 🔴 À abandonner — logo tiers déformé + texte généré (le sujet, lui, est désormais permis : cas A) |
| V5 | 8 mars | 🟠 Charte respectée, mais sujet écarté au titre du cas B (genre) |
| V6 | Eïd Mubarak | 🔴 À abandonner — cas B maintenu, territoire interdit (religion) |
| V7 | 1er mai | 🔴 Données fictives affichées — risque réel |

**Deux visuels sur sept sont dans la charte couleur.** Aucun n'est
intégralement réutilisable comme modèle.

---

## Ce qui fonctionne et doit être conservé

Le corpus contient de vrais acquis. Ils sont listés en premier parce que
l'agent doit les reproduire, pas les redécouvrir.

### A1 — Le bloc logo en en-tête

**Où** : V1, V2, V3, V6, V7

Monogramme sable `#F8D99B` en carré arrondi + « Sunwise Talents » en blanc à
droite, aligné en haut à gauche. C'est devenu la signature de la marque, elle
est immédiatement reconnaissable.

**À conserver tel quel.** Position en haut à gauche, monogramme entre 56 et
80 px sur un visuel 1080 px, nom en blanc à droite, espacement égal à la
moitié de la largeur du monogramme.

Sur V5, le bloc est posé sur un rectangle bleu plus clair que le fond — cette
surcouche est inutile et affaiblit le bloc. À supprimer.

### A2 — La hiérarchie titre en deux niveaux

**Où** : V1, V7

Un mot ou une expression en très grand corps, en sable, suivi d'un second
niveau en blanc plus petit :

```
NOUS RECRUTONS        ← sable #F8D99B, corps 1
Développeur (se) Web  ← blanc, corps 2 (≈ 45 % du corps 1)
```

C'est efficace, lisible en miniature, et ça respecte la règle « un seul mot en
accent ». **À conserver** — c'est exactement la logique du gabarit G1.

### A3 — La structure en bandes horizontales

**Où** : V1

Bandeau bleu haut (titre) → zone photo → bandeau bleu bas (contenu).
La composition est claire, tient en miniature, et sépare proprement
l'information de l'image.

**À conserver** pour les gabarits avec photo, quand des photos autorisées
seront disponibles.

### A4 — La pastille de rappel

**Où** : V7 — « CONNEXION • EXPERTISE • IMPACT »

Une bande fine en capitales, sable et blanc, sur fond bleu foncé arrondi.
Sobre, lisible, utile pour un rappel de positionnement.

**À conserver**, en respectant la règle de sentence case pour tout le reste
du visuel : cette pastille est la seule exception admise aux capitales, parce
qu'elle est courte et fonctionne comme une signature.

---

## Ce qui doit être corrigé

### C1 — La dérive du bleu

C'est l'écart le plus fréquent et le plus visible.

| Visuel | Bleu dominant relevé | Écart |
|---|---|---|
| V5 | `#002C6B` | ✅ Conforme |
| V4 | `#012E6F` | Proche, mais fond bleu roi hors charte |
| V1 | `#001C4C` | Trop sombre |
| V7 | `#01203F` | Trop sombre |
| V2 | `#123048` | Bleu ardoise — hors palette |
| V6 | `#051433` | Bleu nuit — hors palette |

**Règle** : le fond bleu est `#002C6A`, sans exception. `#001B42` est
disponible uniquement comme second point d'un dégradé vertical, jamais comme
aplat principal.

L'œil ne fait pas la différence sur un visuel isolé. Il la fait sur un fil de
douze posts — et c'est là que la marque paraît approximative.

### C2 — Le sable qui glisse vers l'or

V6 utilise un or `#EFC24A` saturé et brillant, très éloigné du sable
`#F8D99B`. V7 utilise `#F6D5A8`, acceptable mais légèrement rosé.

**Règle** : le sable est `#F8D99B`. Les seules variations admises sont
`#FCEDD1` (sable clair) et `#E0B96E` (sable foncé), listées au brand-kit § 2.
Aucun effet métallique, aucune brillance.

### C3 — Les capitales longues

V5 : « JOURNÉE INTERNATIONALE DES DROITS DE LA FEMME » — 44 caractères en
capitales.
V7 : « FÊTE DU TRAVAIL », « DONNÉES STRATÉGIE PERFORMANCE ».

**Règle du brand-kit** : jamais de capitales sur plus de 5 mots. Les capitales
longues réduisent la vitesse de lecture et durcissent le ton.

### C4 — La surcharge

V7 contient : le bloc logo, un titre à deux niveaux, un filet, trois blocs de
texte, une pastille de positionnement, un mockup d'ordinateur, un badge
circulaire, deux motifs de points, une icône, une plante, un mug.

**Le message se perd.** Le brand-kit fixe un principe : un visuel Sunwise doit
se lire en 2 secondes sur un écran de téléphone.

**Règle** : maximum trois blocs d'information par visuel. Si le contenu n'y
tient pas, c'est un carrousel.

### C5 — Le rendu du texte généré

Sur V3, V4, V5, V6, le mot « Talents » apparaît déformé — la lettre T est
altérée sur plusieurs visuels. Sur V4, « Joyeuse » présente un défaut de
rendu.

C'est la signature typique d'un texte produit par génération d'image plutôt
que composé.

**Règle** : le texte n'est jamais généré dans l'image. Il est composé
par-dessus, dans la police de marque. Un nom de marque déformé sur un visuel
public abîme directement la crédibilité.

---

## Ce qui doit être abandonné

### D1 — Le logo Salesforce

**Où** : V4, V5, V7

Le nuage Salesforce apparaît sur trois visuels, dont deux fois recomposé et
déformé (V4). C'est une marque déposée appartenant à Salesforce, Inc.

**Règle absolue** : aucun logo tiers sur un visuel Sunwise, quel qu'il soit.
Cette règle figure déjà au brand-kit § 5 et à `SKILL.md` § « Ce que tu ne
représentes jamais ».

Le partenariat Salesforce se mentionne **en texte** — « intégrateur
Salesforce » — jamais par le logo. Si l'entreprise obtient un statut de
partenaire officiel, Salesforce fournit alors un badge dont l'usage est
encadré par un guide de marque à respecter à la lettre.

### D2 — Les données fictives affichées

**Où** : V7

Le mockup affiche un tableau de bord Salesforce avec : pipeline €2,8M,
76 % de quota atteint, 1 245 comptes actifs, +18 % vs mois précédent,
opportunités à €350 000 / €280 000 / €150 000.

**Ces chiffres sont inventés et se lisent comme les nôtres.**

Un lecteur qui voit ce visuel sur la page Sunwise Talents comprend que ce sont
nos résultats ou ceux d'un client. `shared/offres.md` § 6 est explicite :
aucun chiffre de cette nature n'existe officiellement.

**Règle** : aucune capture d'écran, réelle ou simulée, contenant des données
chiffrées. Si un mockup d'interface est nécessaire, les valeurs sont
remplacées par des libellés neutres, ou floutées de façon manifestement
illisible.

C'est le point le plus sérieux du corpus. Il ne s'agit pas de style.

### D3 — Les visuels de circonstance : la règle a changé

**Décision de la direction** : les posts de circonstance (cas A — vœux, fête du
travail, moments d'équipe) sont désormais **autorisés sous conditions**
(substance + quota de 2/mois). La règle visuelle suit : **un visuel de
circonstance est autorisé dès lors que le post associé l'est**. Voir `SKILL.md`
de l'agent 02 § « Les posts de circonstance » et `shared/ligne-editoriale.md`
§ 5 bis.

Ce qui reste écarté ici ne l'est plus au titre du « sujet de circonstance », mais
pour des motifs propres à chaque visuel :

- **V4 (vœux 2026)** : le sujet est permis (cas A). Le visuel reste à abandonner
  pour ses **autres** défauts, déjà documentés : logo Salesforce recomposé et
  déformé (§ D1) et texte généré dans l'image — « Joyeuse » et « Talents »
  déformés (§ C5). Refait proprement, avec substance, un visuel de vœux serait
  recevable.
- **V5 (8 mars) et V6 (Eïd)** : écartés au titre du **cas B**, maintenu. V5
  singularise le genre ; V6 mobilise une imagerie religieuse complète — mosquées,
  croissant, lanternes, Coran ouvert. Les fêtes et journées liées à un critère
  protégé ne se traitent jamais à l'échelle d'une personne, et la religion reste
  un territoire interdit par la ligne éditoriale. Ces deux-là ne se refont pas.

### D4 — L'imagerie cliché

**Où** : V3 — mains jointes autour d'une table

C'est l'image d'illustration corporate la plus utilisée au monde. Elle ne dit
rien de Sunwise. Le brand-kit § 5 la nomme explicitement :

> Pas de stock photo générique. Ni poignées de main, ni « équipe
> multiculturelle qui rit devant un ordinateur », ni globe terrestre avec
> réseau bleu.

S'y ajoute un orange `#EC791E` totalement hors palette.

### D5 — Les photos générées de personnes

**Où** : V1, V2, V3, V5

Ces visuels montrent des personnes qui n'existent pas, présentées dans un
contexte qui suggère qu'il s'agit de l'équipe ou des clients.

Deux problèmes :
- **Honnêteté** : montrer une équipe fictive sur un visuel de recrutement
  induit le candidat en erreur sur ce qu'il rejoint.
- **Représentation** : ces images figent une composition d'équipe qui n'est
  pas la réalité.

**Règle** : les personnes représentées sont soit des collaborateurs réels avec
accord écrit de droit à l'image, soit personne. Aucune photo générée de
personne sur un support de marque.

En attendant les accords, le gabarit G5 variante B (typographique) est la
solution — et il produit un visuel plus distinctif qu'une photo générique.

---

## Direction visuelle retenue

Ce que le corpus, une fois corrigé, indique comme direction :

| Élément | Décision |
|---|---|
| Fond | Bleu `#002C6A` plein, dominant |
| Accent | Sable `#F8D99B` sur un seul élément par visuel |
| Bloc logo | En-tête haut gauche, monogramme + nom en blanc |
| Titre | Deux niveaux — accent sable puis blanc |
| Densité | Trois blocs d'information maximum |
| Texte | Toujours composé, jamais généré |
| Personnes | Aucune, tant qu'aucun accord n'est collecté |
| Logos tiers | Aucun |
| Chiffres | Sourcés et affichés avec leur source, ou absents |

**Ce que ça donne** : des visuels plus sobres, plus typographiques, plus
rapides à produire, et immédiatement reconnaissables. C'est le sens du
gabarit G1.

---

## Grille de contrôle sur le corpus

À appliquer à tout nouveau visuel. Si une ligne échoue, le visuel ne sort pas.

| # | Contrôle | V1 | V2 | V3 | V4 | V5 | V6 | V7 |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | Bleu exactement `#002C6A` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| 2 | Sable exactement `#F8D99B` | ✅ | — | ❌ | ✅ | ✅ | ❌ | ⚠️ |
| 3 | Aucune couleur hors palette | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| 4 | Aucun logo tiers | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| 5 | Aucune donnée chiffrée non sourcée | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| 6 | Aucune personne sans accord | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| 7 | Texte composé, non déformé | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| 8 | Capitales ≤ 5 mots | ✅ | ✅ | — | ✅ | ❌ | ✅ | ❌ |
| 9 | ≤ 3 blocs d'information | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| 10 | Sujet conforme à la ligne éditoriale | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |

**Aucun visuel ne passe les dix contrôles.** Le plus proche est V1, qui échoue
sur deux points corrigeables : la nuance de bleu et la photo générée.

---

## Le visuel de référence à produire en premier

Reprendre **V1 (recrutement)** en appliquant les corrections :

- Fond `#002C6A` exact au lieu de `#001C4C`
- Supprimer la photo générée → gabarit G5 variante B, typographique
- Conserver le bloc logo en en-tête (A1)
- Conserver la hiérarchie titre à deux niveaux (A2)
- Ajouter la mention des deux sites — Libreville et Paris — qui exprime le
  territoire 2

Une fois validé, ce visuel devient le premier modèle de cette bibliothèque.

---

## À faire

| Action | Qui | Priorité |
|---|---|---|
| Retirer les visuels avec logo Salesforce des supports actifs | Marketing | 🔴 Critique |
| Vérifier que V7 n'est plus en circulation (données fictives) | Marketing | 🔴 Critique |
| Produire le V1 corrigé comme premier modèle | Agent 03 | 🔴 Critique |
| Collecter les accords de droit à l'image de l'équipe | RH | 🟠 Haute |
| Vérifier le statut de partenariat Salesforce et le guide de marque associé | Direction | 🟠 Haute |
| Valider les polices officielles (Poppins / Inter recommandés) | Direction | 🟠 Haute |