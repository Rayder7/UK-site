from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, House

from . import crud


async def house_by_id(
    house_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> House:
    house = await crud.get_house(session=session, house_id=house_id)
    if house is not None:
        return house

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"house {house_id} not found!",
    )
