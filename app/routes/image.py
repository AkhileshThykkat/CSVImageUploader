from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import get_db
from app.services.image_service import ImageService

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/")
async def create_image(image_data: dict, session: AsyncSession = Depends(get_db)):
    return await ImageService.create_image(image_data, session)

@router.get("/{image_id}")
async def get_image_by_id(image_id: str, session: AsyncSession = Depends(get_db)):
    image = await ImageService.get_image_by_id(image_id, session)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@router.get("/")
async def get_all_images(session: AsyncSession = Depends(get_db)):
    return await ImageService.get_all_images(session)

@router.delete("/{image_id}")
async def delete_image(image_id: str, session: AsyncSession = Depends(get_db)):
    success = await ImageService.delete_image(image_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}
