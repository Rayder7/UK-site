from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import house_by_id
from .schemas import (
    House,
    HouseCreate,
    HouseUpdate,
    HouseUpdatePartial,
)

router = APIRouter(tags=["Houses"])


@router.get("/", response_model=list[House])
async def get_houses(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_houses(session=session)


@router.post(
    "/",
    response_model=House,
    status_code=status.HTTP_201_CREATED,
)
async def create_house(
    house_in: HouseCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_house(session=session, house_in=house_in)


@router.get("/{house_id}/", response_model=House)
async def get_house(
    house: House = Depends(house_by_id),
):
    return house


@router.put("/{house_id}/")
async def update_house(
    house_update: HouseUpdate,
    house: House = Depends(house_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_house(
        session=session,
        house=house,
        houseupdate=house_update,
    )


@router.patch("/{house_id}/")
async def update_house_partial(
    house_update: HouseUpdatePartial,
    house: House = Depends(house_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_house(
        session=session,
        house=house,
        house_update=house_update,
        partial=True,
    )


@router.delete("/{house_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_house(
    house: House = Depends(house_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_house(session=session, house=house)
