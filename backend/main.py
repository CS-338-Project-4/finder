from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router


app = FastAPI()
app.include_router(router)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)
