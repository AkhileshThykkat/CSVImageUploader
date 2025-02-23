from sqlalchemy.ext.asyncio import AsyncSession
from app.repos import ImageProcessingRequestRepository
from app.models import ProcessingStatus

class ImageProcessingRequestService:
    @staticmethod
    async def create_request(request_data: dict, session: AsyncSession):
        """Create a new image processing request."""
        return await ImageProcessingRequestRepository.create_request(request_data, session)

    @staticmethod
    async def get_request_by_id(request_id: str, session: AsyncSession):
        """Fetch an image processing request by its ID."""
        return await ImageProcessingRequestRepository.get_request_by_id(request_id, session)

    @staticmethod
    async def update_request(request_id: str, update_data: dict, session: AsyncSession):
        """Update an existing image processing request."""
        return await ImageProcessingRequestRepository.update_request(request_id, update_data, session)

    @staticmethod
    async def delete_request(request_id: str, session: AsyncSession):
        """Delete an image processing request."""
        return await ImageProcessingRequestRepository.delete_request(request_id, session)

    @staticmethod
    async def get_all_requests(session: AsyncSession):
        """Retrieve all image processing requests."""
        return await ImageProcessingRequestRepository.get_all_requests(session)

    @staticmethod
    async def update_request_status(request_id: str, status: ProcessingStatus, session: AsyncSession):
        """Update the processing status of an image processing request."""
        return await ImageProcessingRequestRepository.update_request_status(request_id, status, session)
