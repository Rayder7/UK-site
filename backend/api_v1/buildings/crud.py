from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import BuildingCreate, BuildingUpdate, BuildingUpdatePartial
from core.models import Building


async def get_buildings(session: AsyncSession) -> list[Building]:
    stmt = select(Building).order_by(Building.id)
    result: Result = await session.execute(stmt)
    buildings = result.scalars().all()
    return list(buildings)


async def get_building(
    session: AsyncSession, building_id: int
) -> Building | None:
    return await session.get(Building, building_id)


async def create_building(
    session: AsyncSession, building_in: BuildingCreate
) -> Building:
    building = Building(**building_in.model_dump())
    building.apartments = []
    session.add(building)
    await session.commit()
    return building


async def update_building(
    session: AsyncSession,
    building: Building,
    building_update: BuildingUpdate | BuildingUpdatePartial,
    partial: bool = False,
) -> Building:
    for name, value in building_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(building, name, value)
    await session.commit()
    return building


async def delete_building(
    session: AsyncSession,
    building: Building,
) -> Building:
    await session.delete(building)
    await session.commit()
