---
title: Cargando y gestionando conductores
shortTitle: Conductores
intro: 'Lernen Sie, Fahrer in GoalBus zu erstellen, zu importieren und zu verwalten, deren operativen Profil zu überprüfen und eine zuverlässige Vorlage vor der Adscriptio, Regeln und Roster-Berechnung bereitzustellen.'
contentType: how-tos
versions:
  - '*'
---

## Erstellen oder Importieren der Fahrer-Vorlage

Bevor Sie sich mit Regeln für die Auslastung, Abwesenheiten oder Schichtzuweisungen befassen, benötigen Sie eine zuverlässige Basis von Fahrern. In GoalBus dient die Fahrerverwaltung als Hauptquelle für die menschliche Betriebswirtschaft: Sie ermöglicht die Kombination von manueller Erstellung und Masseneingabe und konzentriert Identität, Verbindung zum Depot und Verfügbarkeit in einem einzigen Verzeichnis. fileciteturn38file2L1-L24

Verwenden Sie diese Quickstart, wenn Sie die Übergang von der Planung zur Auslastung verstanden haben und Sie bereit sind, das tatsächliche Team von Personen zu bereiten, die an der Zuweisung teilnehmen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie die Übergang von der Planung in P19 abgeschlossen haben.
2. Sie wissen, welches Team von Fahrern an dem Berechnungsprozess beteiligt sein wird.
3. Sie wissen, ob Sie einige Fahrer manuell hinzufügen oder eine Masseneingabe benötigen.
4. Sie Zugriff auf das Umfeld mit den erforderlichen Berechtigungen für die Personalverwaltung haben.

Für diese Quickstart verwenden Sie folgenden Referenzfall:

> **Ich werde die Fahrer-Vorlage laden und überprüfen, die die Lösung für L1 vor der Zuordnung bedienen kann, bevor ich mich mit den Zuweisungsregeln und der Verfügbarkeit befasse.**

Um die Fahrer-Vorlage zu erstellen oder zu importieren:
1. In GoalBus gehen Sie zu **Konfiguration** > **Personal** > **Fahrerverwaltung**.
ref: P20_Imagen1.png | compact
2. Überprüfen Sie, ob die Fahrer des Referenzfalls bereits in der allgemeinen Liste vorhanden sind.
3. Wenn Sie einige Fahrer erstellen müssen, klicken Sie auf **Neuer Fahrer**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn Sie viele Fahrer hinzufügen müssen, führen Sie eine Masseneingabe über CSV-Datei in **Personalen Eingabe** durch.
ref: P20_Imagen3.png | compact
5. Wenn Sie eine Masseneingabe wählen, bereiten Sie die Datei mit den notwendigen minimalem Daten vor, die Ihre Betriebswirtschaft benötigt, um jede Person eindeutig zu identifizieren. Die Importvorschau wird Ihnen bei der Vorbereitung der Eingabedatei helfen.
ref: P20_Imagen4.png
6. Führen Sie die Eingabe durch und überprüfen Sie das Ergebnis.
7.kehren Sie zur allgemeinen Liste zurück und stellen Sie sicher, dass die Fahrer korrekt angezeigt werden.
8. Wenn Sie Duplikate oder unvollständige Einträge feststellen, korrigieren Sie diese vor dem Fortfahren.

Für den Fall der Referenz beende diese Abschnitt nur, wenn du folgende Bedingungen erfüllt haben kannst:
1. Die Fahrer der L1 sind bereits registriert oder importiert.
2. Die allgemeine Liste spiegelt eine einheitliche Referenz-Template wider.
3. Du kannst den Profilansicht jedes Fahrers öffnen, um dessen Betriebskontext zu überprüfen.

Wenn du diese Abschnitt beendet hast, solltest du ein Fahrer-Template geladen und sichtbar im System haben. fileciteturn38file0L1-7 fileciteturn38file2L1-24

## Überprüfen des Fahrerprofils und seiner strukturierten Daten

Nach Erstellung des Templates musst du das **Fahrerprofil** überprüfen. Das Profil ist nicht nur eine Kontaktaufnahme: es ist das digitale Lebensbuch des Mitarbeiters innerhalb der Betriebsoperation. Es vereint statische Daten, Betriebskontext und Attribute, die das System später für die Berechnung seiner Qualifikation verwendet. fileciteturn38file0L8-20 fileciteturn38file2L25-40

Bevor du diese Abschnitt beginnst, stelle sicher, dass:
1. Fahrer bereits in der allgemeinen Liste sichtbar sind.
2. Du weißt, welchen Fahrer oder welches Fahrer-Team du als Beispiel verwenden wirst.
3. Du überprüfen möchtest, ob der Eintrag nicht nur administrativ, sondern auch betriebswirtschaftlich ist.

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
6. Führe die Überprüfung für mehrere Fahrer durch, um die Konsistenz im Template zu bestätigen.

Para den referencefall, überprüfe mindestens:
1. Das Fahrer-Kennzeichen.
2. Sein Hauptdepot.
3. Seinen Arbeitsbereich.
4. Die operativen Eigenschaften, die seine zukünftige Zuweisung beeinflussen.

Nach Abschluss dieser Abschnitt solltest du verstehen, dass jeder Fahrer ein kohärentes und nutzbares Fahrer-Handbuch besitzt. fileciteturn38file0L8-L20

## Überprüfen des operativen Kontextes und der dynamischen Daten des Fahrers

Außer den strukturellen Daten umfasst das Fahrerprofil auch dynamische Daten, die direkt auf die Art und Weise beeinflussen, wie das System die Person interpretiert. In der Verwaltungstabelle kannst du Zähler und Arbeitsmuster überprüfen, die später von der Zuweisungslogik im operativen Kontext verwendet werden. fileciteturn38file0L12-L17

Bevor du diese Abschnitt beginnst, stelle sicher, dass:
1. Du die statischen Daten des Profils bereits überprüft hast.
2. Du weißt, ob deine Operation Zähler oder zyklische Muster verwendet.
3. Du überprüfst, ob der Fahrer nicht nur existiert, sondern auch einen interpretierbaren operativen Kontext hat.

Um den dynamischen operativen Kontext zu überprüfen:
1. In dem Fahrerprofil öffnest du die Registerkarte **Verwaltungsdetails**.
2. Überprüfe die **Zähler** oder KPI, die dem Fahrer zugeordnet sind, wenn sie vorhanden sind.
3. Überprüfe, ob der Fahrer an einem Arbeitsmuster gebunden ist.
4. Wenn deine Operation zyklische Muster verwendet, überprüfe auch den Verschiebung oder die aktuelle Position des Fahrers innerhalb des Musters.
5. Stelle sicher, dass diese Daten für den realen Kontext Sinn ergeben.
6. Wenn die dynamischen Daten nicht korrekt sind, korrigiere sie vor dem Übergang zu Regeln oder Berechnungen.

Für den Fall der Verwendung, fragen Sie sich:
1. Hat dieser Fahrer das Patrön, das er haben sollte?
2. Sind seine Zähler oder KPI verfügbar, wenn der Prozess sie benötigt?
3. Könnte das System korrekt über diese Person im Berechnungsprozess rechnen?

Wenn Sie diese Abschnitt beendet haben, sollten Sie nicht nur die Identität des Fahrers, sondern auch seinen dynamischen Betriebskontext validiert haben. fileciteturn38file0L12-L17

## Validieren von Berechtigungen vor der Nutzung des Fahrers im Roster

Bevor ein Fahrer als qualifiziert angesehen wird, müssen Sie seine **Berechtigungen** überprüfen. Diese Berechtigungen beantworten die Frage: „Kann diese Person legal oder technisch im Depot, im Team oder in der Einheit arbeiten?“. Sie werden in einer zeitlichen Achse mit Start- und Enddatum verwaltet, und das System zeigt Zustände wie aktiv, zukünftig, abgelaufen oder nahezu abgelaufen an, um eine einfache Lesbarkeit zu gewährleisten. Wenn eine Person nicht für den erforderlichen Kontext berechtigt ist, generiert das System einen Fehler, wenn sie versucht wird zugewiesen zu werden. fileciteturn38file0L17-L34

Bevor Sie diese Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie den Fahrerprofil bereits überprüft haben.
2. Sie wissen, welches Depot, Team oder Einheit für Ihren Fall erforderlich ist.
3. Sie verstehen, dass eine Berechtigung nicht dasselbe ist wie eine Übertragung oder eine temporäre Zuordnung.

Um die Berechtigungen zu überprüfen und zu validieren:
1. Innerhalb des Fahrerprofils öffnen Sie die Registerkarte **Berechtigungen / Qualifikationen**.
2. Überprüfen Sie, ob es aktuelle Einträge für:
   1. Depots,
   2. Arbeitsgruppen,
   3. Geschäftsuniten gibt.
3. Prüfen Sie den visuellen Zustand jeder Berechtigung:
   1. aktiv,
   2. zukünftig,
   3. nahezu abgelaufen,
   4. abgelaufen.
4. Wenn eine erforderliche Berechtigung fehlt, fügen Sie sie mit den richtigen Datumsangaben hinzu.
5. Wenn eine Berechtigung abgelaufen ist und sie nicht mehr verwendet werden sollte, lassen Sie sie als historisch und versuchen Sie nicht, das Vergangene zu ändern.
6. Speichern Sie die Änderungen.
7. Stellen Sie sicher, dass der Fahrer für den Kontext berechtigt ist, in dem Sie ihn verwenden möchten.

Für den Fall der Referenz solltest du nicht fortfahren, bis du folgende Bedingungen erfüllt hast:
1. Der Fahrer ist für den richtigen Depotbereich ausgebildet.
2. Der erforderliche Arbeitsbereich ist abgedeckt.
3. Es gibt keine Ablaufdaten, die die aktuelle Qualifikation stören.

Wenn du diese Abschnitt beendet hast, solltest du Fahrer haben, die nicht nur in der Vorlage existieren, sondern auch operativ und rechtlich qualifiziert sind. fileciteturn38file0L17-L34

## Bestätigen, dass die Vorlage für die nächste Ebene der Rosterplanung bereit ist

Der letzte Schritt ist die Überprüfung, ob die Fahrerbasis für die nächste Ebene bereit ist: operative Zuordnung, Regeln, Abwesenheiten und Berechnung. Hier geht es nicht nur darum, Namen zu laden, sondern um eine kohärente, nachvollziehbare und nutzbare Vorlage.

Bevor du fertig bist, stelle sicher, dass:
1. Du die Vorlage bereits geladen oder importiert hast.
2. Du die Hauptprofile bereits überprüft hast.
3. Du die strukturellen und dynamischen Daten bereits geprüft hast.
4. Du die wesentlichen Qualifikationen bereits validiert hast.

Um zu bestätigen, dass die Vorlage bereit ist:
1. Gehe zur allgemeinen Fahrerliste.
2. Überprüfe, ob der notwendige Kollektivum für deinen Fall vorhanden ist.
3. Stelle sicher, dass kritische Profile keine wichtigen Informationen fehlen.
4. Stelle sicher, dass die Personen, die du verwenden möchtest, für den richtigen Kontext qualifiziert sind.
5. Frage dich, ob das System diese Basis bereits als Ausgangspunkt für:
   1. operative Zuordnung,
   2. Rosterplanungsregeln,
   3. und reale Verfügbarkeit verwenden könnte.
6. Wenn die Antwort ja ist, fahre mit dem nächsten Quick Start fort.
7. Wenn die Antwort nein ist, korrigiere die Fahrerbasis vor dem Fortfahren.

Para den.Reference, beende diese Quick Start nur, wenn du folgende Punkte bestätigen kannst:
1. Die L1-Fahrer-Vorlage ist bereits geladen.
2. Die Schlüsselprofile wurden bereits überprüft.
3. Die wesentlichen Berechtigungen sind bereits gültig.
4. Die Basis ist bereit für die Übergabe zur operativen Adscription.

Wenn du diese Abschnitt beendet hast, solltest du eine Fahrer-Vorlage haben, die ausreichend stabil ist, um zur nächsten Roster-Layer fortzufahren.

## Zusätzliche Lektüre

- [Gestionando la adscripción operativa del conductor](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)