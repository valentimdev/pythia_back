from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat_router

app = FastAPI(
    title="Pythia RPG Oracle API",
    description="API para o chatbot Pythia, um assistente para mestres de RPG.",
    version="1.0.0"
)

origins = ["*"] # Em produção, restrinja para o endereço do seu front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router.router, prefix="/api")

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "A API de Pythia está online."}