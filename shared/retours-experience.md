---
name: retours-experience
description: Matière première anonymisée pour les formats F1 (retour d'expérience) et F3 (cas client). Projets Salesforce réels, sans nom de client. Lu par Research, Copy et Deck.
sources: [chat]
---

# Retours d'expérience — matière première anonymisée

> ⚠️ **Avertissement — à lire avant tout usage de ce fichier.**
>
> Toutes les fiches ci-dessous sont **anonymisées**. Aucun nom de client, aucune
> URL, aucun détail directement identifiant n'y figure. Cette anonymisation
> n'est pas un choix de style : `shared/offres.md` § 8 (clients citables) est
> **vide**, donc aucune autorisation écrite n'existe. Tant que c'est le cas, le
> référentiel interdit de nommer ou de rendre identifiable un client.
>
> **Passage en nominatif** : un projet ne peut devenir un cas client nominatif
> que si le client donne un **accord écrit daté**. Il faut alors d'abord remplir
> `shared/offres.md` § 8 — pas contourner par la conversation.
>
> **Chiffres** : seuls les chiffres **présents dans les sources** sont
> utilisables. Cet inventaire ne contient aucune métrique de résultat inventée
> (pas de « −40 % d'incidents », pas de « ×2 sur la productivité » : ces
> chiffres n'existent nulle part dans les sources). Quand une fiche indique
> « aucun » en chiffres disponibles, l'agent Copy laisse un marqueur
> `[À FOURNIR : résultat validé]` plutôt que d'en produire un.
>
> **Ce que ce fichier n'est pas** : ce n'est pas un recueil de modèles de posts
> (voir `agents/copy-social/references/posts-valides.md` pour ça). C'est de la
> matière brute : des projets réels dont Copy tire des anecdotes ancrées, et
> Research des angles reliés à du vécu plutôt qu'à la seule veille externe.

---

## Projets — client conseil finance

> Client anonymisé commun à ces huit fiches : **un cabinet de conseil en
> finance, audit et pilotage de la performance, utilisateur intensif de
> Salesforce** (Org central pour l'activité commerciale, les ressources, les
> projets et le reporting financier). Ne jamais reconstituer le nom, l'URL ou un
> détail permettant de l'identifier.

### Organigramme de contacts interactif

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : développement d'une nouvelle fonctionnalité (Lightning Web Component)
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (développement LWC/visualisation), touche P1 (identification des décideurs)
- **Le problème réel** : les équipes commerciales ne parvenaient pas à visualiser rapidement les relations hiérarchiques entre les contacts d'un compte, ni à repérer décideurs et interlocuteurs stratégiques.
- **Ce qui a été fait** : un LWC affichant la hiérarchie des contacts, avec un organigramme interactif généré dynamiquement et des connecteurs orthogonaux dessinés en SVG. Ajout d'un mode « contact stratégique » pour mettre en évidence les interlocuteurs clés, d'une modale de prise de rendez-vous pilotée par Flow, et de l'intégration des profils LinkedIn dans les fiches contacts.
- **La difficulté vécue** : prise en main de la bibliothèque D3.js ; gestion des conflits entre le cache du composant, le bouton de bascule (toggle) et la modale ; intégration correcte des URLs LinkedIn dans Salesforce ; navigation fluide malgré la complexité des arbres hiérarchiques.
- **Ce qu'on en retient** : intégrer une bibliothèque de dataviz (D3.js) dans un LWC pose d'abord un problème d'état — cache, toggle et modale se marchent dessus si le cycle de vie du composant n'est pas maîtrisé.
- **Technologies** : LWC, Apex, D3.js, Flow Builder, SVG
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : intégrer D3.js dans un LWC — ce qui casse quand le cache, le toggle et la modale partagent le même état
  - F2 : dessiner des connecteurs orthogonaux en SVG dans un composant Salesforce
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Tableaux de bord de reporting avancé

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : développement de composants de reporting avancés
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (développement), touche P1 et P3 (pilotage)
- **Le problème réel** : les équipes de pilotage voulaient analyser leur activité et leurs coûts salariaux avec un niveau de détail proche d'Excel, sans sortir de Salesforce.
- **Ce qui a été fait** : un tableau croisé dynamique interactif alimenté par un contrôleur Apex générant les colonnes dynamiquement grâce à la réflexion du schéma Salesforce. Gestion des filtres avancés et des regroupements, export Excel conservant style et mise en forme, optimisation sur de gros volumes de données.
- **La difficulté vécue** : clarifier les besoins fonctionnels avec les utilisateurs ; gérer des filtres en cascade complexes ; corriger des problèmes d'affichage lors de la réinitialisation des filtres ; consolider plusieurs sources de données (activités, coûts salariaux, production) ; gérer les cas où certaines productions n'avaient pas d'activité associée.
- **Ce qu'on en retient** : reconstituer un tableau croisé « comme Excel » dans Salesforce est d'abord un problème de consolidation de sources hétérogènes et de filtres en cascade — pas d'affichage.
- **Technologies** : LWC, Apex, SheetJS
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : reconstruire un tableau croisé dynamique « comme Excel » dans Salesforce — le vrai piège, ce sont les filtres en cascade
  - F2 : générer des colonnes dynamiquement avec la réflexion du schéma Salesforce en Apex
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Portail sous-traitants sur Experience Cloud

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : développement d'un portail Experience Cloud ouvert aux utilisateurs invités (Guest)
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (sécurité et architecture d'un portail public)
- **Le problème réel** : permettre à des sous-traitants de transmettre leurs informations administratives et leurs documents sans créer de compte Salesforce.
- **Ce qui a été fait** : un formulaire sécurisé sur Experience Cloud, un processus d'invitation automatisé via Screen Flow, la gestion du dépôt de documents, la mise à jour automatique des informations des sociétés, une validation des données côté client et côté serveur, et la sécurisation complète du parcours.
- **La difficulté vécue** : contourner les restrictions SOQL des utilisateurs Guest sur ContentVersion ; développer un objet miroir alimenté automatiquement par Trigger ; sécuriser le formulaire contre les attaques de type IDOR ; centraliser et restituer correctement les erreurs Apex côté interface.
- **Ce qu'on en retient** : les contraintes de l'utilisateur Guest (SOQL, ContentVersion, IDOR) ne sont pas un détail de fin de projet — elles structurent l'architecture entière d'un portail public dès la conception.
- **Technologies** : Experience Cloud, LWC, Apex, Flow Builder
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : un portail public sur Experience Cloud — pourquoi l'utilisateur Guest a réorienté toute l'architecture
  - F2 : contourner proprement les restrictions SOQL du Guest user sur ContentVersion (objet miroir alimenté par Trigger)
  - F2 : se protéger des attaques IDOR sur un formulaire Salesforce public
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Intégration d'une solution de signature électronique

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : intégration d'une solution tierce
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (intégration technique), touche P1 (déploiement d'un outil)
- **Le problème réel** : mettre en place la signature électronique directement depuis Salesforce.
- **Ce qui a été fait** : configuration complète d'Adobe Acrobat Sign, mise en place de l'authentification OAuth, personnalisation du nom de l'expéditeur, définition d'une architecture de provisioning multi-utilisateurs, tests des différents scénarios de signature.
- **La difficulté vécue** : comprendre l'architecture d'Adobe Acrobat Sign ; adapter la configuration aux contraintes du client ; résoudre la limitation « Send On Behalf Of », qui imposait une identité Adobe Sign distincte pour chaque utilisateur souhaitant personnaliser son nom d'expéditeur.
- **Ce qu'on en retient** : une intégration de signature électronique bute rarement sur l'OAuth ; le vrai obstacle est une limitation fonctionnelle de l'éditeur (ici « Send On Behalf Of ») qui force à revoir le modèle de provisioning.
- **Technologies** : Adobe Acrobat Sign, Salesforce, OAuth
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : intégrer la signature électronique à Salesforce — la limite « Send On Behalf Of » qu'on n'avait pas anticipée
  - F2 : provisioning multi-utilisateurs d'un outil tiers dans Salesforce — pourquoi OAuth ne suffit pas
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Audit technique et reprise d'un Org

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : audit technique et reprise d'organisation
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P1 et P2 (reprise d'Org et dette technique — angle directement lié à l'offre TMA)
- **Le problème réel** : évaluer l'état général d'un Org Salesforce afin d'identifier les axes d'amélioration techniques et organisationnels.
- **Ce qui a été fait** : analyse complète des classes Apex et des Flows, identification des erreurs récurrentes, analyse de la dette technique, étude de la répartition de la charge entre consultants, et rédaction d'un rapport d'audit détaillé avec recommandations.
- **La difficulté vécue** : analyser un volume important de code ; classifier 122 classes Apex selon leur niveau de couverture de tests ; prioriser les actions correctives.
- **Ce qu'on en retient** : auditer un Org, c'est d'abord classer. Trier 122 classes Apex par couverture de tests donne une carte de la dette bien plus actionnable qu'un score global.
- **Technologies** : Salesforce Inspector, Apex, Flow Builder
- **Chiffres disponibles** : 122 classes Apex analysées et classées selon leur couverture de tests
- **Angles de post identifiés** :
  - F1 : reprendre un Org qu'on ne connaît pas — la méthode d'audit qui commence par classer 122 classes Apex
  - F2 : mesurer la dette technique d'un Org Salesforce — couverture de tests, Flows, erreurs récurrentes
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Tierce Maintenance Applicative (TMA)

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : Tierce Maintenance Applicative (correctif et évolutif)
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P1 et P2 (stabilité de plateforme, douleur « l'intégrateur a livré et disparu »)
- **Le problème réel** : assurer la stabilité de la plateforme et accompagner les utilisateurs dans leurs demandes d'évolution, en continu.
- **Ce qui a été fait** : résolution de nombreux incidents de production — synchronisation Einstein Activity Capture, anomalies d'intégration avec un progiciel métier tiers, Batch Apex dépassant les limites de gouvernance, doublons de clés composites, classes de tests défaillantes, configuration DKIM du domaine — et évolutions fonctionnelles sur plusieurs LWC.
- **La difficulté vécue** : identifier rapidement l'origine des anomalies ; comprendre des processus métier parfois peu documentés ; corriger des bugs ayant des effets en cascade ; maintenir la stabilité de la plateforme tout en déployant des évolutions.
- **Ce qu'on en retient** : en TMA, le coût n'est pas dans le correctif mais dans le diagnostic. Des processus peu documentés et des effets en cascade rendent l'origine d'une anomalie difficile à isoler.
- **Technologies** : Apex, LWC, Einstein Activity Capture, intégration avec un progiciel métier tiers
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : TMA — pourquoi un Batch Apex qui dépasse les limites de gouvernance est un symptôme, pas la cause
  - F2 : les incidents qu'on retrouve le plus souvent en reprise de TMA (Einstein Activity Capture, doublons de clés composites, DKIM)
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Module de projection financière

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : développement et évolution d'une fonctionnalité métier
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (développement Apex, logique d'appariement de données)
- **Le problème réel** : permettre aux consultants de simuler différents scénarios financiers en comparant données réelles et données projetées.
- **Ce qui a été fait** : un moteur de projection (chiffre d'affaires projeté, masse salariale, résultat brut) alimenté par les données réelles (contrats, production, coûts salariaux), un système complet de gestion des scénarios, la sauvegarde/restauration via des fichiers Excel multi-feuilles, et un mécanisme de comparaison entre un scénario sauvegardé et les données Salesforce actuelles (détection des éléments créés, modifiés ou supprimés).
- **La difficulté vécue** : concevoir un mécanisme fiable de sauvegarde des simulations dans des fichiers Excel ; garantir la qualité de l'appariement entre Salesforce et les fichiers importés ; gérer les cas d'IDs manquants, différences de casse, espaces ou valeurs absentes ; reconstituer fidèlement un scénario historique sans recalculer les données dans Apex. L'appariement reposait sur plusieurs niveaux de correspondance : ID Salesforce, nom, identifiant métier, hash de comparaison.
- **Ce qu'on en retient** : comparer un fichier importé à des données Salesforce vivantes est un problème d'appariement (matching). Un seul critère ne suffit jamais — il faut une cascade ID → nom → identifiant métier → hash.
- **Technologies** : Apex, LWC, Salesforce Files, SheetJS / XLSX
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : apparier un import Excel à des données Salesforce vivantes — la cascade de correspondances qui a sauvé la fiabilité
  - F2 : détecter créé / modifié / supprimé entre un fichier sauvegardé et un Org — hash et clés métier
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

### Gestion des disponibilités et du staffing

- **Client anonymisé** : cabinet de conseil en finance, audit et pilotage de la performance, utilisateur intensif de Salesforce
- **Type de projet** : développement d'une nouvelle fonctionnalité
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P2 (développement LWC, ergonomie et performance d'un écran dense)
- **Le problème réel** : centraliser le suivi de la disponibilité des consultants afin d'améliorer le staffing et l'affectation des ressources.
- **Ce qui a été fait** : un module de gestion des disponibilités suivant salariés, indépendants et candidats, avec un tableau récapitulatif, une classification automatique par statut (disponible immédiatement, sous un mois, au-delà, indéfinie, en mission), des cartes consultants (pôle, compétences, missions, client actuel, positionnements) et un système de filtres avancés.
- **La difficulté vécue** : concevoir une interface ergonomique malgré un volume important d'informations ; trouver l'équilibre entre niveau de détail et lisibilité ; optimiser les performances de chargement des tableaux et des cartes consultants ; offrir une vision synthétique tout en permettant un accès rapide au détail.
- **Ce qu'on en retient** : sur un écran dense de staffing, la difficulté n'est pas fonctionnelle mais d'ergonomie et de performance. L'équilibre entre synthèse et détail conditionne l'adoption.
- **Technologies** : Apex, LWC
- **Chiffres disponibles** : aucun
- **Angles de post identifiés** :
  - F1 : un écran de staffing dense — comment on a arbitré entre lisibilité et exhaustivité
  - F2 : performances de chargement d'un tableau LWC volumineux — les leviers concrets
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

---

## Projets — client e-commerce

> Client anonymisé de cette fiche : **un acteur e-commerce (client du secteur du
> retail en ligne)**. Ne jamais reconstituer le nom, l'URL ou un détail
> identifiant. La plateforme e-commerce impliquée (PrestaShop) est un progiciel
> répandu : elle décrit la nature technique du projet, pas l'identité du client.

### Automatisation des process et intégration CRM ↔ e-commerce

- **Client anonymisé** : acteur e-commerce (secteur du retail en ligne)
- **Type de projet** : automatisation des processus métier et intégration Salesforce ↔ plateforme e-commerce (PrestaShop)
- **Territoire éditorial** : 1 (Salesforce en contexte réel)
- **Persona visé** : P1 (transformation des processus, réduction des tâches manuelles) et P2 (Flow en cascade, intégration API)
- **Le problème réel** : des processus commerciaux très manuels, une qualité de données faible, et des informations clients/commandes non synchronisées entre Salesforce et la plateforme e-commerce.
- **Ce qui a été fait** : automatisation des processus métier via Record-Triggered Flow (création d'enregistrements, mises à jour selon les événements métier, notifications, tâches, relances commerciales) ; intégration bidirectionnelle entre Salesforce et la plateforme e-commerce (clients, comptes, contacts, commandes, produits, livraison, statuts) ; règles de validation, normalisation et nettoyage des données ; gestion des erreurs d'intégration avec journalisation et reprise.
- **La difficulté vécue** : les deux systèmes ne partageaient pas le même modèle de données (mise en place de correspondances entre objets, transformations, cas particuliers) ; gestion des doublons de clients créés depuis plusieurs canaux ; éviter les boucles infinies dans des automatisations qui s'exécutaient en cascade et contrôler l'ordre d'exécution des traitements ; gérer les échecs d'appels entre les deux systèmes (données invalides, indisponibilité temporaire, erreurs réseau) via journalisation et reprise.
- **Ce qu'on en retient** : une intégration e-commerce ↔ CRM se joue sur trois fronts rarement anticipés — le mapping de deux modèles de données différents, une stratégie de dédoublonnage définie tôt, et des Flow en cascade maîtrisés pour éviter les boucles.
- **Technologies** : Salesforce Sales Cloud, Flow (Record-Triggered), Apex, SOQL, API REST Salesforce, API PrestaShop, JSON, Webhooks, Git
- **Chiffres disponibles** : aucun (les bénéfices sont décrits qualitativement dans la source, sans aucune valeur chiffrée)
- **Angles de post identifiés** :
  - F1 : intégrer Salesforce et une plateforme e-commerce — pourquoi le mapping des modèles de données prend plus de temps que le code
  - F1 : automatisations en cascade — comment on a évité les boucles infinies de Flow
  - F2 : dédoublonnage clients multi-canal dans Salesforce — définir la stratégie avant d'écrire le premier Flow
  - F2 : gérer les erreurs d'une intégration API bidirectionnelle — journalisation et reprise
- **Statut de citation** : anonymisé (nominatif interdit tant que offres.md § 8 est vide)

---

## Clients sans retour d'expérience documenté

- Un cabinet de conseil international en performance opérationnelle (client
  actuel) : aucun projet documenté à ce jour. À compléter si des missions sont
  décrites ultérieurement.

---

## Récapitulatif des angles exploitables

> Les angles F1 issus d'une difficulté réellement vécue sont placés en haut :
> ce sont les plus forts pour le format signature F1. Les angles F2 (décryptage
> technique) suivent.

| # | Angle | Format | Persona | Territoire | Difficulté source |
|---|---|---|---|---|---|
| 1 | Apparier un import Excel à des données Salesforce vivantes — la cascade de correspondances | F1 | P2 | 1 | oui |
| 2 | Un portail public sur Experience Cloud — l'utilisateur Guest réoriente toute l'architecture | F1 | P2 | 1 | oui |
| 3 | Intégrer la signature électronique — la limite « Send On Behalf Of » non anticipée | F1 | P1/P2 | 1 | oui |
| 4 | Reprendre un Org inconnu — l'audit qui commence par classer 122 classes Apex | F1 | P1/P2 | 1 | oui |
| 5 | Automatisations en cascade — comment on a évité les boucles infinies de Flow | F1 | P1/P2 | 1 | oui |
| 6 | Intégrer Salesforce et une plateforme e-commerce — le mapping des modèles avant le code | F1 | P1/P2 | 1 | oui |
| 7 | TMA — un Batch Apex qui dépasse les limites de gouvernance est un symptôme, pas la cause | F1 | P1/P2 | 1 | oui |
| 8 | Intégrer D3.js dans un LWC — cache, toggle et modale qui partagent le même état | F1 | P2 | 1 | oui |
| 9 | Reconstruire un tableau croisé « comme Excel » — le vrai piège, les filtres en cascade | F1 | P2 | 1 | oui |
| 10 | Un écran de staffing dense — arbitrer entre lisibilité et exhaustivité | F1 | P2 | 1 | oui |
| 11 | Contourner les restrictions SOQL du Guest user sur ContentVersion (objet miroir + Trigger) | F2 | P2 | 1 | oui |
| 12 | Se protéger des attaques IDOR sur un formulaire Salesforce public | F2 | P2 | 1 | oui |
| 13 | Détecter créé / modifié / supprimé entre un fichier sauvegardé et un Org — hash et clés métier | F2 | P2 | 1 | oui |
| 14 | Mesurer la dette technique d'un Org — couverture de tests, Flows, erreurs récurrentes | F2 | P1/P2 | 1 | oui |
| 15 | Les incidents les plus fréquents en reprise de TMA (EAC, doublons de clés composites, DKIM) | F2 | P2 | 1 | oui |
| 16 | Dédoublonnage clients multi-canal — définir la stratégie avant le premier Flow | F2 | P2 | 1 | oui |
| 17 | Gérer les erreurs d'une intégration API bidirectionnelle — journalisation et reprise | F2 | P2 | 1 | oui |
| 18 | Provisioning multi-utilisateurs d'un outil tiers — pourquoi OAuth ne suffit pas | F2 | P2 | 1 | oui |
| 19 | Générer des colonnes dynamiquement avec la réflexion du schéma Salesforce en Apex | F2 | P2 | 1 | oui |
| 20 | Dessiner des connecteurs orthogonaux en SVG dans un composant Salesforce | F2 | P2 | 1 | non |
| 21 | Performances de chargement d'un tableau LWC volumineux — les leviers concrets | F2 | P2 | 1 | oui |
