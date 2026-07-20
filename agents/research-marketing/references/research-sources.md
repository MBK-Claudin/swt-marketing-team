# Sources de veille — Agent 01 Research

> Référentiel des sources autorisées, hiérarchisées par fiabilité.
> L'agent Research privilégie toujours le niveau le plus haut disponible.

---

## Hiérarchie de fiabilité

| Niveau | Type de source | Utilisable pour citer un chiffre ? |
|---|---|---|
| **N1 — Primaire** | Documentation officielle, études avec méthodologie publiée, rapports d'organismes, publications réglementaires | ✅ Oui |
| **N2 — Secondaire fiable** | Presse spécialisée établie, analystes reconnus, publications académiques | ⚠️ Oui avec attribution explicite, après tentative de remontée à N1 |
| **N3 — Contextuel** | Blogs d'experts identifiés, retours de communauté, forums techniques | ❌ Pour comprendre un sujet, jamais pour citer un chiffre |
| **N4 — À écarter** | Contenu d'agence sans méthodologie, articles SEO, « études » sans échantillon, contenu généré non attribué | ❌ Jamais |

**Règle** : si un chiffre n'existe qu'en N2 et que la source primaire est
introuvable ou payante, le signaler en statut ⚠️ et formuler avec prudence
(« selon [organisme] »), ou l'écarter.

---

## Sources par domaine

### Salesforce — produit et écosystème

| Source | Niveau | Usage |
|---|---|---|
| Release Notes officielles Salesforce | N1 | Le socle de toute veille produit. 3 releases/an. |
| Salesforce Developers Blog | N1 | Changements techniques, dépréciations |
| Salesforce Admins Blog | N1 | Angles persona P2 |
| Documentation Salesforce (Help, Trailhead) | N1 | Vérification factuelle |
| Salesforce Newsroom / communiqués | N1 | Annonces stratégiques, avec recul critique (c'est de la com') |
| Trailblazer Community | N3 | Détecter les douleurs réelles des admins (excellent pour P2) |
| Blogs de MVP Salesforce identifiés | N3 | Angles techniques, jamais pour un chiffre |

**Rythme** : consulter les Release Notes à chaque saison (Spring / Summer / Winter).
C'est le rendez-vous éditorial le plus prévisible de l'année.

### Marché CRM et transformation digitale

| Source | Niveau | Usage |
|---|---|---|
| Cabinets d'analystes (Gartner, Forrester, IDC) | N1/N2 | Chiffres de marché. Souvent payant → utiliser les extraits publics et citer précisément |
| Études sectorielles publiées par des éditeurs | N2 | Biais commercial à signaler systématiquement |
| Presse IT / transformation digitale francophone | N2 | Actualité, jamais source unique pour un chiffre |
| Rapports institutionnels (INSEE, Commission européenne, France Num) | N1 | Données sur la digitalisation des entreprises françaises |

**Vigilance** : une étude publiée par un éditeur de CRM sur « le ROI du CRM »
n'est pas une source neutre. Utilisable, mais le biais doit être signalé
dans le livrable.

### Expérience client

| Source | Niveau | Usage |
|---|---|---|
| Études CX sectorielles avec méthodologie | N1/N2 | Benchmarks NPS, satisfaction |
| Publications académiques en marketing/CX | N1 | Fondements, rarement actualité |
| Associations professionnelles CX | N2 | Tendances, événements |

### Tech Afrique centrale et Gabon

| Source | Niveau | Usage |
|---|---|---|
| Organismes internationaux (Banque mondiale, UIT, BAD) | N1 | Connectivité, pénétration numérique, données macro |
| Institutions nationales gabonaises | N1 | Cadre réglementaire, chiffres officiels |
| Presse économique africaine établie | N2 | Actualité de l'écosystème |
| Structures d'accompagnement tech locales (incubateurs, hubs) | N2/N3 | Signaux terrain, événements |

**C'est le domaine où la donnée fiable est la plus rare.** Redoubler de rigueur :
beaucoup de chiffres circulent sans source. Ne rien publier qui ne soit remonté
à un organisme identifié.

### Réglementaire et conformité

| Source | Niveau | Usage |
|---|---|---|
| CNIL | N1 | RGPD, données personnelles, prospection B2B |
| Textes officiels européens | N1 | Souveraineté, hébergement, IA Act |
| Autorités de protection des données concernées | N1 | Selon le périmètre géographique |

### Formats et pratiques LinkedIn

| Source | Niveau | Usage |
|---|---|---|
| Publications officielles LinkedIn (blog, engineering) | N1 | Changements d'algorithme, formats |
| Études avec échantillon publié (≥ 1 000 posts) et méthodologie | N2 | Tendances de format |
| Contenu d'agence « growth » sans méthodologie | N4 | **Écarter systématiquement** |

**Ce domaine est le plus pollué.** La majorité du contenu « comment percer sur
LinkedIn » est recopiée, non sourcée et périmée. Appliquer le filtre N4 sans
état d'âme.

---

## Requêtes types

À adapter, jamais à copier telles quelles. Toujours ajouter l'année en cours.

**Veille produit Salesforce**
- `Salesforce release notes [saison] [année]`
- `Salesforce deprecation [année]`
- `Salesforce Agentforce nouveautés`
- `Salesforce pricing changement [année]`

**Marché**
- `CRM adoption entreprises France [année]`
- `taux échec projet CRM étude`
- `coût total possession CRM étude`
- `marché intégration Salesforce France`

**Expérience client**
- `expérience client B2B tendances [année]`
- `benchmark NPS secteur [année]`
- `adoption utilisateur CRM étude`

**Afrique centrale**
- `écosystème tech Gabon [année]`
- `connectivité internet Afrique centrale rapport`
- `talents développeurs Afrique marché`
- `outsourcing IT Afrique francophone`

**Réglementaire**
- `CNIL prospection B2B règles`
- `RGPD CRM données clients [année]`
- `hébergement données souveraineté [année]`

---

## Sources interdites

| Type | Motif |
|---|---|
| Contenu extrémiste, haineux, discriminatoire | Ligne éditoriale et éthique |
| Sites de contenu généré en masse sans attribution | Fiabilité nulle |
| Agrégateurs qui recopient sans citer la source primaire | Impossible de vérifier |
| Contenus piratés ou reproduits illégalement | Légalité |
| Réseaux sociaux comme source unique d'un fait | Non vérifiable |
| Sources politiques ou confessionnelles | Territoires interdits par la ligne éditoriale |

---

## Journal de veille

L'agent tient à jour `output/drafts/journal-veille.md` : chaque sujet déjà traité
y est consigné avec sa date, pour éviter de proposer deux fois le même angle à
trois semaines d'intervalle.

Format : `| date | sujet | angle | statut (proposé / rédigé / publié / abandonné) |`