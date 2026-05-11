---
title: Caricamento e gestione dei conducenti
shortTitle: Conducenti
intro: 'Impara a creare, importare e mantenere la base dei conducenti in GoalBus, revisionare il loro profilo operativo e lasciare una bozza fiable prima di passare alla adscriptione, regole e calcolo del Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Creando o importando la plantilla di dirottatori

Prima di discutere le regole di Rostering, assenze o assegnazione dei turni, è necessario avere una base fiable di dirottatori. In GoalBus, la gestione dei dirottatori agisce come la fonte principale di verità per l'operatività umana: permette di combinare la creazione manuale e la carica maschera, e concentra identità, appartenenza al deposito e disponibilità in un unico elenco. fileciteturn38file2L1-L24

Usa questa quick start quando già hai chiaro la transizione da Scheduling a Rostering e necessiti di preparare il team reale di persone che parteciperà all'assegnazione.

Prima di iniziare, assicurati di:
1. Avere già chiusa la transizione da Scheduling in P19.
2. Sapere quale team di dirottatori parteciperà al calcolo.
3. Sapere se vuoi inserire pochi dirottatori manualmente o se necessiti di una carica maschera.
4. Avere accesso all'ambiente con i permessi per gestire il personale.

Per questa quick start, usa questo caso di riferimento:

> **Voglio caricare e revisionare la plantilla di dirottatori che potrà coprire la soluzione di L1 prima di entrare in adesione, regole e disponibilità.**

Per creare o importare la plantilla di dirottatori:
1. In GoalBus, vai al modulo di **Configurazione** > **Personale** > **Gestione dirottatori**.
ref: P20_Imagen1.png | compact
2. Controlla se i dirottatori del caso già esistono nella lista generale.
3. Se necessiti creare pochi dirottatori, clicca su **Nuovo Dirottatore**.
ref: P20_Imagen2.png | compact(2x)
4. Se necessiti caricare molti dirottatori, esegui una carica maschera tramite file CSV da **Carica Personale**.
ref: P20_Imagen3.png | compact
5. Se scegli la carica maschera, prepara il file con i dati minimi necessari per identificare correttamente ogni persona. La finestra di importazione agirà come aiuto per preparare il CSV di carica.
ref: P20_Imagen4.png
6. Esegui la carica e controlla il risultato.
7. Torna alla lista generale e verifica che i dirottatori appaiano correttamente.
8. Se rilevi duplicati o registri incompleti, correggili prima di proseguire.

Per il caso di riferimento, termina questa sezione solo quando puoi affermare:
1. I conducenti di L1 sono già iscritti o importati.
2. La lista generale riflette una singola plantilla di riferimento.
3. Puoi già aprire il profilo di ogni conducente per revisionare il suo contesto operativo.

Quando termini questa sezione, dovresti avere una plantilla di conducenti caricata e visibile nel sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando il profilo del conducente e i suoi dati strutturali

Una volta creata la plantilla, necessiti di revisionare il **profilo del conducente**. Il profilo non è solo una scheda di contatto: è il fascicolo digitale completo dell'impiegato all'interno dell'operazione. Qui convivono dati statici, contesto operativo e attributi che il sistema userà più tardi per ragionare sulla sua elegibilità. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Prima di iniziare questa sezione, assicurati di:
1. Avere già conducenti visibili nella lista generale.
2. Sapere quale conducente o quale gruppo userai come esempio.
3. Voler validare che il registro non sia solo amministrativo, ma operativo.

Per revisionare il profilo del conducente:
1. Nella lista generale, clicca sul nome di un conducente.
ref: P20_Imagen5.png | full
2. Revisiona la barra laterale dei dati statici.
3. Controlla almeno questi gruppi di informazioni:
   1. dati basilari, come nome e codice,
   2. dati operativi, come convenzione collettiva o tipo di contratto,
   3. collegamenti operativi, come deposito principale, gruppo di lavoro, area o tipi di veicoli autorizzati.
4. Se qualche dato strutturale chiave manca, completalo prima di procedere.
5. Salva qualsiasi modifica necessaria.
6. Ripeti la revisione in diversi conducenti per confermare la coerenza nella plantilla.

Per il caso di riferimento, verifica almeno:
1. Il codice del conducente.
2. Il suo deposito principale.
3. Il suo team di lavoro.
4. Le proprietà operative che condizioneranno la sua successiva assegnazione.

Quando avrai finito questa sezione, dovresti avere chiaro che ogni conducente dispone di un'operazione coerenza e utilizzabile. fileciteturn38file0L8-L20

## Verificando il contesto operativo e i dati dinamici del conducente

In aggiunta ai dati strutturati, il profilo del conducente include dati dinamici che influenzano direttamente come il sistema ragioni sulla persona. Nella scheda di amministrazione puoi verificare i contatori e i pattern di lavoro, che fanno parte del contesto operativo utilizzato successivamente dalla logica di assegnazione. fileciteturn38file0L12-L17

Prima di iniziare questa sezione, assicurati di:
1. Avere già verificato i dati statici del profilo.
2. Sapere se la tua operazione utilizza contatori o pattern ciclici.
3. Verificare che il conducente non solo esista, ma abbia un contesto operativo interpretabile.

Per verificare il contesto operativo dinamico:
1. Nella scheda del conducente, apri la scheda **Dettagli amministrativi**.
2. Verifica i **contatori** o KPI associati al conducente se esistono.
3. Controlla se il conducente è associato a qualche **pattern di lavoro**.
4. Se la tua operazione utilizza pattern ciclici, verifica anche il ritardo o la posizione attuale del conducente all'interno del pattern.
5. Conferma che questi dati abbiano senso nel contesto reale.
6. Se le informazioni dinamiche non sono corrette, correggile prima di passare alle regole o al calcolo.

Per il caso di riferimento, chiediti:
1. Questo conducente ha il pattern che dovrebbe avere?
2. Le sue contabilità o KPI sono disponibili se il processo ne ha bisogno?
3. Il sistema potrebbe ragionare correttamente su questa persona in un calcolo di reliefs?

Quando hai finito questa sezione, dovresti avere validata non solo l'identità del conducente, ma anche il suo contesto operativo dinamico. fileciteturn38file0L12-L17

## Validando le habilitazioni prima di utilizzare il conducente in Rostering

Prima di considerare un conducente come elegibile, devi revisionare le sue **habilitazioni**. Queste habilitazioni rispondono alla domanda “Può questa persona lavorare legalmente o tecnicamente in questo deposito, gruppo o unità?”. Le gestiscono in una linea temporale con data di inizio e fine, e il sistema mostra stati come attivo, futuro, scaduto o prossimo a scadere per facilitare la lettura. Se una persona non è habilitata per il contesto richiesto, il motore genera un errore al tentativo di assegnarla. fileciteturn38file0L17-L34

Prima di iniziare questa sezione, assicurati di:
1. Avere già revisionato il profilo del conducente.
2. Conoscere già il deposito, gruppo o unità necessario per il tuo caso.
3. Capire che una habilitazione non è la stessa di una cessione o di un addebito temporaneo.

Per revisionare e validare le habilitazioni:
1. Nella scheda del profilo del conducente, apri la scheda **Habilitazioni / Cualificazioni**.
2. Verifica se esistono registri attivi per:
   1. depositi,
   2. gruppi di lavoro,
   3. unità di business.
3. Controlla lo stato visivo di ogni habilitazione:
   1. attiva,
   2. futura,
   3. prossima a scadere,
   4. scaduta.
4. Se manca una habilitazione necessaria, aggiungila con le date corrette.
5. Se una habilitazione è già scaduta e non dovrebbe essere utilizzata, lasciala come storica senza provare a riscrivere il passato.
6. Salva i cambiamenti.
7. Conferma che il conducente sia già habilitato per il contesto dove lo si intende utilizzare.

Per il caso di riferimento, non procedere fino a quando non potrai affermare:
1. Il conducente è habilitato per il deposito corretto.
2. Il team richiesto è coperto.
3. Non ci sono scadenze che rompano l'attuale elegibilità.

Quando avrai finito questa sezione, dovresti avere conducenti non solo presenti nella plantilla, ma anche operativamente e normativamente elegibili. fileciteturn38file0L17-L34

## Confermando che la plantilla sia pronta per la successiva fase di Rostering

L'ultimo passo è verificare che la base di conducenti sia pronta per entrare nella successiva fase: adesione operativa, regole, assenze e calcolo. L'obiettivo non è solo avere nomi caricati, ma una plantilla coerente, tracciabile e utilizzabile dal motore.

Prima di concludere, assicurati di:
1. Avere già caricato o importato la plantilla.
2. Avere già verificato i profili principali.
3. Avere già controllato i dati strutturali e dinamici.
4. Avere già validato le habilitazioni essenziali.

Per confermare che la plantilla sia già pronta:
1. Torna alla lista generale dei conducenti.
2. Verifica che il gruppo necessario per il tuo caso sia presente.
3. Controlla che i profili critici non abbiano vuoti importanti.
4. Assicurati che le persone che intende utilizzare siano habilitate per il contesto corretto.
5. Poni la domanda se il sistema potrebbe già utilizzare questa base come punto di partenza per:
   1. adesione operativa,
   2. regole di Rostering,
   3. e disponibilità reale.
6. Se la risposta è sì, continua con il prossimo quick start.
7. Se la risposta è no, correggi la base di conducenti prima di procedere.

Per il caso di riferimento, termina questa quick start solo quando puoi affermare:
1. La plantilla dei conducenti di L1 già è caricata.
2. I profili chiave già sono stati revisionati.
3. Le habilitazioni essenziali già sono in vigore.
4. La base già è pronta per passare all'admissione operativa.

Quando termini questa sezione, dovresti avere una plantilla dei conducenti sufficientemente solida per continuare con la successiva layer di rostering.

## Letture aggiuntive

- [Gestione dell'admissione operativa del conducente](P21_Gestionando_la_adscripcion_operativa_del_conducente.md)