# tv-series-MongoDB
AGGIORNAMENTO DEL VECCHIO PROGRAMMA DI MEMORIZZAZIONE DELLE SERIE TV. Ora salviamo le serie tv su un database con MongoDB invece che salvare un dizionario (serie tv - voto) su disco utilizzando il modulo Pickle.

## Caratteristiche
* **Aggiunta Rapida**: Inserisci il nome di una serie e assegna un voto numerico.
* **ID Auto-incrementanti**: Gestione automatica e sequenziale degli ID per ogni documento.
* **Visualizzazione Ordinata**: Stampa una tabella formattata delle serie TV, ordinate dal voto più alto al più basso.
* **Rimozione Flessibile**: Elimina una serie specifica tramite il suo titolo o il suo ID, oppure svuota l'intero database.

## Configurazione

1. Accedi al tuo account **MongoDB Atlas**.
2. Vai nella sezione **Connect** del tuo Cluster e copia la stringa di connessione (`MONGO_URI`).
3. Apri lo script Python e sostituisci i placeholder nella funzione `connect_to_database()` con le tue credenziali reali:

```python
MONGO_URI = "mongodb+srv://<db_username>:<db_password>@<db_cluster_name>/?retryWrites=true&w=majority"
```

### Comandi Disponibili

* **`print`**: Mostra la tabella di tutte le serie TV salvate, ordinate per voto decrescente.
* **`pop`**: Rimuove una serie TV. Il sistema ti chiederà se vuoi inserire il **Titolo** o l'**ID** della serie da cancellare.
* **`pop tot`**: Elimina istantaneamente **tutti** i record presenti nella collezione.
* **`end`**: Chiude in modo sicuro la connessione con MongoDB Atlas ed esce dal programma.
* **Qualsiasi altro testo**: Viene interpretato come il titolo di una nuova serie TV da aggiungere (ti verrà richiesto subito dopo il voto).
