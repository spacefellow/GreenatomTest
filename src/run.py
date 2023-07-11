from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from api_service.routers import aggregated_router as identity_routers


app = FastAPI(
    title='Greenatom test task',
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    identity_routers,
    prefix='/main',
    tags=['Identification'],
)
