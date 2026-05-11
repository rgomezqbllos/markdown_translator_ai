---
title: Cargando und Verwaltung von Fahrern
shortTitle: Fahrer
intro: Lerne, wie du Fahrer in GoalBus erstellst, importierst und pflegst, seinen operativen Profil bereitstellst und eine zuverlässige Vorlage hinterlässt, bevor du dich auf Adscription, Regeln und Roster-Fluss beziehst.
contentType: how-tos
versions:
  - '*'
---

## Erstellen oder Importieren der Fahrer-Vorlage

Bevor du dich mit den Regeln für Rostering, Abwesenheiten oder der Einsatz von Teams beschäftigst, musst du eine zuverlässige Basis von Fahrern haben. In GoalBus dient die Verwaltung der Fahrer als die Hauptquelle der Wahrheit für die menschliche Betriebskraft: Sie ermöglicht die Kombination von manueller Erstellung und Masseneingabe und konzentriert Identität, Zuordnung zum Depot und Verfügbarkeit in einem einzigen Verzeichnis. fileciteturn38file2L1-L24

Verwende diese Quick Start, wenn du die Übergang von Scheduling nach Rostering klar hast und du den tatsächlichen Team der Personen vorbereiten musst, die am Einsatz beteiligt sein werden.

Bevor du beginnst, stelle sicher, dass:
1. Du die Übergang von Scheduling in P19 bereits abgeschlossen hast.
2. Du weißt, welches Team von Fahrern am Berechnungsprozess beteiligt sein wird.
3. Du weißt, ob du einige Fahrer manuell eintragen oder eine Masseneingabe durchführen musst.
4. Du Zugriff auf das Umfeld mit den Berechtigungen zur Personalverwaltung hast.

Für diese Quick Start verwende diesen Referenzfall:

> **Ich werde die Fahrer-Vorlage laden und überprüfen, die die Lösung für L1 bedienen kann, bevor sie in den Einsatz eingesetzt wird, einschließlich Regeln und Verfügbarkeit.**

Um die Fahrer-Vorlage zu erstellen oder zu importieren:
1. In GoalBus gehe zu dem Modul **Konfiguration** > **Personal** > **Fahrerverwaltung**.
ref: P20_Imagen1.png | compact
2. Überprüfe, ob die Fahrer des Falles bereits in der allgemeinen Liste vorhanden sind.
3. Wenn du einige Fahrer erstellen musst, klicke auf **Neuer Fahrer**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn du viele Fahrer eintragen musst, führe eine Masseneingabe über ein CSV-Datei-Upload von **Personenimport** durch.
ref: P20_Imagen3.png | compact
5. Wenn du eine Masseneingabe durchführst, bereite die Datei vor, die die minimale Anzahl an Daten enthält, die deine Betriebskraft für die korrekte Identifizierung jeder Person benötigt. Die Importfenster wird dir dabei helfen, die CSV-Datei für den Import vorzubereiten.
ref: P20_Imagen4.png
6. Führe die Eingabe durch und überprüfe das Ergebnis.
7. Gehe zur allgemeinen Liste zurück und überprüfe, ob die Fahrer korrekt angezeigt werden.
8. Wenn du Duplikate oder unvollständige Einträge feststellst, korrigiere sie vor dem Fortfahren.

Für den Fall der Referenz beendest du diese Abschnitt nur, wenn du folgende Punkte bestätigen kannst:
1. Die Fahrer von L1 sind bereits registriert oder importiert.
2. Die allgemeine Liste spiegelt eine einzelne Referenzvorlage wider.
3. Du kannst bereits den Profilansicht jedes Fahrers öffnen, um dessen Betriebskontext zu überprüfen.

Wenn du diese Abschnitt beendet hast, solltest du eine Fahrer-Vorlage geladen und sichtbar im System haben. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Überprüfen des Fahrerprofils und seiner strukturierten Daten

Nach Erstellung der Vorlage musst du das **Fahrerprofil** überprüfen. Das Profil ist nicht nur eine Kontaktdatenkarte: Es ist das digitale Akteur des Arbeitnehmers innerhalb der Betriebsoperation. Hier koexistieren statische Daten, Betriebskontext und Attribute, die das System später für die Berechnung seiner Qualifikation verwendet. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Bevor du diese Abschnitt beginnst, stelle sicher, dass:
1. Du bereits Fahrer in der allgemeinen Liste siehst.
2. Du weißt, welchen Fahrer oder welches Fahrer-Team du als Beispiel verwenden wirst.
3. Du überprüfen möchtest, ob das Protokoll nicht nur administrativ, sondern auch betriebswirtschaftlich ist.

Um das Fahrerprofil zu überprüfen:
1. In der allgemeinen Liste klicke auf den Namen eines Fahrers.
ref: P20_Imagen5.png | full
2. Überprüfe die Seitenleiste mit den statischen Daten.
3. Prüfe mindestens diese Datengruppen:
   1. grundlegende Daten, wie Name und Code,
   2. betriebswirtschaftliche Daten, wie Gewerkschaftsvertrag oder Art des Vertrags,
   3. betriebswirtschaftliche Verbindungen, wie Depot, Arbeitsgruppe, Bereich oder zugelassene Fahrzeughäuser.
4. Füll alle wichtigen strukturellen Daten aus, bevor du fortfährst.
5. Speichere alle notwendigen Änderungen.
6. Führe die Überprüfung bei mehreren Fahrern durch, um die Konsistenz der Vorlage zu bestätigen.

Para den referencefall, überprüfe zumindest:
1. Das Fahrer-Kennzeichen.
2. Sein Hauptdepot.
3. Seinen Arbeitsbereich.
4. Die operativen Eigenschaften, die seine zukünftige Zuordnung beeinflussen.

Wenn du diese Abschnitt beendet hast, solltest du verstehen, dass jedes Fahrer eine coherente und nutzbare Fahrerakte besitzt. fileciteturn38file0L8-L20

## Überprüfen des operativen Kontexts und der dynamischen Daten des Fahrers

Außer den strukturellen Daten umfasst das Fahrerprofil auch dynamische Daten, die direkt auf die Art und Weise beeinflussen, wie das System über die Person nachdenkt. In der Verwaltungstabelle kannst du Zähler und Arbeitsmuster überprüfen, die später von der Zuordnungslogik im Kontextoperativ verwendet werden. fileciteturn38file0L12-L17

Bevor du diese Abschnitt beginnst, stelle sicher, dass:
1. Du die statischen Daten des Profils bereits überprüft hast.
2. Du weißt, ob deine Operation Zähler oder zyklische Muster verwendet.
3. Du überprüfst, ob der Fahrer nicht nur existiert, sondern auch einen interpretierbaren operativen Kontext hat.

Um den dynamischen operativen Kontext zu überprüfen:
1. In dem Fahrerprofil öffnest du die Registerkarte **Verwaltungsdetails**.
2. Überprüfe die KPIs oder Key Performance Indicators (KPIs), die dem Fahrer zugeordnet sind, wenn sie vorhanden sind.
3. Überprüfe, ob der Fahrer an einem Arbeitsmuster gebunden ist.
4. Wenn deine Operation zyklische Muster verwendet, überprüfe auch den Versatz oder die aktuelle Position des Fahrers innerhalb des Musters.
5. Stelle sicher, dass diese Daten für den realen Kontext Sinn machen.
6. Wenn die dynamischen Daten nicht korrekt sind, passe sie vor der Überprüfung von Regeln oder Berechnungen an.

Para den referencefall, frage dich:
1. Hat dieser Fahrer das Muster, das er haben sollte?
2. Sind seine Zähler oder KPIs verfügbar, wenn der Prozess sie benötigt?
3. Könnte das System korrekt über diese Person in einem Reibungsberechnung rechnen?

Wenn du diese Abschnitt beendet hast, solltest du nicht nur die Identität des Fahrers, sondern auch seinen dynamischen Betriebskontext validiert haben. fileciteturn38file0L12-L17

## Validieren der Berechtigungen vor der Nutzung des Fahrers in der Rostering

Bevor du einen Fahrer als qualifiziert betrachtest, musst du seine **Berechtigungen** überprüfen. Diese Berechtigungen beantworten die Frage: „Kann diese Person legal oder technisch in diesem Depot, Gruppe oder Geschäftseinheit arbeiten?“. Sie werden in einer zeitlichen Linie mit Start- und Enddatum verwaltet, und das System zeigt Zustände wie aktiv, zukünftig, abgelaufen oder nahezu abgelaufen an, um die Lesbarkeit zu erleichtern. Wenn eine Person für den erforderlichen Kontext nicht berechtigt ist, generiert das System einen Fehler, wenn sie versucht wird zuzuordnen. fileciteturn38file0L17-L34

Bevor du diese Abschnitt beginnst, stelle sicher, dass:
1. Du den Fahrerprofil bereits überprüft hast.
2. Du weißt, welches Depot, Gruppe oder Geschäftseinheit für deinen Fall erforderlich ist.
3. Du verstehst, dass eine Berechtigung nicht dasselbe ist wie eine Übertragung oder eine temporäre Zuordnung.

Um die Berechtigungen zu überprüfen und zu validieren:
1. In dem Fahrerprofil öffnest du die Registerkarte **Berechtigungen / Qualifikationen**.
2. Überprüfe, ob es aktuelle Einträge gibt für:
   1. Depots,
   2. Arbeitsgruppen,
   3. Geschäftsunit.
3. Prüfe den visuellen Zustand jeder Berechtigung:
   1. aktiv,
   2. zukünftig,
   3. nahezu abgelaufen,
   4. abgelaufen.
4. Wenn eine erforderliche Berechtigung fehlt, füge sie mit den richtigen Datumsangaben hinzu.
5. Wenn eine Berechtigung abgelaufen ist und sie nicht mehr verwendet werden sollte, lass sie als historisch und versuche nicht, den vergangenen Zustand zu ändern.
6. Speichere die Änderungen.
7. Bestätige, dass der Fahrer für den Kontext berechtigt ist, in dem du ihn verwenden möchtest.

Para den referencefall, fortsetze nicht, bis du bejahen kannst:
1. Der Fahrer ist für den richtigen Depot berechtigt.
2. Der erforderliche Arbeitsbereich ist abgedeckt.
3. Es gibt keine Ablaufdaten, die die aktuelle Berechtigung unterbrechen.

Wenn du diese Abschnitt beendet hast, solltest du Fahrer haben, die nicht nur in der Vorlage existieren, sondern auch operativ und rechtlich berechtigt sind. fileciteturn38file0L17-L34

## Bestätigen, dass die Vorlage für die nächste Ebene des Rostering bereit ist

Der letzte Schritt ist die Überprüfung, ob die Fahrerbasis für die nächste Ebene bereit ist: operative Zuordnung, Regeln, Abwesenheiten und Berechnung. Hier geht es nicht nur darum, Namen einzuladen, sondern um eine kohärente, nachvollziehbare und nutzbare Vorlage.

Bevor du fertig bist, stelle sicher, dass:
1. Du bereits die Vorlage geladen oder importiert hast.
2. Du bereits die Hauptprofile überprüft hast.
3. Du bereits die strukturellen und dynamischen Daten überprüft hast.
4. Du bereits die wesentlichen Berechtigungen überprüft hast.

Um zu bestätigen, dass die Vorlage bereit ist:
1. Gehe zur allgemeinen Fahrerliste.
2. Überprüfe, ob der notwendige Kollektiv für deinen Fall vorhanden ist.
3. Prüfe, ob kritische Profile wichtige Informationen fehlen lassen.
4. Stelle sicher, dass die Personen, die du verwenden möchtest, für den richtigen Kontext berechtigt sind.
5. Frage dich, ob das System diese Basis bereits als Ausgangspunkt für:
   1. operative Zuordnung,
   2. Rostering-Regeln,
   3. und die tatsächliche Verfügbarkeit verwenden könnte.
6. Wenn die Antwort ja ist, fahre mit dem nächsten Quick Start fort.
7. Wenn die Antwort nein ist, korrigiere die Fahrerbasis vor dem Fortfahren.

Para den referencefall, beende diese Quick Start nur, wenn du folgende Punkte bestätigen kannst:
1. Die L1-Fahrer-Vorlage ist bereits geladen.
2. Die Schlüsselprofile wurden bereits überprüft.
3. Die wesentlichen Berechtigungen sind bereits gültig.
4. Die Basis ist bereit für die Übergabe zur operativen Adscription.

Wenn du diese Abschnitt beendet hast, solltest du eine Fahrer-Vorlage haben, die ausreichend stabil ist, um zur nächsten Rostering-Ebene fortzufahren.

## Zusätzliche Lektüre

- [Gestionando la adscripción operativa del conductor](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)