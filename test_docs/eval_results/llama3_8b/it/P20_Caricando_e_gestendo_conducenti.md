---
title: Cargando e gestendo i conducenti
shortTitle: Conducenti
intro: 'Impara a creare, importare e mantenere la base dei conducenti in GoalBus, esaminare il profilo operativo e lasciare un modello affidabile prima di passare a adesione, regole e calcolo del cuadrante.'
contentType: how-tos
versions:
  - '*'
---

## Creando o importando la plantilla di conducenti

Prima di parlare di regole di Rostering, assenze o assegnazione di turni, hai bisogno di avere una base affidabile di conducenti. In GoalBus, la gestione di conducenti agisce come la fonte principale di verità per l'operatività umana: consente di combinare creazione manuale e carica di massa, e concentra identità, affiliazione al deposito e disponibilità in un unico directory. fileciteturn38file2L1-L24

Usa questa quick start quando già hai chiaro la transizione da Scheduling a Rostering e hai bisogno di preparare il team reale di persone che parteciperà all'assegnazione.

Prima di iniziare, assicurati di:
1. Aver chiuso la transizione da Scheduling in P19.
2. Di avere chiaro quale team di conducenti parteciperà al calcolo.
3. Di sapere se vuoi registrare alcuni pochi conducenti manualmente o se hai bisogno di una carica di massa.
4. Di avere accesso all'ambiente con permessi per gestire il personale.

Per questa quick start, usa questo caso di riferimento:

> **Vorrei caricare e revisionare la plantilla di conducenti che potrà coprire la soluzione di L1 prima di entrare in adesione, regole e disponibilità.**

Per creare o importare la plantilla di conducenti:
1. In GoalBus, vai al modulo di **Configurazione** > **Personale** > **Gestione di conducenti**.
ref: P20_Imagen1.png | compact
2. Revisa se i conducenti del caso già esistono nella lista generale.
3. Se hai bisogno di creare pochi conducenti, clicca su **Nuovo Conducente**.
ref: P20_Imagen2.png | compact(2x)
4. Se hai bisogno di caricare molti conducenti, realizza un'importazione di massa mediante file CSV da **Carga Personale**.
ref: P20_Imagen3.png | compact
5. Se scegli l'importazione di massa, prepara il file con i dati minimi che la tua operazione necessita per identificare correttamente ogni persona. La finestra di importazione agirà da aiuto per preparare il file CSV di carica.
ref: P20_Imagen4.png
6. Esegui la carica e revisiona il risultato.
7. Ritorna alla lista generale e controlla che i conducenti appaiano correttamente.
8. Se noti duplicati o registri incompleti, correggili prima di proseguire.

## Verificare il caso di riferimento

Per concludere questa sezione, assicurati di aver raggiunto i seguenti obiettivi:
1. I conducenti di L1 sono già stati registrati o importati.
2. La lista generale riflette una sola plantilla di riferimento.
3. Puoi già aprire il profilo di ogni conducente per esaminare il suo contesto operativo.

Una volta conclusa questa sezione, dovresti avere una plantilla di conducenti caricata e visibile nel sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Esaminando il profilo del conducente e i suoi dati strutturali

Una volta creata la plantilla, è necessario esaminare il **profilo del conducente**. Il profilo non è solo una scheda di contatto: è il fascicolo digitale completo dell'impiegato all'interno dell'operazione. Lì convivono dati statici, contesto operativo e attributi che il sistema utilizzerà in seguito per ragionare sulla sua eleggibilità. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Prima di iniziare questa sezione, assicurati di:
1. Avere già i conducenti visibili nella lista generale.
2. Sapere già quale conducente o quale gruppo utilizzare come esempio.
3. Voler verificare che il registro non sia solo amministrativo, ma operativo.

Per esaminare il profilo del conducente:
1. Nella lista generale, clicca sul nome di un conducente.
ref: P20_Imagen5.png | full
2. Esamina la barra laterale dei dati statici.
3. Verifica almeno questi gruppi di informazione:
   1. dati di base, come nome e codice,
   2. dati operativi, come convenzione collettiva o tipo di contratto,
   3. collegamenti operativi, come deposito principale, gruppo di lavoro, area o tipi di veicoli autorizzati.
4. Se manca un dato strutturale chiave, completalo prima di proseguire.
5. Salva qualsiasi cambiamento necessario.
6. Ripeti la revisione su diversi conducenti per confermare la consistenza nella plantilla.

Per il caso di riferimento, controlla almeno:
1. Il codice del conducente.
2. Il suo deposito principale.
3. Il suo gruppo di lavoro.
4. Le proprietà operative che condizioneranno la sua assegnazione successiva.

Quando terminerai questa sezione, dovresti avere chiaro che ogni conducente ha un expediente operativo coherente e utilizzabile. fileciteturn38file0L8-L20

## Verificando il contesto operativo e i dati dinamici del conducente

Inoltre ai dati strutturali, il profilo del conducente include dati dinamici che influiscono direttamente su come il sistema ragiona sulla persona. Nella scheda di amministrazione puoi verificare i contatori e i modelli di lavoro, che fanno parte del contesto operativo utilizzato in seguito dalla logica di assegnazione. fileciteturn38file0L12-L17

Prima di iniziare questa sezione, assicurati di aver:
1. Già verificato i dati statici del profilo.
2. Già saputo se la tua operazione utilizza contatori o modelli cíclici.
3. Volete verificare che il conducente non esista solo, ma abbia un contesto operativo interpretabile.

Per verificare il contesto operativo dinamico:
1. Dentro il profilo del conducente, apri la scheda di **Dettagli di amministrazione**.
2. Verifica i **contatori** o KPI associati al conducente se esistono.
3. Controlla se il conducente è collegato a un **modello di lavoro**.
4. Se la tua operazione utilizza modelli cíclici, verifica anche il disfaso o la posizione attuale del conducente all'interno del modello.
5. Conferma che questi dati hanno senso per il contesto reale.
6. Se l'informazione dinamica non è corretta, aggiustala prima di passare alle regole o al calcolo.

# Verificare le abilitazioni prima di utilizzare il conducente nel Rostering

Prima di considerare un conducente come elegibile, è necessario verificare le sue **abilitazioni**. Queste abilitazioni rispondono alla domanda “può questa persona lavorare legalmente o tecnicamente in questo deposito, gruppo o unità?”. Vengono gestite in una linea temporale con data di inizio e fine, e il sistema mostra stati come attivo, futuro, scaduto o prossimo a scadere per facilitare la lettura. Se una persona non è abilitata per il contesto richiesto, il motore genera un errore al tentare di assegnarla. fileciteturn38file0L17-L34

Prima di iniziare questa sezione, assicurati di aver:
1. già verificato il profilo del conducente.
2. già saputo quale deposito, gruppo o unità sarà necessario per il tuo caso.
3. capisci che un'abilitazione non è lo stesso che una cessione o un'adesione temporanea.

Per verificare e validare le abilitazioni:
1. Dentro del profilo del conducente, apri la scheda **Abilitazioni / Qualificazioni**.
2. Verifica se esistono registri vigenti per:
   1. depositi,
   2. gruppi di lavoro,
   3. unità di business.
3. Controlla lo stato visivo di ogni abilitazione:
   1. attiva,
   2. futura,
   3. prossima a scadere,
   4. scaduta.
4. Se manca un'abilitazione necessaria, aggiungila con le date corrette.
5. Se un'abilitazione è scaduta e non dovrebbe essere utilizzata, lasciala come storico senza tentare di riscriverre il passato.
6. Salva i cambiamenti.
7. Conferma che il conducente è ora abilitato per il contesto dove lo utilizzerai.

Para il caso di riferimento, non procedere fino a quando non potrai affermare:
1. Il conducente è abilitato per il deposito corretto.
2. Il gruppo di lavoro richiesto è coperto.
3. Non ci sono scadenze che rompano l'attuale eleggibilità.

Quando terminerai questa sezione, dovresti avere conducenti che non solo esistono nella tabella, ma che sono anche eleggibili dal punto di vista operativo e normativo.

## Confermando che la tabella già è pronta per la prossima capa di Rostering

L'ultimo passo è verificare che la base di conducenti già è pronta per entrare nella prossima capa: adesione operativa, regole, assenze e calcolo. Qui l'obiettivo non è solo avere nomi caricati, ma una tabella coerente, tracciabile e utilizzabile dal motore.

Prima di terminare, assicurati di aver:
1. Caricato o importato la tabella.
2. Revisionato i profili principali.
3. Verificato i dati strutturali e dinamici.
4. Validato le abilitazioni essenziali.

Per confermare che la tabella già è pronta:
1. Torna alla lista generale di conducenti.
2. Verifica che il team necessario per il tuo caso è presente.
3. Controlla che i profili critici non hanno vuoti di informazioni importanti.
4. Assicurati che le persone che intendi utilizzare siano abilitate per il contesto corretto.
5. Preghiatiti se il sistema già potrebbe utilizzare questa base come punto di partenza per:
   1. adesione operativa,
   2. regole di Rostering,
   3. e disponibilità reale.
6. Se la risposta è sì, procedi con il prossimo quick start.
7. Se la risposta è no, correggi la base di conducenti prima di proseguire.

Per il caso di riferimento, termina questa quick start solo quando potrai affermare:
1. La plantilla dei conducenti di L1 è già caricata.
2. I profili chiave sono già stati revisionati.
3. Le abilitazioni essenziali sono già attive.
4. La base è già pronta per passare all'adscrizione operativa.

Quando terminerai questa sezione, dovresti avere una plantilla dei conducenti sufficientemente solida per continuare con la prossima capa di Rostering.

## Letture aggiuntive

- [Gestendo l'adscrizione operativa del conducente](P21_Gestendo_l'adscripcion_operativa_del_conducente.md)