from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pink Czech History")


@app.get("/", response_class=HTMLResponse)
async def home() -> str:
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Flashy Pink Czech History</title>
        <style>
          :root {
            --pink-1: #ff1fbf;
            --pink-2: #ff4fd8;
            --pink-3: #ff8eea;
            --bg-1: #120012;
            --bg-2: #2a0030;
          }

          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            background: radial-gradient(circle at 20% 20%, var(--pink-2), transparent 35%),
              radial-gradient(circle at 80% 30%, var(--pink-3), transparent 30%),
              linear-gradient(120deg, var(--bg-1), var(--bg-2));
            font-family: "Trebuchet MS", "Segoe UI", sans-serif;
            color: white;
            overflow: hidden;
          }

          .card {
            max-width: 900px;
            margin: 24px;
            padding: 28px;
            border-radius: 20px;
            border: 2px solid var(--pink-3);
            background: rgba(255, 31, 191, 0.14);
            box-shadow: 0 0 24px rgba(255, 79, 216, 0.95), 0 0 64px rgba(255, 31, 191, 0.5);
            backdrop-filter: blur(6px);
            animation: pulse 1.2s infinite alternate;
          }

          h1 {
            margin: 0 0 14px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #ffd3f8;
            text-shadow: 0 0 12px var(--pink-2), 0 0 24px var(--pink-1);
          }

          p {
            margin: 0;
            font-size: 1.08rem;
            line-height: 1.7;
          }

          @keyframes pulse {
            from {
              transform: scale(1);
              box-shadow: 0 0 18px rgba(255, 79, 216, 0.8), 0 0 48px rgba(255, 31, 191, 0.45);
            }
            to {
              transform: scale(1.02);
              box-shadow: 0 0 30px rgba(255, 79, 216, 1), 0 0 72px rgba(255, 31, 191, 0.7);
            }
          }
        </style>
      </head>
      <body>
        <article class="card">
          <h1>History of the Czech Republic</h1>
          <p>
            The history of the Czech Republic stretches from the early Slavic settlements and the powerful medieval Kingdom of Bohemia, through the cultural and political influence of the Holy Roman Empire and Habsburg rule, to the modern era shaped by the creation of Czechoslovakia in 1918 after World War I, the trauma of Nazi occupation during World War II, decades of communist government after 1948, the peaceful Velvet Revolution of 1989 that restored democracy, and the amicable split of Czechoslovakia in 1993 that established today’s Czech Republic as an independent state that later joined NATO and the European Union.
          </p>
        </article>
      </body>
    </html>
    """
