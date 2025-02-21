from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.config import ModelBase

class Product(ModelBase):
    __tablename__ = "products"

    id : Mapped[str] = mapped_column(String, primary_key=True, index=True)
    request_id : Mapped[str]= mapped_column(String, ForeignKey("image_processing_requests.request_id"))
    name : Mapped[str] = mapped_column(String, nullable=False)

    processing_request : Mapped["ImageProcessingRequest"] = relationship("ImageProcessingRequest", back_populates="products")
    images = relationship("Image", back_populates="product")
