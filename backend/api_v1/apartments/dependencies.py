""" from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Apartment

from . import crud


async def apartment_by_id(
    apartment_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Apartment:
    apartment = await crud.get_apartment(
        session=session, apartment_id=apartment_id
    )
    if apartment is not None:
        return apartment

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"apartment {apartment_id} not found!",
    )
 """
