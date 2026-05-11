---
title: Fahren und Fahrer verwalten
shortTitle: Fahrer
intro: 'Lerne, wie du Fahrer erstellen, importieren und in GoalBus verwalten kannst, ihren operativen Profil überprüfen und eine zuverlässige Vorlage vor der Zuweisung, Regeln und Rostering-Berechnung erstellen kannst.'
contentType: how-tos
versions:
  - '*'
---

## Erstellung oder Importieren der Fahrer-Template

Bevor man über Rostering-Regeln, Abwesenheiten oder Zeitplan- Zuweisungen sprechen kann, benötigt man eine zuverlässige Basis von Fahrern. In GoalBus fungiert die Fahrer-Verwaltung als Hauptquelle der Wahrheit für die menschliche Betriebsführung: sie ermöglicht die Kombination von manueller Erstellung und Massenbelastung und konzentriert Identität, Depot-Zugehörigkeit und Verfügbarkeit in einem einzigen Verzeichnis. fileciteturn38file2L1-L24

Verwende diese Quick-Start-Anleitung, wenn du bereits die Übergabe von Scheduling zu Rostering abgeschlossen hast und das tatsächliche Team von Personen vorbereiten möchtest, das an der Zuweisung beteiligt sein wird.

Bevor du beginnst, stelle sicher, dass:
1. Du die Übergabe von Scheduling in P19 abgeschlossen hast.
2. Du weißt, welches Team von Fahrern an der Berechnung beteiligt sein wird.
3. Du weißt, ob du einige wenige Fahrer manuell eintragen oder eine Massenbelastung benötigst.
4. Du Zugriff auf das Umfeld mit Berechtigungen zur Personalverwaltung hast.

Für diese Quick-Start-Anleitung verwende den folgenden Referenzfall:

> **Ich werde die Fahrer-Template laden und überprüfen, die die Lösung von L1 vor der Einführung von Zuweisungen, Regeln und Verfügbarkeit abdecken kann.**

Um das Fahrer-Template zu erstellen oder zu importieren:
1. Gehe in GoalBus zum Modul **Konfiguration** > **Personal** > **Fahrer-Verwaltung**.
ref: P20_Imagen1.png | compact
2. Überprüfe, ob die Fahrer des Referenzfalls bereits in der allgemeinen Liste vorhanden sind.
3. Wenn du wenige Fahrer erstellen musst, klicke auf **Neuer Fahrer**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn du viele Fahrer importieren musst, führe eine Massenbelastung durch, indem du einen CSV-Datei von **Personalbelastung** aus importierst.
ref: P20_Imagen3.png | compact
5. Wenn du dich für eine Massenbelastung entscheidest, bereite das CSV-Datei vor, indem du die minimalen Daten bereitstellst, die deine Operation benötigt, um jede Person korrekt zu identifizieren. Die Import-Verwaltung wird dir helfen, das CSV-Datei vorzubereiten.
ref: P20_Imagen4.png
6. Führe die Belastung durch und überprüfe das Ergebnis.
7. Gehe zurück zur allgemeinen Liste und überprüfe, ob die Fahrer korrekt angezeigt werden.
8. Wenn du Doppelungen oder unvollständige Einträge entdeckst, korrigiere sie, bevor du fortfährst.

# Bevorzugter Fall

Beende diese Abschnitt nur, wenn du sicher bist:

1. Die Fahrer der L1 sind bereits registriert oder importiert.
2. Die allgemeine Liste spiegelt eine einzelne Referenzvorlage wider.
3. Du kannst bereits das Profil jedes Fahrers öffnen, um seinen operativen Kontext zu überprüfen.

Wenn du diese Abschnitt beendest, sollte eine Vorlage für Fahrer geladen und im System sichtbar sein. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Überprüfung des Fahrerprofils und der strukturierten Daten

Nachdem die Vorlage erstellt wurde, musst du das **Fahrerprofil** überprüfen. Das Profil ist nicht nur eine Kontaktinformation: es ist das digitale Personalakte des Mitarbeiters innerhalb der Operation. Hier werden statische Daten, operativer Kontext und Attribute zusammengeführt, die das System später verwenden wird, um seine Eignung zu bewerten. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Bevor du mit dieser Abschnitt beginnst, stelle sicher:

1. Du hast bereits Fahrer in der allgemeinen Liste sichtbar.
2. Du weißt, welcher Fahrer oder welches Team als Beispiel verwendet wird.
3. Du möchtest überprüfen, ob das Registrieren nicht nur administrativ, sondern auch operativ ist.

Um das Fahrerprofil zu überprüfen:

1. In der allgemeinen Liste klicke auf den Namen eines Fahrers.
ref: P20_Imagen5.png | full
2. Überprüfe die Seitenleiste mit statischen Daten.
3. Überprüfe mindestens diese Gruppen von Informationen:
   1. Grundlegende Daten, wie Name und Code,
   2. Operative Daten, wie Kollektivvertrag oder Vertragsart,
   3. Operative Verbindungen, wie Hauptdepot, Arbeitsgruppe, Bereich oder autorisierte Fahrzeugtypen.
4. Wenn ein wichtiger strukturierter Datenpunkt fehlt, vervollständige ihn, bevor du fortfährst.
5. Speichere alle notwendigen Änderungen.
6. Wiederhole die Überprüfung bei verschiedenen Fahrern, um die Konsistenz in der Vorlage zu bestätigen.

# Bevorzugte Einstellungen für den Fahrer

## Überprüfe die folgenden Einstellungen:

1. Die Fahrer-ID.
2. Sein Hauptdepot.
3. Seine Arbeitsgruppe.
4. Die betreffenden operativen Eigenschaften, die seine spätere Zuweisung beeinflussen werden.

Nachdem du diese Abschnitt abgeschlossen hast, solltest du wissen, dass jeder Fahrer ein kohärentes und verwendbares operatives Profil hat.

## Überprüfung des operativen Kontexts und der dynamischen Daten des Fahrers

Neben den strukturierten Daten enthält das Fahrerprofil auch dynamische Daten, die direkt auf die Art und Weise wirken, wie das System über die Person nachdenkt. In der Verwaltungsoberfläche kannst du Zähler und Arbeitsmuster überprüfen, die Teil des später von der Zuweisungslogik verwendeten operativen Kontexts sind.

## Vorbereitung für diese Abschnitt

Bevor du fortfährst, stelle sicher, dass:

1. Du die statischen Daten des Profils bereits überprüft hast.
2. Du weißt, ob deine Operation Zähler oder zyklische Muster verwendet.
3. Du überprüfen möchtest, ob der Fahrer nicht nur existiert, sondern auch einen interpretierbaren operativen Kontext hat.

## Überprüfung des dynamischen operativen Kontexts

1. Öffne im Fahrerprofil die **Verwaltungsoberfläche**.
2. Überprüfe die **Zähler** oder KPI, die dem Fahrer zugeordnet sind, wenn sie existieren.
3. Überprüfe, ob der Fahrer einem bestimmten **Arbeitsmuster** zugeordnet ist.
4. Wenn deine Operation zyklische Muster verwendet, überprüfe auch den Phasenversatz oder die aktuelle Position des Fahrers innerhalb des Musters.
5. Stelle sicher, dass diese Daten für den realen Kontext Sinn ergeben.
6. Wenn die dynamischen Daten falsch sind, korrigiere sie, bevor du zu Regeln oder Berechnungen übergehst.

# Validierung von Berechtigungen vor der Verwendung des Fahrers im Rostering

Bevor du einen Fahrer als verfügbar betrachtest, musst du seine **Berechtigungen** überprüfen. Diese Berechtigungen beantworten die Frage „Kann diese Person rechtlich oder technisch in diesem Depot, Gruppe oder Bereich arbeiten?“. Sie werden in einer zeitlichen Zeile mit Beginn- und Enddatum verwaltet und der System zeigt Status wie aktiv, zukünftig, abgelaufen oder bald ablaufen, um die Lesbarkeit zu verbessern. Wenn eine Person nicht für den erforderlichen Kontext berechtigt ist, generiert der Motor einen Fehler, wenn er versucht, sie zuzuweisen.

## Voraussetzungen für die Validierung von Berechtigungen

Bevor du mit dieser Abschnitt beginnst, stelle sicher, dass:

1. Du bereits das Profil des Fahrers überprüft hast.
2. Du weißt, welches Depot, Gruppe oder Bereich für deinen Fall benötigt wird.
3. Du verstehst, dass eine Berechtigung nicht gleichbedeutend mit einer zeitweiligen Übertragung oder Zuweisung ist.

## Schritte zur Überprüfung und Validierung von Berechtigungen

1. Öffne im Profil des Fahrers die Registerkarte **Berechtigungen / Qualifikationen**.
2. Überprüfe, ob es aktuelle Einträge für:
   1. Depots,
   2. Arbeitsgruppen,
   3. Geschäftseinheiten gibt.
3. Überprüfe den visuellen Status jeder Berechtigung:
   1. aktiv,
   2. zukünftig,
   3. bald ablaufen,
   4. abgelaufen.
4. Wenn eine notwendige Berechtigung fehlt, füge sie mit den richtigen Datum hinzu.
5. Wenn eine Berechtigung bereits abgelaufen ist und nicht verwendet werden sollte, lasse sie als historisch ohne Versuch, die Vergangenheit zu ändern.
6. Speichere die Änderungen.
7. Bestätige, dass der Fahrer für den Kontext berechtigt ist, in dem du ihn verwenden möchtest.

## Überprüfung der Vorraussetzungen

Bevor du fortfährst, musst du sicherstellen, dass:

1. Der Fahrer für das richtige Depot zugelassen ist.
2. Die erforderliche Arbeitsgruppe abgedeckt ist.
3. Es keine Ablaufdaten gibt, die die aktuelle Eignung beeinträchtigen.

Wenn du diese Schritte abgeschlossen hast, sollten die Fahrer nicht nur in der Vorlage vorhanden sein, sondern auch vom operativen und rechtlichen Standpunkt aus eingesetzt werden können.

## Bestätigung, dass die Vorlage für die nächste Ebene von Rostering bereit ist

Der letzte Schritt besteht darin, sicherzustellen, dass die Fahrerbasis für die nächste Ebene: operative Zuweisung, Regeln, Abwesenheit und Berechnung, bereit ist. Hier geht es nicht nur darum, Namen zu laden, sondern eine kohärente, nachvollziehbare und vom Motor verwendbare Vorlage zu haben.

Bevor du fortfährst, stelle sicher, dass:

1. Du die Vorlage geladen oder importiert hast.
2. Du die Hauptprofile überprüft hast.
3. Du die strukturierten und dynamischen Daten überprüft hast.
4. Du die wesentlichen Zulassungen validiert hast.

Um zu bestätigen, dass die Vorlage bereit ist:

1. Gehe zurück zur allgemeinen Liste der Fahrer.
2. Überprüfe, ob das erforderliche Team für deinen Fall anwesend ist.
3. Überprüfe, ob die kritischen Profile keine wichtigen Informationen fehlen lassen.
4. Stelle sicher, dass die Personen, die du verwenden möchtest, für den richtigen Kontext zugelassen sind.
5. Frage dich, ob das System diese Basis bereits als Ausgangspunkt für:
   1. operative Zuweisung,
   2. Rostering-Regeln,
   3. und tatsächliche Verfügbarkeit verwenden könnte.
6. Wenn die Antwort "ja" lautet, gehe zum nächsten quick start über.
7. Wenn die Antwort "nein" lautet, korrigiere die Fahrerbasis, bevor du fortfährst.

# Beendigung der Quick-Start-Anleitung

Beende diese Quick-Start-Anleitung, wenn du dich sicher bist, dass:

1. Die L1-Fahrer-Template bereits geladen ist.
2. Die Schlüsselfiguren bereits überprüft wurden.
3. Die wesentlichen Genehmigungen gültig sind.
4. Die Basis für die operative Zuweisung bereit ist.

Wenn du diese Schritte abgeschlossen hast, sollte deine Fahrer-Template ausreichend stabil sein, um mit der nächsten Ebene von Rostering fortfahren zu können.

## Weitere Informationen

- [Fahrer-Zuweisung](P21_Fahrer-Zuweisung.md)