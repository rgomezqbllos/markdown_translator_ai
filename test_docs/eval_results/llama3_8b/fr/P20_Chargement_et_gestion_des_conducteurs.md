---
title: Chargement et gestion des conducteurs
shortTitle: Conducteurs
intro: 'Apprends à créer, importer et maintenir la base des conducteurs dans GoalBus, consulter leur profil opérationnel et laisser un modèle fiable avant de passer à l'adéquation, les règles et le calcul de Rostering.'
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
3. Si vous avez besoin de créer quelques conducteurs, cliquez sur **Nouveau Conductor**.
ref: P20_Imagen2.png | compact(2x)
4. Si vous avez besoin de charger beaucoup de conducteurs, réalisez une importation massive par fichier CSV depuis **Carga Personal**.
ref: P20_Imagen3.png | compact
5. Si vous choisissez l'importation massive, préparez le fichier avec les données minimales que votre opération nécessite pour identifier correctement chaque personne. La fenêtre d'importation agira comme une aide pour préparer le CSV de charge.
ref: P20_Imagen4.png
6. Exécutez la charge et vérifiez le résultat.
7. Retournez à la liste générale et vérifiez que les conducteurs apparaissent correctement.
8. Si vous détectez des doublons ou des enregistrements incomplets, les corrigez avant de poursuivre.

## Vérification du profil du conducteur et de ses données structurelles

Une fois la plantilla créée, il faut vérifier le **profil du conducteur**. Le profil n'est pas seulement une fiche de contact : c'est le dossier numérique complet de l'employé au sein de l'opération. Là, coexistent des données statiques, un contexte opérationnel et des attributs que le système utilisera plus tard pour raisonner sur sa qualification. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Avant de commencer cette section, assure-toi que :
1. Les conducteurs sont déjà visibles dans la liste générale.
2. Tu connais déjà le conducteur ou le groupe que tu vas utiliser comme exemple.
3. Tu veux valider que le registre n'est pas seulement administratif, mais opérationnel.

Pour vérifier le profil du conducteur :
1. Dans la liste générale, clique sur le nom d'un conducteur.
ref: P20_Imagen5.png | full
2. Vérifie la barre latérale de données statiques.
3. Vérifie au moins ces groupes d'informations :
   1. les données de base, comme le nom et le code,
   2. les données opérationnelles, comme le contrat collectif ou le type de contrat,
   3. les liens opérationnels, comme le dépôt principal, le groupe de travail, l'aire ou les types de véhicules autorisés.
4. Si un élément structurel clé manque, complète-le avant de continuer.
5. Enregistre tout changement nécessaire.
6. Répète la vérification sur plusieurs conducteurs pour confirmer la cohérence dans la plantilla.

## Vérification du contexte opérationnel et des données dynamiques du conducteur

Avant de passer à la section suivante, assure-toi que :

1. Tu as déjà vérifié les données statiques du profil.
2. Tu sais si ton opération utilise des comptes ou des modèles cycliques.
3. Tu veux vérifier que le conducteur n'est pas seulement existant, mais qu'il a un contexte opérationnel interprétable.

Pour vérifier le contexte opérationnel dynamique :

1. Dans le profil du conducteur, ouvre la section **Détails d'administration**.
2. Vérifie les **comptes** ou les KPI associés au conducteur si ils existent.
3. Vérifie si le conducteur est lié à un **modèle de travail**.
4. Si ton opération utilise des modèles cycliques, vérifie également le décalage ou la position actuelle du conducteur dans le modèle.
5. Confirme que ces données ont du sens pour le contexte réel.
6. Si les informations dynamiques ne sont pas correctes, ajuste-les avant de passer aux règles ou au calcul.

## Vérification du contexte opérationnel et des données dynamiques du conducteur

Pour le cas de référence, vérifie au moins :

1. Le code du conducteur.
2. Son dépôt principal.
3. Son groupe de travail.
4. Les propriétés opérationnelles qui conditionneront son affectation ultérieure.

Lorsque tu as terminé cette section, tu devrais avoir une idée claire de ce que chaque conducteur a un dossier opérationnel cohérent et utilisable.

## Vérification du contexte opérationnel et des données dynamiques du conducteur

En plus des données structurales, le profil du conducteur inclut des données dynamiques qui affectent directement la façon dont le système raisonne sur la personne. Dans la section d'administration, tu peux vérifier les comptes et les modèles de travail, qui font partie du contexte opérationnel utilisé plus tard par la logique d'affectation.

Antes de empezar esta sección, asegúrate de que :
1. Ya revisaste los datos estáticos del perfil.
2. Ya sabes si tu operación usa contadores o patrones cíclicos.
3. Quieres comprobar que el conductor no solo existe, sino que tiene un contexto operativo interpretable.

Para revisar el contexto operativo dinámico :
1. Dentro del perfil del conductor, abre la pestaña de **Detalles de administración**.
2. Revisa los **comptes** o KPI asociados al conductor si existen.
3. Comprueba si el conductor está vinculado a algún **patrón de trabajo**.
4. Si tu operación usa patrones cíclicos, revisa también el desfase o posición actual del conductor dentro del patrón.
5. Confirma que estos datos tienen sentido para el contexto real.
6. Si la información dinámica no es correcta, ajústala antes de pasar a reglas o cálculo.

## Validation des habilitations avant d'utiliser le conducteur dans Rostering

Avant de considérer un conducteur comme éligible, il faut vérifier ses **habilitations**. Ces habilitations répondent à la question “Peut-on cette personne travailler légalement ou techniquement dans ce dépôt, groupe ou unité ?”. Elles sont gérées dans une ligne temporelle avec date de début et de fin, et le système affiche des états tels que actif, futur, caducé ou proche de la caducité pour faciliter la lecture. Si une personne n'est pas habilitée pour le contexte requis, le moteur génère une erreur lorsqu'il essaie de l'assigner. fileciteturn38file0L17-L34

Avant de commencer cette section, assure-toi que :
1. Tu as déjà révisé le profil du conducteur.
2. Tu sais déjà quel dépôt, groupe ou unité sera nécessaire pour ton cas.
3. Tu comprends que les habilitations ne sont pas la même chose que les cessions ou les adhésions temporaires.

Pour réviser et valider les habilitations :
1. Dans le profil du conducteur, ouvre la section **Habilitations / Cualificaciones**.
2. Vérifie si il existe des enregistrements actuels pour :
   1. les dépôts,
   2. les groupes de travail,
   3. les unités de commerce.
3. Vérifie l'état visuel de chaque habilitation :
   1. active,
   2. future,
   3. proche de la caducité,
   4. caduquée.
4. Si une habilitation manque, ajoute-la avec les dates correctes.
5. Si une habilitation a déjà expiré et ne devrait pas être utilisée, laisse-la comme historique sans essayer de réécrire le passé.
6. Enregistre les modifications.
7. Confirme que le conducteur est maintenant habilité pour le contexte où tu l'utilises.

## Confirmando que la plantilla ya est est list pour la prochaine couche de Rostering

Le dernier pas est de vérifier que la base de conducteurs est déjà prête pour entrer dans la prochaine couche : adscription opérationnelle, règles, absences et calcul. Ici, l'objectif n'est pas seulement de charger des noms, mais une plantilla cohérente, tracable et utilisable par le moteur.

Avant de terminer, assure-toi de que :
1. Tu as déjà chargé ou importé la plantilla.
2. Tu as déjà révisé les profils principaux.
3. Tu as déjà vérifié les données structurales et dynamiques.
4. Tu as déjà validé les habilitations essentielles.

Pour confirmer que la plantilla est déjà prête :
1. Reviens à la liste générale des conducteurs.
2. Vérifie que le collectif nécessaire pour ton cas est présent.
3. Vérifie que les profils critiques n'ont pas de trous d'informations importantes.
4. Assure-toi que les personnes que tu attends utiliser sont habilitées pour le contexte correct.
5. Pense-toi si le système pourrait déjà utiliser cette base comme point de départ pour :
   1. adscription opérationnelle,
   2. règles de Rostering,
   3. et disponibilité réelle.
6. Si la réponse est oui, continue avec le prochain quick start.
7. Si la réponse est non, corrige la base de conducteurs avant de continuer.

## Confirmando que la plantilla ya está lista pour la siguiente capa de Rostering

Le dernier pas est de vérifier que la base de conducteurs est déjà prête pour entrer dans la prochaine couche : adscription opérationnelle, règles, absences et calcul. Ici, l'objectif n'est pas seulement de charger des noms, mais une plantilla cohérente, tracable et utilisable par le moteur.

Avant de terminer, assure-toi de que :
1. Tu as déjà chargé ou importé la plantilla.
2. Tu as déjà révisé les profils principaux.
3. Tu as déjà vérifié les données structurales et dynamiques.
4. Tu as déjà validé les habilitations essentielles.

Pour confirmer que la plantilla est déjà prête :
1. Reviens à la liste générale des conducteurs.
2. Vérifie que le collectif nécessaire pour ton cas est présent.
3. Vérifie que les profils critiques n'ont pas de trous d'informations importantes.
4. Assure-toi que les personnes que tu attends utiliser sont habilitées pour le contexte correct.
5. Pense-toi si le système pourrait déjà utiliser cette base comme point de départ pour :
   1. adscription opérationnelle,
   2. règles de Rostering,
   3. et disponibilité réelle.
6. Si la réponse est oui, continue avec le prochain quick start.
7. Si la réponse est non, corrige la base de conducteurs avant de continuer.

Pour le cas de référence, terminez cette quick start uniquement lorsque vous pourrez affirmer :
1. La plantilla de conducteurs de L1 est déjà chargée.
2. Les profils clés ont déjà été révisés.
3. Les habilitations essentielles sont déjà en vigueur.
4. La base est déjà prête pour passer à l'adscription opérationnelle.

Lorsque vous avez terminé cette section, vous devriez avoir une plantilla de conducteurs suffisamment solide pour poursuivre avec la prochaine couche de Rostering.

## Lectures additionnelles

- [Gestionando la adscripción operativa del conductor](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)