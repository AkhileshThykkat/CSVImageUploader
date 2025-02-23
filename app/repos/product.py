from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Product

class ProductRepository:
    @staticmethod
    async def get_product_by_id(product_id: str, session: AsyncSession) -> Product | None:
        """Fetch a product by its ID."""
        return await session.get(Product, product_id)

    @staticmethod
    async def create_product(product_data: dict, session: AsyncSession) -> Product:
        """Create a new product in the database."""
        product = Product(**product_data)
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product

    @staticmethod
    async def update_product(product_id: str, update_data: dict, session: AsyncSession) -> Product | None:
        """Update an existing product."""
        product = await ProductRepository.get_product_by_id(product_id, session)
        if not product:
            return None

        for key, value in update_data.items():
            setattr(product, key, value)

        await session.commit()
        await session.refresh(product)
        return product

    @staticmethod
    async def delete_product(product_id: str, session: AsyncSession) -> bool:
        """Delete a product from the database."""
        product = await ProductRepository.get_product_by_id(product_id, session)
        if not product:
            return False

        await session.delete(product)
        await session.commit()
        return True

    @staticmethod
    async def get_all_products(session: AsyncSession):
        """Retrieve all products from the database."""
        result = await session.execute(select(Product))
        return result.scalars().all()
