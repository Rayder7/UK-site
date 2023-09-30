from datetime import datetime
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import NewsCreate, NewsUpdate, NewsUpdatePartial
from core.models import New as News


async def get_news(session: AsyncSession) -> list[News]:
    stmt = select(News).order_by(News.created_date)
    result: Result = await session.execute(stmt)
    news = result.scalars().all()
    return list(news)


async def get_one_news(session: AsyncSession, news_id: int) -> News | None:
    return await session.get(News, news_id)


async def create_news(session: AsyncSession, news_in: NewsCreate) -> News:
    news = News(**news_in.model_dump())
    news.created_date = str(datetime.now())
    news.user_id = 1
    session.add(news)
    await session.commit()
    return news


async def update_news(
    session: AsyncSession,
    news: News,
    news_update: NewsUpdate | NewsUpdatePartial,
    partial: bool = False,
) -> News:
    for name, value in news_update.model_dump(exclude_unset=partial).items():
        setattr(news, name, value)
    await session.commit()
    return news


async def delete_news(
    session: AsyncSession,
    news: News,
) -> News:
    await session.delete(news)
    await session.commit()
