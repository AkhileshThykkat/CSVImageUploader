from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import ImageProcessingRequest, ProcessingStatus

class ImageProcessingRequestRepository:
    @staticmethod
    async def get_request_by_id(request_id: str, session: AsyncSession) -> ImageProcessingRequest | None:
        """Fetch an image processing request by its ID."""
        return await session.get(ImageProcessingRequest, request_id)

    @staticmethod
    async def create_request(request_data: dict, session: AsyncSession) -> ImageProcessingRequest:
        """Create a new image processing request."""
        request = ImageProcessingRequest(**request_data)
        session.add(request)
        await session.commit()
        await session.refresh(request)
        return request

    @staticmethod
    async def update_request(request_id: str, update_data: dict, session: AsyncSession) -> ImageProcessingRequest | None:
        """Update an existing image processing request."""
        request = await ImageProcessingRequestRepository.get_request_by_id(request_id, session)
        if not request:
            return None

        for key, value in update_data.items():
            setattr(request, key, value)

        await session.commit()
        await session.refresh(request)
        return request

    @staticmethod
    async def delete_request(request_id: str, session: AsyncSession) -> bool:
        """Delete an image processing request."""
        request = await ImageProcessingRequestRepository.get_request_by_id(request_id, session)
        if not request:
            return False

        await session.delete(request)
        await session.commit()
        return True

    @staticmethod
    async def get_all_requests(session: AsyncSession):
        """Retrieve all image processing requests."""
        result = await session.execute(select(ImageProcessingRequest))
        return result.scalars().all()

    @staticmethod
    async def update_request_status(request_id: str, status: ProcessingStatus, session: AsyncSession) -> bool:
        """Update the processing status of an image processing request."""
        request = await ImageProcessingRequestRepository.get_request_by_id(request_id, session)
        if not request:
            return False

        request.status = status
        await session.commit()
        await session.refresh(request)
        return True
