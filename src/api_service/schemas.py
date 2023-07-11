from pydantic import BaseModel


class FilmSchema(BaseModel):
    film_id: str
    film_name: str
    film_rating: float


class ReviewSchema(BaseModel):
    review_id: str
    review_text: str
    film_id: str
    review_score: int
