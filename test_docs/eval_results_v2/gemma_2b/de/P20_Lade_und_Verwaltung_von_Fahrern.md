---
title: ```markdown
Cargando y gestionando conductores
```
shortTitle: Fahrer
intro: Erfahren Sie, wie Sie die Basis von Fahrern in GoalBus erstellen, importieren und pflegen, ihre operative Profile überprüfen und eine zuverlässige Planungsvorlage erstellen, bevor Sie sich auf Adressierung, Regeln und das Rostering-System beziehen.
contentType: how-tos
versions:
  - '*'
---

## Erstellen oder Importieren der Fahrer-Vorlage

Bevor wir über Regeln für Rostering, Ausfälle oder die Zuweisung von Schichten sprechen, benötigen Sie eine zuverlässige Basis von Fahrern. In GoalBus fungiert die Fahrerverwaltung als die Hauptquelle für die menschliche Betriebsfähigkeit: sie ermöglicht die Kombination von manueller Erstellung und massiver Upload, und konzentriert Identität, Zugehörigkeit zum Depot und Verfügbarkeit in einem einzigen Verzeichnis. 
fileciteturn38file2L1-L24

Nutzen Sie diese Quickstart, wenn Sie bereits die Überleitung von Scheduling zu Rostering klar haben und die realen Personen, die an der Zuweisung teilnehmen, vorbereiten müssen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie die Überleitung von Scheduling in P19 abgeschlossen haben.
2. Sie wissen, welcher Fahrerkreis für den Berechnungsvorgang verwendet wird.
3. Sie wissen, ob Sie nur wenige Fahrer manuell hinzufügen oder eine massives Upload benötigen.
4. Sie haben Zugriff auf das Umfeld mit den notwendigen Berechtigungen, um Personal zu verwalten.

Für diese Quickstart verwenden Sie diesen Beispielfall:

> **Ich lade und überprüfe die Fahrer-Vorlage, die die Lösung L1 abdecken kann, bevor ich in die Zuweisung, Regeln und Verfügbarkeit eintreten.**

Um die Fahrer-Vorlage zu erstellen oder zu importieren:
1. Gehen Sie in GoalBus zum Modul **Konfiguration** > **Personal** > **Fahrerverwaltung**.
ref: P20_Imagen1.png | compact
2. Überprüfen Sie, ob die Fahrer aus dem Beispielfall bereits in der allgemeinen Liste vorhanden sind.
3. Wenn Sie nur wenige Fahrer erstellen müssen, klicken Sie auf **Neuer Fahrer**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn Sie viele Fahrer importieren müssen, führen Sie eine massives Upload durch, indem Sie ein CSV-Datei aus **Personal Upload** laden.
ref: P20_Imagen3.png | compact
5. Wenn Sie massives Upload wählen, bereiten Sie den CSV-Datei mit den notwendigen Daten vor, die Ihre Operation benötigt, um jede Person korrekt zu identifizieren. Die Import-Fenster helfen Ihnen, den CSV-Datei zu erstellen.
ref: P20_Imagen4.png
6. Führen Sie die Upload-Operation aus und überprüfen Sie den Ergebnis.
7. Gehen Sie zurück zur allgemeinen Liste und überprüfen Sie, ob die Fahrer korrekt angezeigt werden.
8. Wenn Sie Duplikate oder unvollständige Registrierungen finden, korrigieren Sie diese, bevor Sie fortfahren.

##  Referenz-Abschluss

**Referenz-Abschluss**

1. Die Fahrer der L1-Linie sind entweder bereits registriert oder importiert.
2. Die allgemeine Liste zeigt eine einzige Referenz-Vorlage.
3. Sie können nun den Profilen jedes Fahrers zugreifen, um seinen operativen Kontext zu überprüfen.

**Abschluss**

Nach Abschluss dieser Sektion sollte eine geplante Fahrer-Vorlage im System sichtbar sein. 
fileciteturn38file0L1-L7
fileciteturn38file2L1-L24

##  Fahrerprofil und strukturelle Daten

Nach der Erstellung der Vorlage müssen Sie das **Fahrerprofil** überprüfen. Das Profil ist nicht nur eine Kontaktkarte: es ist das digitale Dossier des Mitarbeiters innerhalb der Operation. Dort finden sich statische Daten, operativer Kontext und Attribute, die das System später für die Bewertung seiner Eignung verwenden wird. 
fileciteturn38file0L8-L20
fileciteturn38file2L25-L40

**Vor Beginn dieser Sektion:**

1. Stellen Sie sicher, dass Fahrer in der allgemeinen Liste sichtbar sind.
2. Sie wissen, welcher Fahrer oder welcher Gruppe als Referenz dient.
3. Sie wollen sicherstellen, dass das Register nicht nur administrativer Natur ist, sondern auch operativ relevant ist.

**Um das Fahrerprofil zu überprüfen:**

1. Klicken Sie im allgemeinen Register auf den Namen eines Fahrers.
ref: P20_Imagen5.png | full
2. Überprüfen Sie die Seitenleiste mit den statischen Daten.
3. Überprüfen Sie mindestens diese Gruppen von Informationen:
   1. Grundlegende Daten, wie Name und Code,
   2. Operative Daten, wie Tarifvereinbarung oder Vertragsart,
   3. Operative Links, wie Hauptdepot, Arbeitsgruppe, Bereich oder zugelassene Fahrzeugtypen.
4. Fügen Sie fehlende Schlüsseldaten ein, bevor Sie fortfahren.
5. Speichern Sie alle Änderungen.
6. Wiederholen Sie die Überprüfung bei mehreren Fahrern, um die Konsistenz der Vorlage zu gewährleisten.

Für die Referenzprüfung überprüfen Sie bitte mindestens:
1. Den Fahrerscheinkodex.
2. Sein Hauptdepot.
3. Sein Arbeitsteam.
4. Die operativen Eigenschaften, die seine spätere Zuweisung beeinflussen.

Sobald Sie diese Sektion abgeschlossen haben, sollten Sie wissen, dass jeder Fahrer einen kohärenten und nutzbaren Betriebserfahrung hat. 
fileciteturn38file0L8-L20

## Kontextualisierung des Betriebes und dynamische Daten des Fahrers

Neben den strukturellen Daten enthält der Fahrerprofile auch dynamische Daten, die direkt die Funktionsweise des Systems beeinflussen. In der Verwaltungspfeife können Sie Zähler und Arbeitsmuster überprüfen, die im Kontext des Betriebes verwendet werden, um die Logik der Zuweisung zu unterstützen. 
fileciteturn38file0L12-L17

Bevor Sie mit dieser Sektion beginnen, stellen Sie sicher, dass:
1. Sie die statischen Daten des Profiles überprüft haben.
2. Sie wissen, ob Ihre Operation Zähler oder zyklische Muster verwendet.
3. Sie überprüfen, ob der Fahrer existiert und ein interpretierbarer Betriebskontext hat.

Um den dynamischen Kontext zu überprüfen:
1. Öffnen Sie in der Fahrerprofil-Detailansicht die Verwaltungspfeife.
2. Überprüfen Sie die zugehörigen Zähler oder KPIs.
3. Überprüfen Sie, ob der Fahrer an einem Arbeitsmuster gebunden ist.
4. Wenn Ihre Operation zyklische Muster verwendet, überprüfen Sie den Abstand oder die aktuelle Position des Fahrers im Muster.
5. Stellen Sie sicher, dass diese Daten für den realen Kontext sinnvoll sind.
6. Wenn die dynamischen Daten nicht korrekt sind, passen Sie sie vor dem Übergang zu Regeln oder Berechnungen an.

##  Validierung der Berechtigungen vor der Verwendung des Fahrers in Rostering

Bevor ein Fahrer als geeignet angesehen werden kann, muss die **Berechtigung** überprüft werden. Diese Berechtigungen beantworten die Frage: „Kann diese Person rechtlich oder technisch in diesem Depot, Team oder Einheit arbeiten?“ Sie werden in einer Zeitspanne mit Start- und Enddatum verwaltet und das System zeigt den Status als aktiv, zukünftig, abgelaufen oder bald abgelaufen an, um die Lesbarkeit zu erleichtern. Wenn eine Person nicht für den benötigten Kontext berechtigt ist, generiert der Motor einen Fehler beim Versuch, sie zuzuordnen. 

## Validierung der Berechtigungen vor der Verwendung des Fahrers in Rostering

Bevor Sie diese Sektion beginnen, stellen Sie sicher, dass:

1. Sie den Fahrerprofil bereits überprüft haben.
2. Sie wissen, welches Depot, Team oder Einheit für Ihr Fall benötigt wird.
3. Sie verstehen, dass eine Beretigung nicht dasselbe ist wie eine zeitlich begrenzte Ausleihung oder eine zeitliche Zugehörigkeit.

Um die Berechtigungen zu überprüfen und zu validieren:

1. Öffnen Sie im Fahrerprofil die Registerkarte **Berechtigungen / Qualifikationen**.
2. Überprüfen Sie, ob es gültige Registrierungen für:
   1. Depots,
   2. Arbeitsgruppen,
   3. Geschäftsbereiche gibt.
3. Prüfen Sie den visuellen Status jeder Beretigung:
   1. aktiv,
   2. zukünftig,
   3. bald abgelaufen,
   4. abgelaufen.
4. Wenn eine notwendige Beretigung fehlt, fügen Sie sie mit den korrekten Daten hinzu.
5. Wenn eine Beretigung bereits abgelaufen ist und nicht mehr verwendet werden sollte, lassen Sie sie als Historie speichern, ohne sie zu überarbeiten.
6. Speichern Sie die Änderungen.
7. Stellen Sie sicher, dass der Fahrer für den Kontext, in dem Sie ihn verwenden möchten, berechtigt ist.

Für die Referenz-Situation ist es wichtig, bis zu diesem Zeitpunkt zu bestätigen:
1. Der Fahrer ist für den richtigen Depot zugelassen.
2. Der benötigte Arbeitsteam ist vorhanden.
3. Es gibt keine Ausnahmen, die die aktuelle Berechtigung beeinträchtigen.

Sobald diese Sektion abgeschlossen ist, sollten Fahrer vorhanden sein, die nicht nur in der Planungsliste, sondern auch operativ und normativ elegibel sind. 

**[fileciteturn38file0L17-L34]**

## Bestätigung, dass die Planungsliste für die nächste Schicht bereit ist

Der letzte Schritt ist, zu überprüfen, ob die Datenbank der Fahrer bereits für die nächste Schicht vorbereitet ist: operative Adressierung, Regeln, Ausfälle und Berechnung. Ziel ist es, eine planbare, tragbare und nutzbare Basis für den Motor zu schaffen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie die Planungsliste geladen oder importiert haben.
2. Sie die wichtigsten Profile überprüft haben.
3. Sie die strukturellen und dynamischen Daten überprüft haben.
4. Sie die notwendigen Berechtigungen validiert haben.

Um zu bestätigen, dass die Planungsliste bereit ist:
1. Gehen Sie zur Liste aller Fahrer zurück.
2. Überprüfen Sie, ob das benötigte Team für Ihren Fall vorhanden ist.
3. Überprüfen Sie, ob die kritischen Profile keine wichtigen Informationen fehlen.
4. Stellen Sie sicher, dass die Personen, die Sie verwenden möchten, für den richtigen Kontext zugelassen sind.
5. Stellen Sie sich die Frage, ob das System diese Basis bereits als Ausgangspunkt für:
   1. operative Adressierung,
   2. Regeln für Rostering,
   3. und realistische Verfügbarkeit verwenden kann.
6. Wenn die Antwort ja ist, starten Sie mit dem nächsten Quick Start.
7. Wenn die Antwort nein ist, korrigieren Sie die Fahrerbasis, bevor Sie fortfahren.

Für die Referenz-Situation beenden Sie diese Quickstart, sobald Sie die folgenden Punkte bestätigen können:
1. Die Fahrer-Vorlage L1 ist geladen.
2. Die wichtigsten Profile wurden geprüft.
3. Die notwendigen Berechtigungen sind aktiv.
4. Die Basis ist bereit für die operative Adressierung.

Nach Abschluss dieser Sektion sollten Sie eine ausreichend solide Fahrer-Vorlage haben, um mit der nächsten Schritt der Rostering zu beginnen.

## Zusätzliche Lesungen

- [Verwalten der operative Adressierung des Fahrers](P21_Verwalten_der_operative_Adressierung_des_Fahrers.md)