from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import ApartmentCreate, ApartmentUpdate, ApartmentUpdatePartial
from core.models import Apartment


async def get_apartments(session: AsyncSession) -> list[Apartment]:
    stmt = select(Apartment).order_by(Apartment.id)
    result: Result = await session.execute(stmt)
    apartments = result.scalars().all()
    return list(apartments)


async def get_apartment(
    session: AsyncSession, apartment_id: int
) -> Apartment | None:
    return await session.get(Apartment, apartment_id)


async def create_apartment(
    session: AsyncSession, apartment_in: ApartmentCreate
) -> Apartment:
    apartment = Apartment(**apartment_in.model_dump())
    session.add(apartment)
    await session.commit()
    return apartment


async def update_apartment(
    session: AsyncSession,
    apartment: Apartment,
    apartment_update: ApartmentUpdate | ApartmentUpdatePartial,
    partial: bool = False,
) -> Apartment:
    for name, value in apartment_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(apartment, name, value)
    await session.commit()
    return apartment


async def delete_apartment(
    session: AsyncSession,
    apartment: Apartment,
) -> Apartment:
    await session.delete(apartment)
    await session.commit()
