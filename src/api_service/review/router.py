from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from database import get_async_session
from api_service.models import ReviewModel
from api_service.schemas import ReviewSchema
from ml_service.base_functions import add_score

router = APIRouter()


@router.get('/film/{id}/reviews')
async def get_all_reviews(id: str, session: AsyncSession = Depends(get_async_session)):
    query = select(ReviewModel).filter_by(film_id=id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post('/film/{id}/add_review')
async def create_review(new_review: ReviewSchema, id: str, session: AsyncSession = Depends(get_async_session)):
    score = await add_score([new_review.review_text])
    stmt = insert(ReviewModel).values(text=new_review.review_text, film_id=id, score=score)
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            'instance': new_review.dict(),
            'status': 'success',
            'data': None
        }
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': e
        })
