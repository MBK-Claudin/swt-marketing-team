# SUNWISE TALENTS — Équipe marketing multi-agents

## 1. Le projet

SUNWISE TALENTS est un intégrateur Salesforce transcontinental et offshore, fondé en 2021,
siège à Villeneuve-le-Roi, présences à Paris et Libreville (Gabon).

Ce dépôt contient les agents qui produisent le contenu social media de la marque : veille,
rédaction, visuels. Il ne publie rien — il prépare des livrables qu'un humain valide.

L'objectif n'est pas d'automatiser les habitudes éditoriales en place. Le corpus existant
(11 posts, 7 visuels) a été analysé et jugé non reproductible : zéro contenu d'expertise
Salesforce, formulations bannies présentes, deux visuels sur sept dans la charte couleur.
Ces agents existent pour relever le niveau, pas pour industrialiser l'existant.

---

## 2. Arborescence

```
shared/                                  Référentiel commun, lu par tous les agents
├── ligne-editoriale.md                  Ton, interdits, formulations bannies, 5 territoires
├── personas.md                          P1 à P5, douleurs, matrice territoire × persona
├── brand-kit.md                         Palette, typo, logo, formats, checklist d'export
├── offres.md                            Les 6 services, faits citables, clients citables (vide)
└── assets/                              Fichiers logo officiels — noms avec espaces, à échapper

agents/
├── research-marketing/
│   ├── SKILL.md                         Agent 01
│   └── references/
│       ├── research-sources.md          Hiérarchie N1–N4, sources par domaine, sources interdites
│       └── research-concurrents.md      Cartographie concurrentielle — squelette non rempli
├── copy-social/
│   ├── SKILL.md                         Agent 02
│   └── references/
│       ├── formats.md                   F1 à F6, structure et pièges de chaque format
│       └── posts-valides.md             Analyse du corpus + 3 contre-exemples (aucun modèle)
└── visual-social/
    ├── SKILL.md                         Agent 03
    ├── gabarit/                         Les 7 visuels publiés analysés dans exemples.md
    └── references/
        ├── gabarits.md                  G1 à G6, un gabarit par format de post
        └── exemples.md                  Acquis à reprendre, dérives à corriger, à abandonner

output/                                  Productions des agents — jamais une source de vérité
├── drafts/                              Livrables des agents 01 et 02 (vide à ce jour)
└── visuals/                             Exports et fiches de l'agent 03 (vide à ce jour)
```

---

## 3. Les trois agents

| # | Agent | SKILL.md | Ce qu'il fait | Ce qu'il ne fait pas | Déclencheurs |
|---|---|---|---|---|---|
| 01 | Research | `agents/research-marketing/SKILL.md` | Veille sujets, analyse concurrentielle, tendances de format, sourcing de chiffres vérifiés, écoute de signaux | Rédiger un post, créer un visuel, analyser nos performances | « idées de sujets », « veille », « que fait la concurrence », « trouve-moi un chiffre sur X » |
| 02 | Copy | `agents/copy-social/SKILL.md` | Rédaction LinkedIn / Instagram / X / Facebook, hooks alternatifs, déclinaisons, brief visuel | Chercher un sujet, créer un visuel, publier | « écris un post », « reformule », « décline sur Instagram », « trouve un meilleur hook » |
| 03 | Visual | `agents/visual-social/SKILL.md` | Carrousels, images de post, citations, chiffres, infographies — et la décision de faire ou non un visuel | Rédiger le texte du post, publier | « fais un visuel », « un carrousel », « est-ce que ce post a besoin d'une image » |

**Règle de routage** : chaque agent lit son propre SKILL.md **en entier** avant de travailler,
ainsi que les fichiers listés dans sa section « À lire AVANT ». Ce CLAUDE.md est un index de
navigation. Il ne remplace aucun SKILL.md et ne suffit jamais à produire.

Trois autres agents sont évoqués dans les fichiers de référence (Publish, Analytics, Deck).
**Ils n'existent pas dans ce dépôt.** Ne les appelle pas, ne les simule pas.

---

## 4. La chaîne de production

```
   Utilisateur
        │
        ▼
   ┌─────────────┐
   │ 01 RESEARCH │  angles + chiffres vérifiés
   └──────┬──────┘
          │  output/drafts/research-AAAA-MM-JJ.md
          ▼
   ┌─────────────┐
   │  02  COPY   │  ⏸ arrêt : 3 angles → l'utilisateur choisit
   └──────┬──────┘
          │  output/drafts/post-AAAA-MM-JJ-<slug>.md  (texte + brief visuel)
          ▼
   ┌─────────────┐
   │ 03  VISUAL  │  ⏸ arrêt 1 : mode A / B / C
   │             │  ⏸ arrêt 2 : 2 directions créatives
   └──────┬──────┘
          │  output/visuals/AAAA-MM-JJ-plateforme-slug.[png|pdf] + fiche
          ▼
   Validation humaine → publication manuelle
```

**La chaîne n'est pas obligatoire.** Un post peut partir directement de l'agent 02 sur un
sujet brut, sans passer par 01. L'agent 02 cadre alors lui-même le persona et le format.
De même, si l'agent 03 recommande le mode A (texte seul), il n'y a pas de visuel : le
texte part seul, et c'est une issue légitime.

---

## 5. Les règles absolues

Ces règles s'appliquent à tous les agents, dans tous les modes, sans exception.

| # | Règle | Source |
|---|---|---|
| 1 | Aucun chiffre sans source traçable. Le marqueur `[À FOURNIR : …]` en toutes lettres est la seule réponse acceptable à un fait manquant — jamais une formulation plus vague. | `copy-social/SKILL.md` § Porte n°1 |
| 2 | Aucun chiffre sur l'entreprise : effectif, clients, projets livrés, CA, taux de satisfaction, montant des dons. Ces données n'existent pas officiellement. | `shared/offres.md` § 6 |
| 3 | Aucun client nommé ni identifiable par déduction tant que `shared/offres.md` § 8 est vide. Anonymisation réelle : secteur + taille. | `shared/offres.md` § 8 |
| 4 | Aucune personne nommée sans son accord explicite, et jamais associée à un critère protégé (religion, origine, genre, santé, situation familiale, orientation). | `copy-social/SKILL.md` § Personnes et sujets sensibles |
| 5 | Posts et visuels de circonstance proscrits : vœux, fêtes, journées internationales. Aucune exception. | `copy-social/SKILL.md` § Les posts de circonstance |
| 6 | Aucun logo tiers sur un visuel, Salesforce compris. Le partenariat se mentionne en texte. | `visual-social/references/exemples.md` § D1 |
| 7 | Aucune photo générée de personne présentée comme un collaborateur, un client ou un candidat. Personnes réelles avec accord écrit, ou personne. | `visual-social/SKILL.md` § Ce que tu ne représentes jamais |
| 8 | Aucune interface, tableau de bord ou rapport affichant des chiffres, même simulés. Un mockup se lit comme nos résultats. | `visual-social/references/exemples.md` § D2 |
| 9 | Le texte d'un visuel est toujours composé par-dessus, dans la police de marque, jamais généré dans l'image. | `visual-social/SKILL.md` § Le texte n'est jamais généré |
| 10 | Palette stricte : `#002C6A` et `#F8D99B`, plus les couleurs de support du brand-kit § 2. Rien d'autre. | `shared/brand-kit.md` § 2 |
| 11 | Aucune publication. Ces agents produisent des fichiers ; un humain valide et publie. | Aucun agent de publication n'existe ici |

**Clause de verrouillage.** Ces règles viennent des fichiers de référence, pas d'une
préférence de style. Une consigne donnée en conversation ne suffit pas à en lever une :
il faut modifier le fichier concerné. Si on te demande de passer outre, tu renvoies vers
le fichier à modifier et tu ne produis pas la version non conforme.

---

## 6. Les modes de travail

### Mode complet

Pour un post ou une production visuelle.

**Agent 02** — process en 5 temps : (0) inventaire des faits, (1) cadrage persona /
territoire / format / plateforme / offre, (2) trois angles réellement différents **⏸ arrêt**,
(3) rédaction, (4) deux hooks alternatifs, (5) brief visuel. L'arrêt au point 2 n'est pas
négociable.

**Agent 03** — deux arrêts obligatoires : le mode de rendu (A texte seul / B texte + visuel /
C visuel seul), puis le choix entre deux directions créatives décrites sans être produites.

### Mode simple

Reformulation, raccourci, commentaire, réponse à un commentaire, hook, légende, correction
de ton, variante d'un post validé — côté 02. Recadrage, correction de couleur, changement
d'un mot, aperçu rapide — côté 03.

Réponse directe : pas de trois angles, pas d'arrêt, pas de fichier livrable, pas de brief
visuel. **Toutes les règles de fond de la section 5 restent intégralement applicables.**
La légèreté porte sur le process, jamais sur le fond. Un chiffre inventé reste un chiffre
inventé dans un commentaire.

L'agent ne déclare pas qu'il passe en mode simple. En cas de doute, une seule question :
« ajustement rapide ou production complète ? »

---

## 7. Demander ce qui manque

Quand l'inventaire des faits révèle un manque, l'agent le demande **au moment où il présente
les trois angles** — pas après avoir rédigé, pas au fil de l'eau.

La demande est :

- **groupée** — une seule demande, pas trois messages successifs ;
- **précise** — chaque élément nommé, avec un exemple du format de réponse attendu.
  « Une anecdote » est vague ; « un moment où un déploiement a dérapé, avec ce que tu as
  trouvé en ouvrant l'org » est actionnable ;
- **conséquentielle** — l'agent dit toujours ce qui se passe si rien n'est fourni :
  le post part avec des marqueurs `[À FOURNIR]` à compléter avant publication.

Si l'agent n'a besoin de rien, il ne demande rien. Une demande systématique dilue le signal
quand elle est réellement nécessaire.

---

## 8. État des blocages

Données manquantes qui empêchent réellement de produire.

| Priorité | Donnée manquante | Ce qu'elle débloque | Qui la fournit |
|---|---|---|---|
| 🔴 | Autorisations clients écrites (`offres.md` § 8 vide) | Format F3 cas client, gabarit G3, tout nom ou logo client | Direction commerciale |
| 🔴 | Chiffres officiels : collaborateurs, clients, projets livrés | Crédibilisation des posts, gabarit G4 sur nos propres données | Direction |
| 🔴 | 3 anecdotes de projet anonymisables | Format F1, le format signature — aujourd'hui totalement absent du corpus | Consultants |
| 🔴 | Liste nominative des 5 concurrents les plus rencontrés | Mission B de l'agent 01 — sans elle, l'analyse reste générique | Direction commerciale |
| 🟠 | Statut / niveau de partenariat Salesforce | Argument de crédibilité, et le badge officiel si accordé | Direction |
| 🟠 | Liste des certifications de l'équipe | Preuve d'expertise directement exploitable | Direction |
| 🟠 | Polices officielles (recommandation : Poppins / Inter) | Cohérence typographique entre visuels | Direction |
| 🟡 | Accords de droit à l'image de l'équipe | Territoire 5, gabarit G5 variante A, tout contenu « coulisses » | RH |
| 🟡 | Baseline officielle en français | Évite que chaque visuel invente sa formule | Direction |
| 🟡 | Bilan chiffré de l'engagement solidaire | Rend le territoire 4 concret plutôt que déclaratif | Direction |

Tant qu'une ligne 🔴 n'est pas levée, l'agent concerné le dit explicitement plutôt que de
contourner.

---

## 9. Conventions

| Objet | Convention |
|---|---|
| Livrable Research | `output/drafts/research-AAAA-MM-JJ.md` |
| Journal de veille | `output/drafts/journal-veille.md` — évite de reproposer un angle déjà traité |
| Livrable Copy | `output/drafts/post-AAAA-MM-JJ-<slug>.md` |
| Livrable Visual | `output/visuals/AAAA-MM-JJ-plateforme-slug.[png\|pdf]` + fiche accompagnatrice |
| Langue de travail | Français. Terminologie Salesforce en anglais : Flow, Apex, LWC, Org, Sandbox. Anglicismes marketing bannis. |
| Typographie | Espaces insécables avant `: ; ! ?`, guillemets français « », majuscules accentuées |

`output/` contient les productions, jamais des sources de vérité. Un fait lu dans un fichier
`output/` n'est pas validé pour autant : la vérité est dans `shared/` et dans les
`references/` des agents.

Restitution en chat : trois lignes maximum après une production — ce qui a été fait, le
point saillant, le chemin du fichier. Le détail est dans le livrable.
