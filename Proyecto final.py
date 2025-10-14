from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Guardará el historial de operaciones en memoria
historial = []

# Página principal
@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html>
    <head>
        <title>Calculadora FastAPI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #4c6ef5, #b197fc);
                color: white;
                text-align: center;
                height: 100vh;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 2rem;
                width: 90%;
                max-width: 400px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            }
            input {
                width: 80%;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 1.2em;
                text-align: center;
            }
            button {
                margin-top: 10px;
                padding: 10px 20px;
                background: #51cf66;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                color: white;
                cursor: pointer;
                transition: 0.2s;
            }
            button:hover {
                background: #37b24d;
            }
            .resultado {
                margin-top: 1rem;
                font-size: 1.2em;
            }
            .historial {
                margin-top: 1.5rem;
                text-align: left;
            }
            .historial ul {
                list-style: none;
                padding: 0;
            }
            .historial li {
                background: rgba(255,255,255,0.2);
                border-radius: 8px;
                padding: 6px 10px;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 Calculadora FastAPI</h1>
            <form method="post" action="/calcular">
                <input type="text" name="expresion" placeholder="Ej: 3+5*2" required autofocus>
                <button type="submit">Calcular</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


# Procesar los cálculos
@app.post("/calcular", response_class=HTMLResponse)
def calcular(expresion: str = Form(...)):
    try:
        resultado = eval(expresion)
        historial.append(f"{expresion} = {resultado}")
    except Exception:
        resultado = "Error"
        historial.append(f"{expresion} = Error")

    # HTML con historial incluido
    html = f"""
    <html>
    <head>
        <title>Calculadora FastAPI</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #4c6ef5, #b197fc);
                color: white;
                text-align: center;
                height: 100vh;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 2rem;
                width: 90%;
                max-width: 400px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            }}
            input {{
                width: 80%;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 1.2em;
                text-align: center;
            }}
            button {{
                margin-top: 10px;
                padding: 10px 20px;
                background: #51cf66;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                color: white;
                cursor: pointer;
                transition: 0.2s;
            }}
            button:hover {{
                background: #37b24d;
            }}
            .resultado {{
                margin-top: 1rem;
                font-size: 1.2em;
            }}
            .historial {{
                margin-top: 1.5rem;
                text-align: left;
            }}
            .historial ul {{
                list-style: none;
                padding: 0;
            }}
            .historial li {{
                background: rgba(255,255,255,0.2);
                border-radius: 8px;
                padding: 6px 10px;
                margin-top: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 Calculadora FastAPI</h1>
            <form method="post" action="/calcular">
                <input type="text" name="expresion" placeholder="Ej: 3+5*2" required autofocus>
                <button type="submit">Calcular</button>
            </form>
            <div class="resultado">
                <h2>Resultado: {resultado}</h2>
            </div>
            <div class="historial">
                <h3>Historial:</h3>
                <ul>
                    {''.join(f'<li>{item}</li>' for item in historial)}
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)
