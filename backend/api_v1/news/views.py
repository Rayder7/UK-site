from datetime import datetime
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import news_by_id
from .schemas import (
    News,
    NewsCreate,
    NewsUpdate,
    NewsUpdatePartial,
)

router = APIRouter(tags=["News"])


@router.get("/", response_model=list[News])
async def get_news(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_news(session=session)


@router.post(
    "/",
    response_model=News,
    status_code=status.HTTP_201_CREATED,
)
async def create_news(
    news_in: NewsCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_news(session=session, news_in=news_in)


@router.get("/{news_id}/", response_model=News)
async def get_one_news(
    news: News = Depends(news_by_id),
):
    return news


@router.put("/{news_id}/")
async def update_news(
    news_update: NewsUpdate,
    news: News = Depends(news_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_news(
        session=session,
        news=news,
        news_update=news_update,
    )


@router.patch("/{news_id}/")
async def update_product_partial(
    news_update: NewsUpdatePartial,
    news: News = Depends(news_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_news(
        session=session,
        news=news,
        news_update=news_update,
        partial=True,
    )


@router.delete("/{news_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(
    news: News = Depends(news_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_news(session=session, news=news)
