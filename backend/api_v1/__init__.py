from fastapi import APIRouter

from .products.views import router as products_router
from .news.views import router as news_router
from .apartments.views import router as apartments_router
from .buildings.views import router as buildings_router

router = APIRouter()
router.include_router(router=products_router, prefix="/products")
router.include_router(router=news_router, prefix="/news")
router.include_router(router=apartments_router, prefix="/apartments")
router.include_router(router=buildings_router, prefix="/buildings")
