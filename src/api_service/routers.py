from fastapi import APIRouter
from api_service.review.router import router as review_router
from api_service.film.router import router as film_router


aggregated_router = APIRouter()

routers = (
    review_router,
    film_router,
)

for router in routers:
    aggregated_router.include_router(
        router,
    )
