from sqlalchemy.ext.asyncio import AsyncSession
from app.repos import ProductRepository

class ProductService:
    @staticmethod
    async def create_product(product_data: dict, session: AsyncSession):
        return await ProductRepository.create_product(product_data, session)

    @staticmethod
    async def get_product_by_id(product_id: str, session: AsyncSession):
        return await ProductRepository.get_product_by_id(product_id, session)

    @staticmethod
    async def delete_product(product_id: str, session: AsyncSession):
        return await ProductRepository.delete_product(product_id, session)

    @staticmethod
    async def get_all_products(session: AsyncSession):
        return await ProductRepository.get_all_products(session)
