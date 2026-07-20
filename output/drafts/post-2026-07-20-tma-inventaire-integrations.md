# Post — TMA : l'inventaire des intégrations avant le retrait de SOAP login()

**Persona** : P2 (principal), P1 (secondaire)
**Territoire** : 1 — Salesforce en contexte réel
**Format** : F2 — Décryptage technique
**Plateforme(s)** : LinkedIn (principal), X (déclinaison)
**Offre mise en avant** : Tierce Maintenance Applicative — seule
**Source de l'angle** : `research-2026-07-20-p2.md`, sujet 1, angle validé par l'utilisateur

> **Pourquoi F2 et non F1** : le retour d'expérience aurait mieux servi ce sujet, mais il
> exige un ancrage vécu réel et aucune anecdote n'a été fournie. Règle de la Porte n°1 :
> un F1 sans anecdote devient un F2, jamais un F1 inventé.

---

## Version finale — LinkedIn

En Summer '27, l'appel SOAP login() cesse de fonctionner.

La question n'est pas de savoir comment migrer. C'est de savoir ce qui, chez vous, s'en sert encore.

La migration vers OAuth et les External Client Apps est documentée. Ce n'est pas là que ça coince.

Ce qui coince, c'est l'inventaire.

login() permet à une application de s'authentifier avec un identifiant, un mot de passe et un token. Il disparaît des versions 31.0 à 64.0, et il est déjà indisponible à partir de la v65.0.

Dans un org de cinq ans, ce mode d'authentification est partout. Des exports planifiés. Des connecteurs installés puis oubliés. Des scripts écrits par un prestataire qui n'est plus là.

Aucun n'apparaît dans une liste quelque part. On les découvre quand ils cassent.

[À FOURNIR : exemple réel — secteur, taille, ce qui se connectait, comment on l'a découvert]

C'est à ça que sert une maintenance applicative. Pas à réparer après coup, mais à tenir la carte de ce qui tourne pendant que le socle bouge — trois releases par an.

Quand personne n'a ce travail dans ses attributions, la carte n'existe pas.

Il reste moins d'un an pour la dresser.

Sur votre org, vous sauriez dire combien d'intégrations s'authentifient encore avec un mot de passe et un token ?

#Salesforce #SalesforceAdmin #TMA #CRM

**Longueur** : 1 288 caractères (marqueur `[À FOURNIR]` inclus — à recompter après remplacement)
**Hook (avant troncature)** : 159 caractères
**Lien en premier commentaire** : https://developer.salesforce.com/blogs/2026/06/the-salesforce-developers-guide-to-the-summer-26-release

---

## Hooks alternatifs

1. *(axe : la contre-intuition sur l'offre)*
   « La maintenance applicative ne sert pas à réparer. Elle sert à savoir ce qui va casser
   avant que ça casse. Summer '27 est un bon test. »

2. *(axe : la conséquence métier — bascule le post vers P1)*
   « Le jour où une intégration Salesforce cesse de s'authentifier, ce n'est pas un incident
   technique. C'est une chaîne de données à l'arrêt, et personne pour dire laquelle. »

---

## Déclinaisons

### X

> SOAP login() disparaît en Summer '27. Déjà indisponible en v65.0.
>
> Migrer vers OAuth est documenté. Le problème est ailleurs : savoir quelles intégrations
> s'authentifient encore avec un mot de passe et un token.
>
> Dans un org de cinq ans, personne n'a cette liste.

### Instagram — **non recommandé**

Post technique visant P2. `SKILL.md` § Déclinaison multi-plateforme : un post technique P2
n'a rien à faire sur Instagram. Ne pas décliner.

### Facebook — **non recommandé**

Même motif. Aucune audience P2 sur ce canal.

---

## Brief visuel (→ agent 03)

- **Type** : image simple
- **Format** : LinkedIn image de post — 1200 × 627 px (`brand-kit.md` § 6)
- **Message clé** : une échéance datée tombe sur un inventaire que personne n'a fait
- **Texte à intégrer** :
  - Ligne 1 : « SOAP login() »
  - Ligne 2 : « Summer '27 »
  - Ligne 3, plus petit : « Vous savez ce qui s'en sert ? »
- **Traitement** : voix visuelle « veille / décryptage » (`brand-kit.md` § 7) — fond blanc,
  structure éditoriale, titre bleu `#002C6A`, filet sable `#E0B96E`
- **Ambiance** : sobre et technique. Le motif du lien (arc, flux) du § 5 peut servir à
  suggérer une connexion interrompue, en très faible opacité.
- **Ce qu'il ne faut pas** :
  - Aucune capture d'écran Salesforce, aucun mockup d'interface, aucun tableau de bord —
    même simulé (règle absolue n° 8)
  - Aucun logo Salesforce ni logo d'éditeur d'intégration (règle absolue n° 6)
  - Le visuel ne résume pas le post : il porte l'échéance, rien d'autre
  - Le texte est composé par-dessus dans la police de marque, jamais généré dans l'image
    (règle absolue n° 9)

---

## Éléments à fournir

- [ ] `[À FOURNIR : exemple réel d'intégration non documentée trouvée en reprise d'org]` —
      secteur, taille, ce qui se connectait, comment on l'a découvert. C'est le seul
      marqueur du post, et c'est lui qui le rend reconnaissable comme un post Sunwise.
      Sans lui, le post reste juste et publiable, mais générique.
- [ ] **Vérification avant publication** : la date exacte du retrait (1ᵉʳ juin 2027) circule
      largement mais n'a pas pu être confirmée sur `help.salesforce.com` depuis cet
      environnement. Le post dit « Summer '27 » et non la date — c'est volontaire. Ne pas
      ajouter la date sans l'avoir vérifiée.

---

## Traçabilité des faits

| Élément du post | D'où il vient |
|---|---|
| Retrait de SOAP login() en Summer '27 | Salesforce Developers Blog (N1), via `research-2026-07-20-p2.md` — statut ✅ Vérifié |
| Versions 31.0 à 64.0 concernées, indisponible dès la v65.0 | Idem, ✅ Vérifié |
| Migration vers OAuth et External Client Apps | Idem, ✅ Vérifié |
| Définition de login() (identifiant + mot de passe + token) | Idem, ✅ Vérifié |
| Trois releases Salesforce par an | `shared/offres.md` § 2.3 et `shared/personas.md` § P2 |
| « moins d'un an » | Calcul à partir de juillet 2026 → Summer '27 (≈ juin 2027). Volontairement approximatif plutôt que faussement précis. |
| Description de la TMA | `shared/offres.md` § 2.3 |
| « org de cinq ans », « prestataire qui n'est plus là » | **Aucune source** — ce sont des cas de figure génériques, pas des faits présentés comme nôtres. Formulés au conditionnel implicite, jamais comme un projet vécu. |

**Vérification** : aucun chiffre sur l'entreprise, aucun client, aucune anecdote non fournie.

---

## Contrôle qualité

- [x] Longueur dans la cible (1 288 / 1000–1300 pour un F2) — vérifiée par comptage, pas estimée
- [x] Hook sous 200 caractères (159) — vérifié par comptage
- [x] Aucune formulation bannie
- [x] Aucun chiffre non sourcé
- [x] Aucun client nommé ni identifiable
- [x] Une seule offre (TMA)
- [x] Une seule idée (l'inventaire, pas la migration)
- [x] CTA précis, répondable par un pair depuis son vécu
- [x] 4 hashtags
- [x] Pas de gras Unicode
- [x] Pas de lien dans le corps — mis en premier commentaire
- [x] Aucun emoji
- [x] Section « quand ne pas l'appliquer » — portée par « la migration est documentée, ce n'est pas là que ça coince » : le post dit explicitement ce dont il ne s'occupe pas
- [x] Test de signature : le « nous » implicite d'équipe, l'angle terrain, la question technique finale — reconnaissable
