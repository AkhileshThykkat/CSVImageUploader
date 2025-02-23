from sqlalchemy.ext.asyncio import AsyncSession
from app.repos  import ImageRepository

class ImageService:
    @staticmethod
    async def create_image(image_data: dict, session: AsyncSession):
        return await ImageRepository.create_image(image_data, session)

    @staticmethod
    async def get_image_by_id(image_id: str, session: AsyncSession):
        return await ImageRepository.get_image_by_id(image_id, session)

    @staticmethod
    async def delete_image(image_id: str, session: AsyncSession):
        return await ImageRepository.delete_image(image_id, session)

    @staticmethod
    async def get_all_images(session: AsyncSession):
        return await ImageRepository.get_all_images(session)
