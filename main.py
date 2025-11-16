from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Дозволяємо CORS (щоб до сервісу можна було звертатись з браузера/інших доменів)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


@app.api_route("/", methods=["GET", "POST", "OPTIONS"])
async def http_entry(request: Request):
    # Обробка preflight-запитів
    if request.method == "OPTIONS":
        return Response(status_code=204)

    # Значення за замовчуванням
    name = "world"

    # 1) GET /?name=...
    if "name" in request.query_params:
        name = request.query_params["name"]

    # 2) POST JSON: {"name": "Nastia"}
    elif request.method == "POST":
        try:
            body = await request.json()
        except Exception:
            body = {}

        if isinstance(body, dict) and "name" in body:
            name = body["name"]

    # Точний формат відповіді:
    return {"hello": name}
