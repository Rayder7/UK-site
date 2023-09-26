from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items")


@router.get("/{item_id}/")  # больше 0, меньше 1 млн
def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": item_id,
    }


@router.get("/")
def list_items():
    return ["item1", "item2"]
