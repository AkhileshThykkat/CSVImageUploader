import aiohttp
from celery import Celery
from sqlalchemy.ext.asyncio import AsyncSession

from .env_loader import settings
from app.models import Image

celery = Celery(__name__, broker=settings.REDIS_URL)
MAX_RETRIES = 3


@celery.task(bind=True, max_retries=MAX_RETRIES)
async def process_image(self, image_id: str, session: AsyncSession):
    async with session.begin():
        image = await session.get(Image, image_id)
        if not image:
            return

        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(image.input_url) as response:
                    if response.status == 200:
                        # Simulate image compression (50% quality reduction)
                        compressed_image_url = await upload_compressed_image(response.content)
                        image.output_url = compressed_image_url
                        await session.commit()
                    else:
                        raise Exception("Failed to download image")
        
        except Exception as e:
            image.retry_count += 1
            if image.retry_count >= MAX_RETRIES:
                print(f"Image {image_id} failed after max retries.")
            else:
                print(f"Retrying image {image_id}, attempt {image.retry_count}")
                self.retry(countdown=5)  # Retry after 5 seconds
            
            await session.commit()
