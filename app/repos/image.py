from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Image, ProcessingStatus

class ImageRepository:
    @staticmethod
    async def get_image_by_id(image_id: str, session: AsyncSession) -> Image | None:
        """Fetch an image by its ID."""
        return await session.get(Image, image_id)

    @staticmethod
    async def create_image(image_data: dict, session: AsyncSession) -> Image:
        """Create a new image entry in the database."""
        image = Image(**image_data)
        session.add(image)
        await session.commit()
        await session.refresh(image)
        return image

    @staticmethod
    async def update_image(image_id: str, update_data: dict, session: AsyncSession) -> Image | None:
        """Update an existing image record."""
        image = await ImageRepository.get_image_by_id(image_id, session)
        if not image:
            return None

        for key, value in update_data.items():
            setattr(image, key, value)

        await session.commit()
        await session.refresh(image)
        return image

    @staticmethod
    async def delete_image(image_id: str, session: AsyncSession) -> bool:
        """Delete an image from the database."""
        image = await ImageRepository.get_image_by_id(image_id, session)
        if not image:
            return False

        await session.delete(image)
        await session.commit()
        return True

    @staticmethod
    async def get_images_by_product_id(product_id: str, session: AsyncSession):
        """Retrieve all images associated with a specific product."""
        result = await session.execute(select(Image).where(Image.product_id == product_id))
        return result.scalars().all()

    @staticmethod
    async def update_image_status(image_id: str, status: ProcessingStatus, session: AsyncSession) -> bool:
        """Update the processing status of an image."""
        image = await ImageRepository.get_image_by_id(image_id, session)
        if not image:
            return False

        image.status = status
        await session.commit()
        await session.refresh(image)
        return True
