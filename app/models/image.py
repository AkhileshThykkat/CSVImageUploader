import enum
from sqlalchemy import  Integer, String, ForeignKey,Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.config import ModelBase

class ProcessingStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Image(ModelBase):
    __tablename__ = "images"

    id : Mapped[str] = mapped_column(String, primary_key=True, index=True)
    product_id : Mapped[str] = mapped_column(String, ForeignKey("products.id"))
    input_url : Mapped[str] = mapped_column(String, nullable=False)
    output_url : Mapped[str] = mapped_column(String, nullable=True)
    retry_count : Mapped[int] = mapped_column(Integer, default=0)
    status : Mapped[str] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING)

    product : Mapped["Product"] = relationship("Product", back_populates="images")
