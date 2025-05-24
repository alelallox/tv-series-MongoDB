from pymongo import MongoClient
from prettytable import PrettyTable

def connect_to_database():
    """Si connette a MongoDB Atlas e restituisce il database e il client."""
    MONGO_URI = "mongodb+srv://NuovoUtenteProva:passwordProva@cluster0.ah74a.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGO_URI)
    db = client["serieTV"]  
    return db, client 

def add_serie(db, titolo, voto):
    """Aggiunge un documento alla collezione serieTV."""
    collection = db["serieTV"]  
    
    def get_next_id(collection):
        """Trova l'ID più alto nella collezione e lo incrementa di 1."""
        last_doc = collection.find_one(sort=[("id", -1)])  
        return (last_doc["id"] + 1) if last_doc else 1  
   
    id_serie = get_next_id(collection)

    serie = {
        "titolo": titolo,
        "voto": voto,
        "id": id_serie
    }

    result = collection.insert_one(serie)
    return result.inserted_id

db, client = connect_to_database() 
print("Connessione aperta con MongoDB ✅")

while True:
    key = input("Inserisci una serie tv o digita un comando: ")
    
    if key == "print":
        series = db["serieTV"].find().sort("voto", -1)

        table = PrettyTable()
        table.field_names = ["ID", "Titolo", "Voto"]

        for serie in series:
            table.add_row([serie["id"], serie["titolo"], serie["voto"]])

        print(table)
    
    elif key == "pop":
        titolo_da_eliminare = input("Inserisci titolo o id della serie TV da eliminare:")
        if titolo_da_eliminare.isdigit():
            result = db["serieTV"].delete_one({"id": int(titolo_da_eliminare)})
            print(f"Serie con ID {titolo_da_eliminare} eliminata.") if result.deleted_count > 0 else print("Nessuna serie trovata con questo ID.")
        else:
            result = db["serieTV"].delete_one({"titolo": titolo_da_eliminare})
            if result.deleted_count > 0:
                print(f"La serie '{titolo_da_eliminare}' è stata eliminata con successo! ✅")
            else:
                print(f"Nessuna serie trovata con il titolo '{titolo_da_eliminare}'. ❌")

    elif key == "pop tot":
        result = db["serieTV"].delete_many({})
        print(f"Eliminate {result.deleted_count} serie dalla collezione.")
    
    elif key == "end":
        client.close()  
        print("Connessione chiusa con MongoDB ✅")
        break

    else:
        try:
            voto = float(input("Voto: "))  
            add_serie(db, key, voto)
            print(f"Serie '{key}' aggiunta con voto {voto} ✅")
        except ValueError:
            print("Errore: il voto deve essere un numero valido.")