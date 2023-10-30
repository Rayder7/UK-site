from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import building_by_id
from .schemas import (
    Building,
    BuildingCreate,
    BuildingUpdate,
    BuildingUpdatePartial,
)

router = APIRouter(tags=["Buildings"])


@router.get("/", response_model=list[Building])
async def get_buildings(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_buildings(session=session)


@router.post(
    "/",
    response_model=Building,
    status_code=status.HTTP_201_CREATED,
)
async def create_building(
    building_in: BuildingCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_building(session=session, building_in=building_in)


@router.get("/{building_id}/", response_model=Building)
async def get_building(
    building: Building = Depends(building_by_id),
):
    return building


@router.put("/{building_id}/")
async def update_building(
    building_update: BuildingUpdate,
    building: Building = Depends(building_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_building(
        session=session,
        building=building,
        building_update=building_update,
    )


@router.patch("/{building_id}/")
async def update_building_partial(
    building_update: BuildingUpdatePartial,
    building: Building = Depends(building_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_building(
        session=session,
        building=building,
        building_update=building_update,
        partial=True,
    )


@router.delete("/{building_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_building(
    building: Building = Depends(building_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_building(session=session, building=building)
