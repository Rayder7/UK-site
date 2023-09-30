from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, New

from . import crud


async def news_by_id(
    news_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> New:
    news = await crud.get_one_news(session=session, news_id=news_id)
    if news is not None:
        return news

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"News {news_id} not found!",
    )
