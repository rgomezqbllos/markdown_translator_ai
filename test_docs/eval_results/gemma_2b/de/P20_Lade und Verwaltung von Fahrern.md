## Lade und verwalte Fahrer
**Kurztitel:** Fahrer
**Intro:** 'Lernen Sie, wie Sie die Fahrerbasis in GoalBus erstellen, importieren und pflegen, ihre operative Profile überprüfen und eine zuverlässige Vorlage vor der Adscripción, Regeln und Berechnung des Rostering erstellen.'
**Inhaltstyp:** Anleitungen
**Versionen:**
  - '*'

## Erstellen oder Importieren der Fahrer-Vorlage

Bevor wir über Regeln für Rostering, Ausfälle oder die Zuweisung von Schichten sprechen, benötigen Sie eine zuverlässige Basis von Fahrern. In GoalBus fungiert die Fahrerverwaltung als die Hauptquelle für die menschliche Betriebsführung: sie ermöglicht die Kombination von manueller Erstellung und massiver Upload-Funktion und konzentriert Identität, Zugehörigkeit zum Depot und Verfügbarkeit in einem einzigen Verzeichnis. 
fileciteturn38file2L1-L24


Nutzen Sie diese Quickstart, wenn Sie die Überleitung von Scheduling zu Rostering bereits erfolgreich durchgeführt haben und die realen Personen, die an der Zuweisung teilnehmen, vorbereiten müssen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie die Überleitung von Scheduling in P19 abgeschlossen haben.
2. Sie wissen, welcher Fahrerkreis für den Berechnungsvorgang verwendet wird.
3. Sie wissen, ob Sie nur wenige Fahrer manuell hinzufügen oder eine massives Upload-Funktion benötigen.
4. Sie haben Zugriff auf den Kontext mit den notwendigen Berechtigungen, um Personal zu verwalten.

Für diese Quickstart verwenden Sie diesen Beispielfall:

> **Ich lade und überprüfe die Fahrer-Vorlage, die die Lösung L1 abdecken kann, bevor ich in die Zuweisung, Regeln und Verfügbarkeit eintreten.**

Um die Fahrer-Vorlage zu erstellen oder zu importieren:
1. Gehen Sie in GoalBus zum Modul **Konfiguration** > **Personal** > **Fahrerverwaltung**.
ref: P20_Imagen1.png | compact
2. Überprüfen Sie, ob die Fahrer des Falles bereits in der allgemeinen Liste vorhanden sind.
3. Wenn Sie nur wenige Fahrer hinzufügen müssen, klicken Sie auf **Neuer Fahrer**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn Sie eine massives Upload-Funktion benötigen, führen Sie eine massives Upload-Funktion durch, indem Sie ein CSV-Datei aus **Personal Upload** laden.
ref: P20_Imagen3.png | compact
5. Wenn Sie eine massives Upload-Funktion wählen, bereiten Sie das CSV-Dokument mit den minimalen Daten vor, die Ihre Operation benötigt, um jede Person korrekt zu identifizieren. Die Import-Fenster helfen Ihnen, das CSV-Dokument zu erstellen.
ref: P20_Imagen4.png
6. Führen Sie die Upload-Funktion aus und überprüfen Sie den Ergebnis.
7. Gehen Sie zurück zur allgemeinen Liste und überprüfen Sie, ob die Fahrer korrekt angezeigt werden.
8. Wenn Sie Duplikate oder unvollständige Registrierungen erkennen, korrigieren Sie diese, bevor Sie fortfahren.

Für die Referenz-Situation beenden Sie diese Section erst, wenn Sie bestätigen können:

1. Die Fahrer der L1 sind entweder bereits registriert oder importiert.
2. Die allgemeine Liste zeigt eine einzige Referenz-Vorlage.
3. Sie können den Profil jedes Fahrers öffnen, um seinen operativen Kontext zu überprüfen.

Wenn Sie diese Section abgeschlossen haben, sollten Sie eine Liste mit Fahrern, die in der System sichtbar sind, haben. 
fileciteturn38file0L1-L7
fileciteturn38file2L1-L24

## Überprüfung des Fahrers und seiner strukturellen Daten

Nach der Erstellung der Vorlage müssen Sie den Fahrerprofil überprüfen. Der Profil ist nicht nur eine Kontaktkarte, sondern das digitale Dossier des Mitarbeiters innerhalb der Operation. Dort finden sich statische Daten, operativer Kontext und Attribute, die das System später für die Bewertung seiner Eignung verwenden wird. 
fileciteturn38file0L8-L20
fileciteturn38file2L25-L40

Bevor Sie mit dieser Section beginnen, stellen Sie sicher, dass:

1. Sie bereits Fahrer in der allgemeinen Liste sehen können.
2. Sie wissen, welcher Fahrer oder welcher Gruppe als Referenz dient.
3. Sie die Validierung bestätigen, dass das Register nicht nur administrativer Natur ist, sondern auch operativ.

Um den Fahrerprofil zu überprüfen:

1. Klicken Sie in der allgemeinen Liste auf den Namen eines Fahrers.
ref: P20_Imagen5.png | full
2. Überprüfen Sie die Seitenleiste mit den statischen Daten.
3. Überprüfen Sie mindestens diese Gruppen von Informationen:
   1. Grunddaten, wie Name und Code,
   2. Operative Daten, wie Tarifvertrag oder Arbeitsvertragstyp,
   3. Operative Links, wie Hauptdepot, Arbeitsgruppe, Bereich oder zugelassene Fahrzeugtypen.
4. Fügen Sie gegebenenfalls fehlende Schlüsseldaten ein, bevor Sie fortfahren.
5. Speichern Sie alle Änderungen, die erforderlich sind.
6. Wiederholen Sie die Überprüfung bei mehreren Fahrern, um die Konsistenz in der Vorlage zu bestätigen.

Für die Referenzprüfung überprüfen Sie bitte mindestens:
1. Der Fahrerschein.
2. Sein Hauptdepot.
3. Sein Arbeitsteam.
4. Die operativen Eigenschaften, die seine spätere Zuweisung beeinflussen.

Nach Abschluss dieser Sektion sollten Sie wissen, dass jeder Fahrer einen kohärenten und nutzbaren Betriebsausweis hat. fileciteturn38file0L8-L20


## Überprüfung des operativen Kontextes und dynamischer Daten des Fahrers

Neben den strukturellen Daten enthält der Fahrerprofile auch dynamische Daten, die direkt die Funktionsweise des Systems beeinflussen. In der Verwaltungspfeife können Sie Zähler und Arbeitsmuster überprüfen, die Teil des operativen Kontextes sind, der später von der Assigment-Logik verwendet wird. fileciteturn38file0L12-L17


Bevor Sie diese Sektion beginnen, stellen Sie sicher, dass:
1. Sie die statischen Daten des Profiles überprüft haben.
2. Sie wissen, ob Ihre Operation Zähler oder zyklische Muster verwendet.
3. Sie überprüfen, ob der Fahrer existiert und ein interpretierbarer operativer Kontext hat.

Um den dynamischen operativen Kontext zu überprüfen:
1. Öffnen Sie in der Fahrerprofile die Verwaltungspfeife.
2. Überprüfen Sie die zugehörigen Zähler oder KPI.
3. Überprüfen Sie, ob der Fahrer an einem Arbeitsmuster gebunden ist.
4. Wenn Ihre Operation zyklische Muster verwendet, überprüfen Sie auch den Versatz oder die aktuelle Position des Fahrers im Muster.
5. Stellen Sie sicher, dass diese Daten für den realen Kontext sinnvoll sind.
6. Wenn die dynamischen Daten nicht korrekt sind, passen Sie sie vor dem Übergang zu Regeln oder Berechnungen an.

## Validierung von Berechtigungen vor der Verwendung des Fahrers im Rostering

Bevor Sie einen Fahrer als geeignet betrachten, müssen Sie seine **Berechtigungen** überprüfen. Diese Berechtigungen beantworten die Frage: „Kann diese Person in diesem Depot, Arbeitsgruppe oder Einheit legal oder technisch arbeiten?“ Sie werden in einer Zeitspanne mit Start- und Enddatum verwaltet und das System zeigt den Status als aktiv, zukünftig, abgelaufen oder bald abgelaufen an, um die Lesbarkeit zu erleichtern. Wenn eine Person nicht für den benötigten Kontext berechtigt ist, generiert der Motor einen Fehler beim Versuch, sie zuzuordnen.

## Validierung der Berechtigungen vor der Verwendung des Fahrers im Rostering

Bevor Sie mit dieser Sektion beginnen, stellen Sie sicher, dass:
1. Sie den Fahrerprofil bereits überprüft haben.
2. Sie wissen, welches Depot, Arbeitsgruppe oder Einheit Sie für Ihr Anliegen benötigen.
3. Sie verstehen, dass eine Berechtigungs- ist nicht dasselbe wie eine zeitlich begrenzte Ausleihung oder eine zeitlich begrenzte Zugehörigkeit.

Um die Berechtigungen zu überprüfen und zu validieren, müssen Sie:
1. Öffnen Sie im Fahrerprofil die Registerkarte **Berechtigungen / Qualifikationen**.
2. Überprüfen Sie, ob für:
   1. Depots,
   2. Arbeitsgruppen,
   3. Geschäftsbereiche,
   registrierte Berechtigungen vorhanden sind.
3. Prüfen Sie den visuellen Status jeder Berechtigungs:
   1. aktiv,
   2. zukünftig,
   3. bald abgelaufen,
   4. abgelaufen.
4. Wenn eine notwendige Berechtigungs fehlt, fügen Sie sie mit den korrekten Daten hinzu.
5. Wenn eine Berechtigungs bereits abgelaufen ist und nicht mehr verwendet werden sollte, lassen Sie sie als Historie ohne erneute Eintragung.
6. Speichern Sie die Änderungen.
7. Stellen Sie sicher, dass der Fahrer für den Kontext, in dem Sie ihn verwenden möchten, berechtigt ist.

Für die Referenzfälle ist es erforderlich, bis die Aussage bestätigt ist:
1. Der Fahrer ist für den korrekten Depot zugelassen.
2. Der benötigte Arbeitsteam ist vorhanden.
3. Es gibt keine Ablösungen, die die aktuelle Berechtigung beeinträchtigen.

Nach Abschluss dieser Sektion sollten Fahrer vorhanden sein, die nicht nur in der Planungsliste, sondern auch operativ und normativ elegibel sind. 

## Bestätigung, dass die Planungsliste für die nächste Schicht bereit ist

Der letzte Schritt ist die Überprüfung, ob die Fahrerliste bereits für die nächste Schicht vorbereitet ist:  adscripción operativ, Regeln, Ausfälle und Berechnung. Ziel ist es, eine kohärente, nachvollziehbare und nutzbare Basis für den Motor zu schaffen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie die Planungsliste geladen oder importiert haben.
2. Sie die wichtigsten Profile überprüft haben.
3. Sie die strukturellen und dynamischen Daten überprüft haben.
4. Sie die notwendigen Berechtigungen validiert haben.

Um zu bestätigen, dass die Planungsliste bereit ist:
1. Gehen Sie zur Liste aller Fahrer zurück.
2. Überprüfen Sie, ob das benötigte Kollektiv für Ihren Fall vorhanden ist.
3. Überprüfen Sie, ob die kritischen Profile keine wichtigen Informationen fehlen.
4. Stellen Sie sicher, dass die Personen, die Sie verwenden möchten, für den richtigen Kontext zugelassen sind.
5. Stellen Sie sich die Frage, ob das System diese Basis bereits als Ausgangspunkt für:
   1.  adscripción operativ,
   2.  Rostering-Regeln,
   3.  und tatsächliche Verfügbarkeit verwenden kann.
6. Wenn die Antwort ja ist, beginnen Sie mit dem nächsten Quickstart.
7. Wenn die Antwort nein ist, korrigieren Sie die Fahrerliste, bevor Sie fortfahren.

Für die Referenz-Situation beenden Sie diese Quick Start, sobald Sie folgende Aussagen treffen können:

1. Die Fahrer-Vorlage L1 ist geladen.
2. Die wichtigsten Profile wurden geprüft.
3. Die notwendigen Berechtigungen sind aktiv.
4. Die Basis ist bereit, in die operative Adressierung zu wechseln.

Nach Abschluss dieser Sektion sollten Sie eine ausreichend solide Fahrer-Vorlage haben, um mit der nächsten Schritt des Rostering zu beginnen.

## Zusätzliche Lesungen

- [Betriebliche Adressierung des Fahrers](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)