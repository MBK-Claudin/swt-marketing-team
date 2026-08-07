# Formats de post — SUNWISE TALENTS

> Référence de l'agent 02 Copy. Chaque post doit correspondre à un de ces
> six formats. Un post hors format est un post sans structure.

---

## Vue d'ensemble

| # | Format | Territoire | Persona | Fréquence cible |
|---|---|---|---|---|
| F1 | Retour d'expérience | 1, 2 | P1, P2 | 1 / semaine |
| F2 | Décryptage technique | 1 | P2 | 1 / semaine |
| F3 | Cas client anonymisé | 1, 3 | P1, P3 | 2 / mois |
| F4 | Chiffre / donnée | 3 | P1, P3 | 2 / mois |
| F5 | Coulisses & équipe | 5, 2 | P4 | 2 / mois |
| F6 | Engagement & RSE | 4 | P5, P4 | 1 / mois |
| F7 | Circonstance & moments d'équipe | aucun (hors territoire) | P4, P5 | 2 / mois max (quota) |

---

## F1 — Retour d'expérience

**Le format signature de Sunwise.** C'est celui qui incarne le mieux « on parle
aussi de ce qui a raté ».

**Structure**
```
[HOOK — le problème, brut, sans contexte]

[CONTEXTE — 2-3 lignes : chez qui (anonymisé), quand, quel enjeu]

[CE QUI S'EST PASSÉ — 3-5 lignes, chronologique]

[CE QU'ON EN RETIENT — 2-3 points courts]

[CTA — une question à ceux qui ont vécu la même chose]

#hashtags
```

**Longueur** : 900–1300 caractères

**Ce qui fait la différence** : commencer par le problème, pas par le contexte.
Le lecteur doit reconnaître sa propre douleur dans la première ligne.

**Règles spécifiques**
- L'échec ou la difficulté doit être réel, jamais fabriqué
- Anonymisation stricte du client
- On assume notre part de responsabilité quand elle existe — c'est ce qui rend
  le post crédible
- Jamais de morale condescendante en conclusion

**Pièges**
- Le faux échec (« notre seule erreur a été d'être trop rigoureux ») — inaudible
- Le retour d'expérience qui finit en argumentaire commercial
- Le contexte trop long avant d'arriver au problème

---

## F2 — Décryptage technique

**Le format qui construit la crédibilité auprès de P2.** Peu de conversions
directes, mais c'est lui qui fait dire « eux, ils savent de quoi ils parlent ».

**Structure**
```
[HOOK — une affirmation technique nette ou contre-intuitive]

[LE CONSTAT — pourquoi c'est un sujet, 2 lignes]

[L'EXPLICATION — 4-6 lignes ou liste courte]
   ↳ Le raisonnement, pas juste la conclusion

[QUAND L'APPLIQUER / QUAND NE PAS L'APPLIQUER]
   ↳ C'est cette section qui distingue un décryptage d'une reprise de doc

[CTA — une question technique à des pairs]

#hashtags
```

**Longueur** : 1000–1300 caractères

**Ce qui fait la différence** : la section « quand ne PAS l'appliquer ».
N'importe qui peut recopier la documentation. Peu de gens disent quand une
solution est un mauvais choix.

**Règles spécifiques**
- Ne jamais écrire sur une fonctionnalité qu'on n'a pas réellement pratiquée
- Les termes Salesforce restent en anglais (Flow, Apex, LWC, Org, Sandbox)
- Si le post vise aussi P1, expliquer le terme au premier usage
- Pas de capture d'écran avec de la donnée client réelle

**Pièges**
- La paraphrase de la documentation officielle
- Le « 5 astuces » sans raisonnement
- Le jargon non expliqué quand le persona est mixte

---

## F3 — Cas client anonymisé

**Le format qui convertit.** C'est celui que P1 lit en se demandant « est-ce
qu'ils pourraient faire ça pour moi ».

**Structure**
```
[HOOK — la situation de départ, ou le résultat obtenu]

[LE CONTEXTE — secteur, taille, enjeu. Anonymisé.]

[LE PROBLÈME — ce qui bloquait concrètement]

[CE QU'ON A FAIT — 3-4 lignes, sans jargon inutile]

[LE RÉSULTAT — chiffré si possible, sinon qualitatif et honnête]

[CE QUI EST TRANSPOSABLE — pour que le lecteur s'y projette]

[CTA]

#hashtags
```

**Longueur** : 1000–1300 caractères

**⚠️ CONTRAINTE BLOQUANTE ACTUELLE**
`shared/offres.md` § 8 est vide : aucun client n'a donné d'autorisation écrite.
Tant que c'est le cas :
- Anonymisation obligatoire et **réelle** (secteur + taille uniquement)
- Interdit : « un grand acteur français du retail » si ça permet de deviner
- Aucun chiffre de résultat qui ne soit validé par la direction
- Le post doit être relu par la direction avant publication

**Règles spécifiques**
- Un résultat non chiffré honnête vaut mieux qu'un chiffre inventé
- Toujours inclure ce qui a été difficile — un cas 100 % lisse n'est pas crédible
- Une seule offre mise en avant

---

## F4 — Chiffre / donnée

**Le format le plus rapide à produire et le plus partagé.** Un chiffre, un
commentaire, une implication.

**Structure**
```
[HOOK — le chiffre, brut, avec sa source]

[POURQUOI CE CHIFFRE COMPTE — 2-3 lignes]

[CE QU'ON OBSERVE SUR LE TERRAIN — notre lecture, 3-4 lignes]
   ↳ C'est ici qu'on apporte de la valeur, pas dans le chiffre lui-même

[L'IMPLICATION CONCRÈTE — 1-2 points]

[CTA]

#hashtags
```

**Longueur** : 700–1000 caractères

**⚠️ Le chiffre doit venir d'un fichier Research avec statut ✅ Vérifié.**
Aucune exception. La source est citée dans le texte du post, pas seulement en
commentaire.

**Ce qui fait la différence** : la section « ce qu'on observe sur le terrain ».
Relayer un chiffre n'apporte rien. Le confronter à notre expérience, si.

**Visuel** : ce format demande un visuel où le chiffre occupe 60 % de la
surface (voir `shared/brand-kit.md` § 7).

---

## F5 — Coulisses & équipe

**Le format qui humanise et qui recrute.**

**Structure**
```
[HOOK — une situation concrète, pas une annonce]

[LE CONTEXTE — qui, où, quoi]

[LE RÉCIT — 4-6 lignes, à hauteur d'humain]

[CE QUE ÇA DIT DE NOUS — 1-2 lignes, sans autocélébration]

[CTA — question ouverte, ou mention d'un poste ouvert]

#hashtags
```

**Longueur** : 700–1100 caractères

**⚠️ CONTRAINTE ACTUELLE**
Aucune photo d'équipe avec accord de droit à l'image n'est disponible
(`shared/brand-kit.md` § 9). Ce format est donc limité au texte, ou au visuel
graphique, tant que les accords ne sont pas collectés.

**Règles spécifiques**
- Jamais de storytelling fabriqué
- Le nom d'un collaborateur uniquement avec son accord
- Le territoire 2 (pont France-Afrique) s'exprime très bien ici : le quotidien
  d'une équipe sur deux continents est un contenu que peu peuvent produire
- Pas de « nous sommes fiers de » en ouverture

**Variante recrutement**
```
[HOOK — le contexte réel du poste, pas l'intitulé]
[CE QU'ON CHERCHE — 3-4 points concrets]
[CE QU'ON OFFRE — honnête, y compris les contraintes]
[COMMENT POSTULER]
```
Une offre d'emploi publiée telle qu'elle sort du service RH ne sera pas lue.

---

## F6 — Engagement & RSE

**Le format le plus risqué.** Mal fait, il détruit la crédibilité de tout le reste.

**Structure**
```
[HOOK — l'action, au passé, sans emphase]

[LE CONTEXTE — avec qui, où, pourquoi]

[CE QUI A ÉTÉ FAIT — concret, factuel]

[CE QUE ÇA A CHANGÉ — sobrement]

[Éventuellement : la suite]

#hashtags
```

**Longueur** : 600–1000 caractères

**Règles spécifiques — les plus strictes de tous les formats**
- **Au passé et au concret.** Ce qui a été fait, jamais ce qu'on compte faire.
- **Aucun appel commercial.** Pas de lien vers nos offres, pas de CTA de
  conversion.
- **Aucune récupération.** Le post ne dit pas « choisissez-nous parce qu'on est
  engagés ».
- **Photos** : uniquement avec accord de l'association et respect du droit à
  l'image des personnes. Ne jamais publier de photo de bénéficiaires
  identifiables.
- Partenaire à citer : « Rayons d'Espoir et d'Amour »
- Pas de chiffre de don tant qu'il n'est pas validé par la direction

**Le test** : est-ce que ce post serait publié même s'il ne rapportait rien
commercialement ? Si non, il ne doit pas sortir.

---

## F7 — Circonstance & moments d'équipe

**Autorisé sous conditions** depuis la décision de la direction (voir
`shared/ligne-editoriale.md` § 5 bis et `SKILL.md` § « Les posts de
circonstance »). Ce format marque un moment — vœux, fête du travail, team
building — **uniquement s'il porte une substance concrète**.

**Structure**
```
[HOOK — ancré dans un fait, pas dans le vœu lui-même]

[LE MOMENT — de quoi il s'agit, brièvement]

[L'ENSEIGNEMENT OU LE BILAN — le concret : ce qui a été fait, appris, décidé]

[éventuellement : la projection — au concret, jamais une intention creuse]

#hashtags
```

**Longueur** : 500–900 caractères

**Règles spécifiques — ce sont les conditions de la décision**
- **Substance obligatoire.** Un vœu creux ne sort pas. Le post s'ancre dans un
  fait, un bilan, un enseignement. C'est la différence entre « belle année pleine
  d'innovation » et « voilà ce qu'on a livré cette année, et ce qu'on en retient ».
- **Quota : 2 par mois maximum.** Ces posts ne prennent pas la place du contenu
  de fond (cible : 40 % de territoire Salesforce, formats F1/F2).
- **Au passé et au concret.** Pas de déclaration d'intention au futur non adossée
  à un fait.
- **Aucun appel commercial.**
- **Cas B proscrit.** Ne nomme ni ne rend identifiable une personne sur un
  critère protégé (religion, origine, genre, santé, situation familiale,
  orientation). Ces sujets se traitent à l'échelle de l'entreprise. Voir
  `SKILL.md` § « Personnes et sujets sensibles ».

**Ce format ne porte pas de territoire éditorial propre** : il s'ajoute dans la
limite du quota, sans réduire la part des territoires 1 à 5.

**Le test** : est-ce que ce post apprend ou rappelle quelque chose de concret au
lecteur ? Si ce n'est qu'un vœu, il ne sort pas.

---

## Choix du format — arbre de décision

```
Le sujet vient d'un projet réel qu'on a vécu ?
├─ OUI, avec une difficulté → F1 Retour d'expérience
└─ OUI, avec un résultat client → F3 Cas client (⚠️ anonymisation)

Le sujet est une fonctionnalité, un concept technique ?
└─ F2 Décryptage technique

Le sujet part d'une donnée externe sourcée ?
└─ F4 Chiffre / donnée

Le sujet concerne l'équipe, un poste, notre façon de travailler ?
└─ F5 Coulisses & équipe

Le sujet concerne nos actions solidaires ?
└─ F6 Engagement & RSE

Le sujet marque un moment de circonstance (vœux, fête du travail, team building) ?
└─ F7 Circonstance — uniquement avec substance, dans le quota de 2/mois,
   cas B exclu (jamais nommer une personne sur un critère protégé)

Aucun de ces cas ?
└─ Le sujet n'est probablement pas pour nous. Retour à l'agent Research.
```

---

## Répartition cible sur un mois (12 posts LinkedIn)

| Format | Nombre | Territoire dominant |
|---|---|---|
| F1 Retour d'expérience | 4 | 1, 2 |
| F2 Décryptage technique | 4 | 1 |
| F3 Cas client | 1 | 1, 3 |
| F4 Chiffre / donnée | 1 | 3 |
| F5 Coulisses & équipe | 1 | 5 |
| F6 Engagement & RSE | 1 | 4 |

Ces 12 posts de fond restent le socle. **F7 (circonstance) s'ajoute par-dessus,
dans la limite de 2 par mois**, et ne remplace aucun de ces 12 : il ne réduit
donc jamais la part de F1/F2 (le cœur territoire Salesforce). Un mois sans moment
de circonstance à marquer est un mois à zéro F7 — le quota est un plafond, pas
un objectif à remplir.

Cette répartition reflète les pourcentages de `shared/ligne-editoriale.md` § 6.
Elle est indicative : l'agent Analytics l'ajustera avec les données réelles
après six semaines.