---
title: Chargement et gestion des conducteurs
shortTitle: Conducteurs
intro: 'Apprenez à créer, importer et à maintenir la base de conducteurs sur GoalBus, à vérifier leur profil opérationnel et à établir une feuille de route fiable avant de passer à l'adscription, aux règles et au calcul de Rostering.'
contentType: tutoriels
versions:
  - '*'
---

## Créer ou importer la feuille de route des conducteurs

Avant de parler des règles de Rostering, de absences ou d'affectation de horaires, vous devez avoir une base fiable de conducteurs. En GoalBus, la gestion des conducteurs agit comme la source principale de vérité pour l'opérabilité humaine : elle permet de combiner création manuelle et chargement massif, et concentre l'identité, l'affiliation au dépôt et la disponibilité dans un même répertoire. fileciteturn38file2L1-L24


Utilisez cette quick start lorsque vous avez déjà une idée claire de la transition de Scheduling à Rostering et que vous devez préparer le collectif réel de personnes qui participeront à l'affectation.

Avant de commencer, assurez-vous que :
1. Vous avez terminé la transition de Scheduling en P19.
2. Vous avez bien compris quel collectif de conducteurs participera au calcul.
3. Vous savez si vous allez créer quelques conducteurs manuellement ou si vous avez besoin d'un chargement massif.
4. Vous avez accès à l'environnement avec les autorisations pour gérer les personnels.

Pour cette quick start, utilisez ce cas d'étude :

> **Je vais charger et vérifier la feuille de route des conducteurs qui pourra couvrir la solution L1 avant d'entrer dans l'adscription, les règles et la disponibilité.**

Pour créer ou importer la feuille de route des conducteurs :
1. Dans GoalBus, allez dans le module de **Configuration** > **Personnel** > **Gestion des conducteurs**.
ref: P20_Imagen1.png | compact
2. Vérifiez si les conducteurs du cas existent déjà dans la liste générale.
3. Si vous devez créer quelques conducteurs, cliquez sur **Nouveau conducteur**.
ref: P20_Imagen2.png | compact(2x)
4. Si vous devez charger de nombreux conducteurs, effectuez une importation massive via un fichier CSV depuis **Charge Personnel**.
ref: P20_Imagen3.png | compact
5. Si vous choisissez l'importation massive, préparez le fichier avec les données minimales que votre opération a besoin pour identifier correctement chaque personne. La fenêtre d'importation agira comme un aide pour préparer le CSV de chargement.
ref: P20_Imagen4.png
6. Exécutez la charge et vérifiez le résultat.
7. Retournez à la liste générale et vérifiez que les conducteurs apparaissent correctement.
8. Si vous détectez des doublons ou des enregistrements incomplets, corrigez-les avant de continuer.

Pour l'instance de référence, terminez cette section uniquement lorsque vous pouvez affirmer :
1. Les conducteurs de L1 sont déjà inscrits ou importés.
2. La liste générale reflète une seule feuille de référence.
3. Vous pouvez désormais ouvrir le profil de chaque conducteur pour vérifier son contexte opérationnel.

Lorsque vous avez terminé cette section, vous devriez avoir une feuille de conducteurs chargée et visible dans le système. fileciteturn38file0L1-L7 Tully fileciteturn38file2L1-L24 Tully

##  Revoir le profil du conducteur et ses données structurelles

Une fois la feuille créée, vous devez vérifier le **profil du conducteur**. Le profil n'est pas simplement une fiche de contact : c'est l'expediteur numérique complet de l'employé au sein de l'opération. Il y a des données statiques, contexte opérationnel et attributs que le système utilisera plus tard pour raisonner sur son éligibilité. fileciteturn38file0L8-L20 Tully fileciteturn38file2L25-L40 Tully

Avant de commencer cette section, assurez-vous que :
1. Vous avez des conducteurs visibles sur la liste générale.
2. Vous savez quel conducteur ou quel groupe allez-vous utiliser comme exemple.
3. Vous souhaitez valider que le registre n'est pas uniquement administratif, mais opérationnel.

Pour vérifier le profil du conducteur :
1. Dans la liste générale, cliquez sur le nom d'un conducteur.
ref: P20_Imagen5.png | full
2. Vérifiez la barre latérale des données statiques.
3. Vérifiez au moins ces groupes d'informations :
   1. Données basiques, comme le nom et le code,
   2. Données opérationnelles, comme le convention collective ou le type de contrat,
   3. Liens opérationnels, comme le dépôt principal, le groupe de travail, l'area ou les types de véhicules autorisés.
4. Si un élément structurel clé est manquant, complétez-le avant de continuer.
5. Enregistrez tous les changements nécessaires.
6. Répétez la vérification sur plusieurs conducteurs pour confirmer la cohérence dans la feuille.

Pour le cas de référence, veuillez vérifier au moins :
1. Le code du conducteur.
2. Son dépôt principal.
3. Son groupe de travail.
4. Les propriétés opérationnelles qui détermineront sa future allocation.

Lorsque vous aurez terminé cette section, vous devriez avoir une idée claire que chaque conducteur dispose d'un expediente opérationnel cohérent et utilisable. fileciteturn38file0L8-L20


##  Revoir le contexte opérationnel et les données dynamiques du conducteur

En plus des données structurelles, le profil du conducteur inclut des données dynamiques qui affectent directement la façon dont le système raisonne sur la personne. Dans la section d'administration, vous pouvez consulter les conducteurs et les modèles de travail, qui font partie du contexte opérationnel utilisé plus tard par la logique d'attribution. fileciteturn38file0L12-L17


Avant de commencer cette section, assurez-vous de bien avoir vérifié :
1. Les données statiques du profil.
2. Si votre opération utilise des conducteurs ou des modèles cycliques.
3. Si vous souhaitez vérifier que le conducteur existe et qu'il a un contexte opérationnel interprétatif.

Pour vérifier le contexte opérationnel dynamique :
1. Dans le profil du conducteur, ouvrez la section **Détails d'administration**.
2. Vérifiez les **conducteurs** ou les indicateurs de performance associés au conducteur si ils existent.
3. Vérifiez si le conducteur est lié à un **modèle de travail**.
4. Si votre opération utilise des modèles cycliques, vérifiez également le décalage ou la position actuelle du conducteur dans le modèle.
5. Confirmez que ces données ont un sens pour le contexte réel.
6. Si les données dynamiques sont incorrectes, ajustez-les avant de passer aux règles ou au calcul.

Pour le cas de référence, posez-vous la question :
1. Ce conducteur a-t-il le schéma qui devrait l'avoir ?
2. Ses compteurs ou KPI sont-ils disponibles si le processus les a besoin ?
3. Le système pourrait-il raisonner correctement sur cette personne dans un calcul d'affectation ?

Lorsque vous avez terminé cette section, vous devez avoir validé non seulement l'identité du conducteur, mais aussi son contexte opérationnel dynamique. 
fileciteturn38file0L12-L17

## Validation des autorisations avant d'utiliser le conducteur dans le Rostering

Avant de considérer un conducteur comme éligible, il faut examiner ses **autorisations**. Ces autorisations répondent à la question « peut-on cette personne travailler légalement ou techniquement dans ce dépôt, groupe ou unité ? ». Elles sont gérées sur une ligne temporelle avec une date de début et de fin, et le système affiche des états comme actif, futur, caduqué ou proche de caducité pour faciliter la lecture. Si une personne n'est pas habilitée pour le contexte requis, le moteur génère une erreur lors de l'attribution. 
fileciteturn38file0L17-L34

Avant de commencer cette section, assurez-vous de :
1. Avoir déjà examiné le profil du conducteur.
2. Avoir déjà identifié le dépôt, le groupe ou l'unité nécessaire pour votre cas.
3. Avoir compris que l'autorisation n'est pas la même chose qu'une cession ou une affiliation temporaire.

Pour vérifier et valider les autorisations :
1. Dans le profil du conducteur, ouvrez la section **Autorisations / Qualifications**.
2. Vérifiez si des enregistrements sont en vigueur pour :
   1. dépôts,
   2. groupes de travail,
   3. unités de business.
3. Vérifiez l'état visuel de chaque autorisation :
   1. active,
   2. future,
   3. proche de caducité,
   4. caduquée.
4. Si une autorisation est manquante, ajoutez-la avec les dates correctes.
5. Si une autorisation a déjà caduqué et ne devrait pas être utilisée, la laissez comme historique sans tenter de la réécrire.
6. Enregistrez les modifications.
7. Confirmez que le conducteur est déjà habilité pour le contexte où vous l'utilisez.

Pour l'instance de référence, ne continuez pas jusqu'à pouvoir affirmer :
1. Le conducteur est habilité pour le dépôt correct.
2. Le groupe de travail requis est couvert.
3. Il n'y a pas de dates qui rompent l'éligibilité actuelle.

Lorsque vous avez terminé cette section, vous devriez avoir des conducteurs qui ne se limitent pas à l'existence dans la feuille de route, mais qui sont également éligibles en termes opérationnels et réglementaires. fileciteturn38file0L17-L34


## Confirmez que la feuille de route est déjà prête pour la prochaine couche de Rostering

Le dernier pas est de vérifier que la base de conducteurs est déjà prête pour entrer dans la prochaine couche : adscription opérationnelle, règles, absences et calcul. L'objectif n'est pas seulement de charger des noms, mais une feuille de route cohérente, traçable et utilisable par le moteur.

Avant de terminer, assurez-vous que :
1. Vous avez chargé ou importé la feuille de route.
2. Vous avez vérifié les profils principaux.
3. Vous avez vérifié les données structurelles et dynamiques.
4. Vous avez validé les habilitations essentielles.

Pour confirmer que la feuille de route est prête :
1. Retournez à la liste générale des conducteurs.
2. Vérifiez que le groupe nécessaire pour votre cas est présent.
3. Vérifiez que les profils critiques n'ont pas de trous d'informations importantes.
4. Assurez-vous que les personnes que vous attendez d'utiliser sont habilitées pour le contexte correct.
5. Posez-vous la question de savoir si le système pourrait déjà utiliser cette base comme point de départ pour :
   1. adscription opérationnelle,
   2. règles de Rostering,
   3. et disponibilité réelle.
6. Si la réponse est oui, continuez avec le quick start suivant.
7. Si la réponse est non, corrigez la base de conducteurs avant de continuer.

Pour l'instance de référence, termine cette quick start seulement lorsque vous pouvez affirmer :
1. La plantilla de conducteurs de L1 est déjà chargée.
2. Les profils clés ont déjà été examinés.
3. Les autorisations essentielles sont déjà en vigueur.
4. La base est déjà prête à passer à l'adscription opérationnelle.

Lorsque vous avez terminé cette section, vous devriez avoir une feuille de route de conducteurs suffisamment solide pour continuer à la couche suivante de planification.

## Lectures supplémentaires

- [Gestion de l'adscription opérationnelle du conducteur](P21_Gestion_de_l_adscription_operationnelle_du_conducteur.md)