from typing import List
from sqlalchemy import  String, DateTime, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import enum
from app.config import ModelBase

class ProcessingStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class ImageProcessingRequest(ModelBase):
    __tablename__ = "image_processing_requests"

    request_id : Mapped[str] =  mapped_column(String, primary_key=True, index=True)
    created_at :Mapped[DateTime] =  mapped_column(DateTime, default=datetime.utcnow)
    updated_at : Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status : Mapped[str] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING)

    products : Mapped[List["Product"]] = relationship("Product", back_populates="processing_request")
