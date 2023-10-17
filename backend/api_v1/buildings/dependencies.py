from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Building

from . import crud


async def building_by_id(
    building_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Building:
    building = await crud.get_building(session=session, building_id=building_id)
    if building is not None:
        return building

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Building {building_id} not found!",
    )
