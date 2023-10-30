""" from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import apartment_by_id
from .schemas import (
    Apartment,
    ApartmentCreate,
    ApartmentUpdate,
    ApartmentUpdatePartial,
)

router = APIRouter(tags=["Apartments"])


@router.get("/", response_model=list[Apartment])
async def get_apartments(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_apartments(session=session)


@router.post(
    "/",
    response_model=Apartment,
    status_code=status.HTTP_201_CREATED,
)
async def create_apartment(
    apartment_in: ApartmentCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_apartment(
        session=session, apartment_in=apartment_in
    )


@router.get("/{apartment_id}/", response_model=Apartment)
async def get_one_news(
    apartment: Apartment = Depends(apartment_by_id),
):
    return apartment


@router.put("/{apartment_id}/")
async def update_apartment(
    apartment_update: ApartmentUpdate,
    apartment: Apartment = Depends(apartment_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_apartment(
        session=session,
        apartment=apartment,
        apartmentupdate=apartment_update,
    )


@router.patch("/{apartment_id}/")
async def update_apartment_partial(
    apartment_update: ApartmentUpdatePartial,
    apartment: Apartment = Depends(apartment_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_apartment(
        session=session,
        apartment=apartment,
        apartment_update=apartment_update,
        partial=True,
    )


@router.delete("/{apartment_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_apartment(
    apartment: Apartment = Depends(apartment_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_apartment(session=session, apartment=apartment)
 """
