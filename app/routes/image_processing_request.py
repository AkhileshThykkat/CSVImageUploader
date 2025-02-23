from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import get_db
from app.services.image_processing_request_service import ImageProcessingRequestService
from app.models import ProcessingStatus

router = APIRouter(prefix="/image-processing-requests", tags=["Image Processing Requests"])

@router.post("/")
async def create_request(request_data: dict, session: AsyncSession = Depends(get_db)):
    request = await ImageProcessingRequestService.create_request(request_data, session)
    return request

@router.get("/{request_id}")
async def get_request_by_id(request_id: str, session: AsyncSession = Depends(get_db)):
    request = await ImageProcessingRequestService.get_request_by_id(request_id, session)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

@router.put("/{request_id}")
async def update_request(request_id: str, update_data: dict, session: AsyncSession = Depends(get_db)):
    updated_request = await ImageProcessingRequestService.update_request(request_id, update_data, session)
    if not updated_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return updated_request

@router.delete("/{request_id}")
async def delete_request(request_id: str, session: AsyncSession = Depends(get_db)):
    success = await ImageProcessingRequestService.delete_request(request_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="Request not found")
    return {"message": "Request deleted successfully"}

@router.get("/")
async def get_all_requests(session: AsyncSession = Depends(get_db)):
    return await ImageProcessingRequestService.get_all_requests(session)

@router.patch("/{request_id}/status")
async def update_request_status(request_id: str, status: ProcessingStatus, session: AsyncSession = Depends(get_db)):
    success = await ImageProcessingRequestService.update_request_status(request_id, status, session)
    if not success:
        raise HTTPException(status_code=404, detail="Request not found")
    return {"message": "Request status updated successfully"}
