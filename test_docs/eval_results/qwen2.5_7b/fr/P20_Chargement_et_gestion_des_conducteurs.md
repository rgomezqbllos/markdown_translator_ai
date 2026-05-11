---
title: Chargement et gestion des conducteurs
shortTitle: Conducteurs
intro: 'Apprenez à créer, importer et maintenir la base de conducteurs dans GoalBus, examiner leur profil opérationnel et laisser une feuille de relève fiable avant de passer à l'adéquation, règles et calcul de roulement.'
contentType: how-tos
versions:
  - '*'
---

## Créer ou importer le modèle de conducteurs

Avant de parler des règles de Roulement, absences ou affectation de postes, vous avez besoin d'une base fiable de conducteurs. Dans GoalBus, la gestion des conducteurs agit comme la source principale de vérité pour la gestion humaine : elle permet de combiner la création manuelle et la charge massive, et regroupe l'identité, l'affiliation au dépôt et la disponibilité dans un même répertoire. fileciteturn38file2L1-L24

Utilisez cette quick start lorsque vous avez clairement la transition de Scheduling à Roulement et que vous préparez le collectif réel de personnes qui participera à l'affectation.

Avant de commencer, assurez-vous que :
1. Vous avez déjà fermé la transition de Scheduling en P19.
2. Vous savez quel collectif de conducteurs participera au calcul.
3. Vous savez si vous allez inscrire quelques conducteurs manuellement ou si vous avez besoin d'une charge massive.
4. Vous avez accès à l'environnement avec les droits nécessaires pour gérer le personnel.

Pour cette quick start, utilisez ce cas de référence :

> **Je vais charger et vérifier le modèle de conducteurs qui pourra couvrir la solution de L1 avant l'admission, les règles et la disponibilité.**

Pour créer ou importer le modèle de conducteurs :
1. Dans GoalBus, accédez au module de **Configuration** > **Personnel** > **Gestion des conducteurs**.
ref: P20_Imagen1.png | compact
2. Vérifiez si les conducteurs du cas existent déjà dans la liste générale.
3. Si vous devez créer quelques conducteurs, cliquez sur **Nouveau Conducteur**.
ref: P20_Imagen2.png | compact(2x)
4. Si vous devez charger de nombreux conducteurs, effectuez une importation massive via un fichier CSV depuis **Charge de personnel**.
ref: P20_Imagen3.png | compact
5. Si vous choisissez l'importation massive, préparez le fichier avec les données minimales nécessaires pour identifier correctement chaque personne. La fenêtre d'importation agira en aide pour préparer le CSV de charge.
ref: P20_Imagen4.png
6. Exécutez la charge et vérifiez le résultat.
7. Revenez à la liste générale et vérifiez que les conducteurs apparaissent correctement.
8. Si vous détectez des doublons ou des enregistrements incomplets, corrigez-les avant de continuer.

Pour le cas de référence, termine cette section seulement lorsque tu pourras affirmer :
1. Les conducteurs de L1 sont déjà enregistrés ou importés.
2. La liste générale reflète une seule feuille de référence.
3. Tu peux déjà ouvrir le profil de chaque conducteur pour vérifier son contexte opérationnel.

Lorsque tu termines cette section, tu devrais avoir une feuille de référence des conducteurs chargée et visible dans le système. fileciteturn38file0L1-7 fileciteturn38file2L1-24

## Vérification du profil du conducteur et de ses données structurales

Une fois la feuille de référence créée, tu dois vérifier le **profil du conducteur**. Le profil n'est pas seulement une fiche de contact : c'est le dossier numérique complet de l'employé au sein de l'opération. Il regroupe des données statiques, un contexte opérationnel et des attributs que le système utilisera plus tard pour raisonner sur sa faisabilité. fileciteturn38file0L8-20 fileciteturn38file2L25-40

Avant de commencer cette section, assure-toi de :
1. Avoir déjà des conducteurs visibles dans la liste générale.
2. Savoir quel conducteur ou quel groupe tu vas utiliser comme exemple.
3. Vérifier que le registre n'est pas seulement administratif, mais opérationnel.

Pour vérifier le profil du conducteur :
1. Dans la liste générale, clique sur le nom d'un conducteur.
ref: P20_Imagen5.png | full
2. Vérifie la barre latérale de données statiques.
3. Vérifie au moins ces groupes d'informations :
   1. des données de base, comme le nom et le code,
   2. des données opérationnelles, comme le conventionnement ou le type de contrat,
   3. des liens opérationnels, comme le dépôt principal, le groupe de travail, l'aire ou les types de véhicules autorisés.
4. Si un élément structuré clé est manquant, complétalo avant de continuer.
5. Enregistre tout changement nécessaire.
6. Répète la vérification pour plusieurs conducteurs pour confirmer la cohérence de la feuille de référence.

Pour le cas de référence, examinez au moins :
1. Le code du conducteur.
2. Son dépôt principal.
3. Son équipe de travail.
4. Les propriétés opérationnelles qui conditionneront sa réaffectation ultérieure.

Quand vous avez terminé cette section, vous devriez comprendre que chaque conducteur dispose d'un dossier opérationnel cohérent et utilisable. fileciteturn38file0L8-L20

## Revisant le contexte opérationnel et les données dynamiques du conducteur

Outre les données structurales, le profil du conducteur inclut des données dynamiques qui influencent directement la façon dont le système raisonne sur la personne. Dans l'onglet de gestion, vous pouvez examiner les compteurs et les schémas de roulement, qui font partie du contexte opérationnel utilisé ultérieurement par la logique de réaffectation. fileciteturn38file0L12-L17

Avant de commencer cette section, assurez-vous que :
1. Vous avez déjà examiné les données statiques du profil.
2. Vous savez si votre opération utilise des compteurs ou des schémas cycliques.
3. Vous voulez vérifier que le conducteur existe et a un contexte opérationnel interprétable.

Pour examiner le contexte opérationnel dynamique :
1. Dans le profil du conducteur, ouvrez l'onglet **Détails de gestion**.
2. Examinez les **compteurs** ou KPI associés au conducteur, s'ils existent.
3. Vérifiez si le conducteur est lié à un **schéma de roulement**.
4. Si votre opération utilise des schémas cycliques, examinez également l'écart ou la position actuelle du conducteur dans le schéma.
5. Confirmez que ces données ont du sens dans le contexte réel.
6. Si les informations dynamiques ne sont pas correctes, ajustez-les avant de passer aux règles ou au calcul.

Pour le cas de référence, posez-vous ces questions :
1. Ce conducteur a-t-il le patronyme qu'il devrait avoir ?
2. Ses compteurs ou KPI sont-ils disponibles si le processus les nécessite ?
3. Le système pourrait-il raisonner correctement sur cette personne dans un calcul de relève ?

Quand vous terminerez cette section, vous devriez avoir validé non seulement l'identité du conducteur, mais aussi son contexte opérationnel dynamique. fileciteturn38file0L12-L17

## Valider les autorisations avant d'utiliser le conducteur dans le roulement

Avant de considérer un conducteur comme éligible, vous devez vérifier ses **autorisations**. Ces autorisations répondent à la question « peut-elle travailler légalement ou techniquement dans ce dépôt, groupe ou unité ? ». Elles sont gérées sur une ligne temporelle avec une date de début et une date de fin, et le système affiche des états comme actif, futur, caduc ou proche de la caducité pour faciliter la lecture. Si une personne n'est pas autorisée dans le contexte requis, le moteur génère une erreur lorsqu'elle est tentée d'être assignée. fileciteturn38file0L17-L34

Avant de commencer cette section, assurez-vous de :
1. Vous être déjà penché sur le profil du conducteur.
2. Savoir quel dépôt, groupe ou unité sera nécessaire pour votre cas.
3. Comprendre que une autorisation n'est pas la même qu'une cession ou une affectation temporaire.

Pour vérifier et valider les autorisations :
1. Dans le profil du conducteur, ouvrez l'onglet **Autorisations / Qualifications**.
2. Vérifiez s'il existe des enregistrements en cours pour :
   1. les dépôts,
   2. les groupes de travail,
   3. les unités d'entreprise.
3. Examinez l'état visuel de chaque autorisation :
   1. active,
   2. future,
   3. proche de la caducité,
   4. caduquée.
4. Si une autorisation nécessaire est manquante, ajoutez-la avec ses dates correctes.
5. Si une autorisation a déjà caducé et ne devrait pas être utilisée, laissez-la en historique sans tenter de réécrire le passé.
6. Enregistrez les modifications.
7. Confirmez que le conducteur est déjà autorisé pour le contexte où vous prévoyez de l'utiliser.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer :
1. Le conducteur est habilité pour le Depôt correct.
2. Le groupe de travail requis est couvert.
3. Il n'y a pas de caducités qui rompent l'éligibilité actuelle.

Quand vous terminerez cette section, vous devriez avoir des conducteurs qui ne sont pas seulement présents dans la planification, mais qui sont également éligibles du point de vue opérationnel et réglementaire. fileciteturn38file0L17-L34

## Confirmez que la planification est prête pour la prochaine couche de Roulement

Le dernier pas est de vérifier que la base de conducteurs est prête pour entrer dans la prochaine couche : affectation opérationnelle, règles, absences et calcul. L'objectif ici n'est pas seulement d'avoir des noms chargés, mais d'avoir une planification cohérente, tracable et utilisable par le système.

Avant de terminer, assurez-vous de ce que :
1. Vous avez déjà chargé ou importé la planification.
2. Vous avez déjà vérifié les profils principaux.
3. Vous avez déjà vérifié les données structurales et dynamiques.
4. Vous avez déjà validé les habilitations essentielles.

Pour confirmer que la planification est prête :
1. Retournez à la liste générale des conducteurs.
2. Vérifiez que le collectif nécessaire à votre cas est présent.
3. Vérifiez que les profils critiques n'ont pas de lacunes d'information importantes.
4. Assurez-vous que les personnes que vous prévoyez d'utiliser sont habilitées pour le contexte correct.
5. Posez-vous la question si le système pourrait déjà utiliser cette base comme point de départ pour :
   1. affectation opérationnelle,
   2. règles de Roulement,
   3. et disponibilité réelle.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, corrigez la base de conducteurs avant de continuer.

Pour le cas de référence, termine cette quick start seulement lorsque tu pourras affirmer :
1. La plantilla de conducteurs de L1 est déjà chargée.
2. Les profils clés ont déjà été revus.
3. Les autorisations essentielles sont déjà en vigueur.
4. La base est déjà prête pour passer à l'adcription opérationnelle.

Lorsque tu termines cette section, tu devrais avoir une plantilla de conducteurs suffisamment solide pour pouvoir continuer avec la prochaine couche de roulement.

## Lectures supplémentaires

- [Gestion de l'adcription opérationnelle du conducteur](P21_Gestion_de_l_adscription_opérationnelle_du_conducteur.md)