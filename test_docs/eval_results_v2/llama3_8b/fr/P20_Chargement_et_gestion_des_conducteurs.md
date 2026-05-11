---
title: Chargement et gestion des conducteurs
shortTitle: Conducteurs
intro: Apprenez à créer, importer et maintenir la base de conducteurs dans GoalBus, consulter son profil opérationnel et laisser un modèle fiable avant de passer à l'adoption, les règles et le calcul de Rostering.
contentType: how-tos
versions:
  - '*'
---

## Création ou importation de la plantilla de conducteurs

Avant de parler de règles de Rostering, d'absences ou d'affectation de tours, vous devez avoir une base fiable de conducteurs. Dans GoalBus, la gestion de conducteurs agit comme la source principale de vérité pour l'opération humaine : elle permet de combiner la création manuelle et la charge massive, et concentre l'identité, l'affiliation au dépôt et la disponibilité dans un même répertoire. fileciteturn38file2L1-L24

Utilisez cette quick start lorsque vous avez déjà claire la transition depuis Scheduling à Rostering et que vous avez besoin de préparer l'équipe réelle de personnes qui participera à l'affectation.

Avant de commencer, assurez-vous que :
1. Vous avez déjà fermé la transition depuis Scheduling en P19.
2. Vous avez claire l'équipe de conducteurs qui participera au calcul.
3. Vous savez si vous allez inscrire quelques conducteurs manuellement ou si vous avez besoin d'une charge massive.
4. Vous avez accès à l'environnement avec les permissions pour gérer le personnel.

Pour cette quick start, utilisez ce cas de référence :

> **Je vais charger et vérifier la plantilla de conducteurs qui pourra couvrir la solution de L1 avant d'entrer en adscription, règles et disponibilité.**

Pour créer ou importer la plantilla de conducteurs :
1. Dans GoalBus, allez au module de **Configuration** > **Personnel** > **Gestion de conducteurs**.
ref: P20_Imagen1.png | compact
2. Vérifiez si les conducteurs du cas existent déjà dans la liste générale.
3. Si vous avez besoin de créer quelques conducteurs, cliquez sur **Conducteur Nouveau**.
ref: P20_Imagen2.png | compact(2x)
4. Si vous avez besoin de charger beaucoup de conducteurs, réalisez une importation massive par fichier CSV depuis **Carga Personal**.
ref: P20_Imagen3.png | compact
5. Si vous choisissez l'importation massive, préparez le fichier avec les données minimales que votre opération nécessite pour identifier correctement chaque personne. La fenêtre d'importation agira comme une aide pour préparer le CSV de charge.
ref: P20_Imagen4.png
6. Exécutez la charge et vérifiez le résultat.
7. Revenez à la liste générale et vérifiez que les conducteurs apparaissent correctement.
8. Si vous détectez des doublons ou des enregistrements incomplets, les corrigez avant de poursuivre.

Pour le cas de référence, termine cette section uniquement lorsque tu peux affirmer :
1. Les conducteurs de L1 sont déjà enregistrés ou importés.
2. La liste générale reflète une seule maquette de référence.
3. Tu peux déjà ouvrir le profil de chaque conducteur pour examiner son contexte opérationnel.

Lorsque tu as terminé cette section, tu devrais avoir une maquette de conducteurs chargée et visible dans le système. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Examinant le profil du conducteur et ses données structurales

Une fois créée la maquette, il faut examiner le **profil du conducteur**. Le profil n'est pas seulement une fiche de contact : c'est le dossier numérique complet de l'employé au sein de l'opération. Là, coexistent des données statiques, un contexte opérationnel et des attributs qui seront utilisés par le système plus tard pour raisonner sur sa qualification. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Avant de commencer cette section, assure-toi que :
1. Les conducteurs sont déjà visibles dans la liste générale.
2. Tu connais déjà le conducteur ou le groupe que tu vas utiliser comme exemple.
3. Tu veux valider que le registre n'est pas seulement administratif, mais opérationnel.

Pour examiner le profil du conducteur :
1. Dans la liste générale, clique sur le nom d'un conducteur.
ref: P20_Imagen5.png | full
2. Examine la barre latérale de données statiques.
3. Vérifie au moins ces groupes d'informations :
   1. les données de base, comme le nom et le code,
   2. les données opérationnelles, comme le contrat collectif ou le type de contrat,
   3. les liens opérationnels, comme le dépôt principal, le groupe de travail, l'aire ou les types de véhicules autorisés.
4. Si un élément structurale clé manque, complète-le avant de continuer.
5. Enregistre tout changement nécessaire.
6. Répète l'examen sur plusieurs conducteurs pour confirmer la cohérence dans la maquette.

Pour le cas de référence, vérifie au moins :
1. Le code du conducteur.
2. Son dépôt principal.
3. Son groupe de travail.
4. Les propriétés opérationnelles qui conditionneront son affectation ultérieure.

Lorsque vous avez terminé cette section, vous devriez avoir une idée claire que chaque conducteur dispose d'un dossier opérationnel cohérent et utilisable. fileciteturn38file0L8-L20

## Revisant le contexte opérationnel et les données dynamiques du conducteur

En plus des données structurales, le profil du conducteur inclut des données dynamiques qui affectent directement à la façon dont le système raisonne sur la personne. Dans la page de gestion, vous pouvez vérifier les compteurs et les modèles de travail, qui font partie du contexte opérationnel utilisé plus tard par la logique d'affectation. fileciteturn38file0L12-L17

Avant de commencer cette section, assurez-vous que :
1. Vous avez déjà vérifié les données statiques du profil.
2. Vous savez si votre opération utilise des compteurs ou des modèles cycliques.
3. Vous voulez vérifier que le conducteur n'existe pas seulement, mais dispose d'un contexte opérationnel interprétable.

Pour vérifier le contexte opérationnel dynamique :
1. Dans le profil du conducteur, ouvrez la page de **Détails de gestion**.
2. Vérifiez les **compteurs** ou les KPI associés au conducteur si ils existent.
3. Vérifiez si le conducteur est lié à un **modèle de travail**.
4. Si votre opération utilise des modèles cycliques, vérifiez également le déphasage ou la position actuelle du conducteur dans le modèle.
5. Confirmez que ces données ont du sens pour le contexte réel.
6. Si les informations dynamiques ne sont pas correctes, ajustez-les avant de passer aux règles ou au calcul.

Pour le cas de référence, posez-vous les questions suivantes :
1. Ce conducteur a-t-il le profil qui devrait avoir ?
2. Ses compteurs ou KPI sont-ils disponibles si le processus les nécessite ?
3. Le système pourrait-il raisonner correctement sur cette personne dans un calcul de répartition ?

Lorsque vous avez terminé cette section, vous devriez avoir validé non seulement l'identité du conducteur, mais aussi son contexte opérationnel dynamique. fileciteturn38file0L12-L17

## Vérification des habilitations avant d'utiliser le conducteur en Rostering

Avant de considérer un conducteur comme éligible, vous devez vérifier ses **habilitations**. Ces habilitations répondent à la question “Pouvez-vous cette personne travailler légalement ou techniquement dans ce dépôt, groupe ou unité ?”. Elles sont gérées dans une ligne temporelle avec date de début et de fin, et le système affiche des états tels que actif, futur, caduc ou proche de la caducité pour faciliter la lecture. Si une personne n'est pas habilitée pour le contexte requis, le moteur génère une erreur lors de l'essai de l'assigner. fileciteturn38file0L17-L34

Avant de commencer cette section, assurez-vous que :
1. Vous avez déjà vérifié le profil du conducteur.
2. Vous savez déjà quel dépôt, groupe ou unité sera nécessaire pour votre cas.
3. Vous comprenez que l'habilité n'est pas la même chose qu'une cession ou une adscription temporaire.

Pour vérifier et valider les habilitations :
1. Dans le profil du conducteur, ouvrez la section **Habilitations / Cualificaciones**.
2. Vérifiez si des enregistrements sont actuels pour :
   1. dépôts,
   2. groupes de travail,
   3. unités de business.
3. Vérifiez l'état visuel de chaque habilitation :
   1. active,
   2. future,
   3. proche de la caducité,
   4. caduquée.
4. Si une habilitation manque, ajoutez-la avec les dates correctes.
5. Si une habilitation a déjà expiré et ne devrait pas être utilisée, laissez-la comme historique sans essayer de réécrire le passé.
6. Enregistrez les modifications.
7. Confirmez que le conducteur est désormais habilité pour le contexte où vous l'attendez.

Pour le cas de référence, ne continuez pas jusqu'à pouvoir affirmer :
1. Le conducteur est habilité pour le dépôt correct.
2. Le groupe de travail requis est couvert.
3. Il n'y a pas de caducités qui rompent l'éligibilité actuelle.

Lorsque vous avez terminé cette section, vous devriez avoir des conducteurs qui ne sont pas seulement présents dans la grille, mais qui sont également éligibles du point de vue opérationnel et normatif. fileciteturn38file0L17-L34

## Confirmando que la grille est déjà prête pour la prochaine couche de Rostering

L'étape finale est de vérifier que la base de conducteurs est déjà prête pour entrer dans la prochaine couche : adscription opérationnelle, règles, absences et calcul. Ici, l'objectif n'est pas seulement de charger des noms, mais une grille cohérente, tracable et utilisable par le moteur.

Avant de terminer, assurez-vous de :
1. Avoir déjà chargé ou importé la grille.
2. Avoir déjà révisé les profils principaux.
3. Avoir déjà vérifié les données structurelles et dynamiques.
4. Avoir validé les habilitations essentielles.

Pour confirmer que la grille est déjà prête :
1. Revenez à la liste générale des conducteurs.
2. Vérifiez que le collectif nécessaire pour votre cas est présent.
3. Vérifiez que les profils critiques n'ont pas d'informations importantes manquantes.
4. Assurez-vous que les personnes que vous attendez utiliser sont habilitées pour le contexte correct.
5. Demandez-vous si le système pourrait déjà utiliser cette base comme point de départ pour :
   1. adscription opérationnelle,
   2. règles de Rostering,
   3. et disponibilité réelle.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, corrigez la base de conducteurs avant de poursuivre.

Pour le cas de référence, terminez cette quick start uniquement lorsque vous pourrez affirmer :
1. La matrice des conducteurs de L1 est déjà chargée.
2. Les profils clés ont déjà été revus.
3. Les habilitations essentielles sont déjà en vigueur.
4. La base est déjà prête pour passer à l'adscription opérationnelle.

Lorsque vous avez terminé cette section, vous devriez avoir une matrice des conducteurs suffisamment solide pour continuer avec la prochaine couche de Rostering.

## Lectures additionnelles

- [Gestionant l'adscription opérationnelle du conducteur](P21_Gestionant_l'adscription_opérationnelle_du_conducteur.md)