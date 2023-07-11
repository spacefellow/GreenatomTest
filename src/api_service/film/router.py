from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, func
from database import get_async_session
from api_service.models import FilmModel, ReviewModel
from api_service.schemas import FilmSchema

router = APIRouter()


@router.get('/films')
async def get_all_films(session: AsyncSession = Depends(get_async_session)):
    query = select(FilmModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/film/{id}')
async def get_one_film(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(FilmModel).filter_by(id=id))
    return result.scalars().all()


@router.post('/film/add')
async def create_film(new_film: FilmSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        insert(FilmModel).
        values(name=new_film.film_name)
    )
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            'instance': new_film.dict(),
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


@router.patch('/film/{id}/get_rating')
async def get_rating(id: str, session: AsyncSession = Depends(get_async_session)):
    try:
        pos_reviews_request = await session.execute(select(func.count(ReviewModel.id)).filter(ReviewModel.film_id == id)
                                                    .where(ReviewModel.score == 1))
        all_reviews_request = await session.execute(select(func.count(ReviewModel.id)).
                                                    filter(ReviewModel.film_id == id))
        pos_reviews_value = pos_reviews_request.scalars().all()[0]
        all_reviews_value = all_reviews_request.scalars().all()[0]
        if all_reviews_value == 0:
            rating = 0
        else:
            rating = round(pos_reviews_value / all_reviews_value * 10, 2)
        stmt = update(FilmModel).values(
            rating=rating
        ).filter_by(id=id)
        await session.execute(stmt)
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': e
        })
