from fastapi import FastAPI
from router.routers import transliteration

app = FastAPI()

app.include_router(transliteration)
