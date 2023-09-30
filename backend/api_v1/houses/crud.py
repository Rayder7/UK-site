from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import HouseCreate, HouseUpdate, HouseUpdatePartial
from core.models import House


async def get_houses(session: AsyncSession) -> list[House]:
    stmt = select(House).order_by(House.id)
    result: Result = await session.execute(stmt)
    houses = result.scalars().all()
    return list(houses)


async def get_house(session: AsyncSession, house_id: int) -> House | None:
    return await session.get(House, house_id)


async def create_house(session: AsyncSession, house_in: HouseCreate) -> House:
    house = House(**house_in.model_dump())
    house.apartments = []
    session.add(house)
    await session.commit()
    return house


async def update_house(
    session: AsyncSession,
    house: House,
    house_update: HouseUpdate | HouseUpdatePartial,
    partial: bool = False,
) -> House:
    for name, value in house_update.model_dump(exclude_unset=partial).items():
        setattr(house, name, value)
    await session.commit()
    return house


async def delete_house(
    session: AsyncSession,
    house: House,
) -> House:
    await session.delete(house)
    await session.commit()
