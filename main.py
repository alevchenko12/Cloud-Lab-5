from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import os

# Створюємо FastAPI-застосунок
app = FastAPI()

# Додаємо CORS, щоб до сервісу можна було звертатися з будь-якого фронтенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # дозволити всі домени
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

# Один вхідний HTTP-ендпоінт "/" на всі методи
@app.api_route("/", methods=["GET", "POST", "OPTIONS"])
async def http_entry(request: Request):
    # Обробка preflight-запитів від браузера (CORS)
    if request.method == "OPTIONS":
        return Response(status_code=204)

    # -------- Витягуємо параметр "name" з GET або POST --------
    name = "world"

    # 1) Якщо прийшов GET-запит з query-параметром ?name=...
    if request.query_params.get("name"):
        name = request.query_params["name"]
    else:
        # 2) Якщо POST — пробуємо прочитати JSON-тіло
        if request.method == "POST":
            try:
                body = await request.json()
            except Exception:
                body = {}

            # Якщо тіло — dict і є ключ "name"
            if isinstance(body, dict) and body.get("name"):
                name = body["name"]

    # -------- Тут має бути твоя логіка з Лаби 4 --------
    # Приклад:
    # result = your_lab4_function(name)
    #
    # Поки що для прикладу зробимо просту відповідь:

    result = {
        "hello": name,
        "runtime": "python",
        "my_test_env": os.getenv("TEST_ENV", "unknown"),
    }

    return result
