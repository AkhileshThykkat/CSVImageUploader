import io
import aioboto3
from PIL import Image
import os
from app.config import env_settings  # Load env variables

# S3 Client Session
session = aioboto3.Session()

async def upload_compressed_image(image_bytes: bytes) -> str:
    """
    Compresses the image and uploads it to S3.

    :param image_bytes: Raw image data in bytes
    :return: S3 URL of the uploaded image
    """
    try:
        # Open image using Pillow
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if image has transparency (PNG)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Compress image (reduce quality by 50%)
        img_buffer = io.BytesIO()
        image.save(img_buffer, format="JPEG", quality=50)
        img_buffer.seek(0)

        # Generate unique S3 key
        image_key = f"processed_images/{os.urandom(16).hex()}.jpg"

        # Upload to S3
        async with session.client(
            "s3",
            region_name=env_settings.REGION,
            aws_access_key_id=env_settings.ACCESS_KEY,
            aws_secret_access_key=env_settings.SECRET_KEY,
        ) as s3_client:
            await s3_client.upload_fileobj(img_buffer, env_settings.BUCKET_NAME, image_key, ExtraArgs={"ContentType": "image/jpeg"})

        # Return full S3 URL
        return f"https://{env_settings.BUCKET_NAME}.s3.{env_settings.REGION}.amazonaws.com/{image_key}"
    
    except Exception as e:
        print(f"Error processing and uploading image: {e}")
        return None
