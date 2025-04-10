# IFC Backend

Dit is de backend van het IFC-dashboard project. Deze server ontvangt IFC-bestanden, valideert ze en stuurt fouten terug.

## Installatie

1. Navigeer naar de backend-map:

```bash
cd backend
```

2. Installeer de vereiste packages:

```bash
pip install -r requirements.txt
```

3. Start de server:

```bash
python app.py
```

Server draait standaard op `http://localhost:5000`.

## Endpoints

- **POST** `/upload`: Upload een IFC-bestand voor validatie.