from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import get_db
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
async def create_product(product_data: dict, session: AsyncSession = Depends(get_db)):
    return await ProductService.create_product(product_data, session)

@router.get("/{product_id}")
async def get_product_by_id(product_id: str, session: AsyncSession = Depends(get_db)):
    product = await ProductService.get_product_by_id(product_id, session)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/")
async def get_all_products(session: AsyncSession = Depends(get_db)):
    return await ProductService.get_all_products(session)

@router.delete("/{product_id}")
async def delete_product(product_id: str, session: AsyncSession = Depends(get_db)):
    success = await ProductService.delete_product(product_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
