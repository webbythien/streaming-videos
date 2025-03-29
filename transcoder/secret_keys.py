from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class SecretKeys(BaseSettings):
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    REGION_NAME: str = ""
    POSTGRES_DB_URL: str = ""
    AWS_SQS_VIDEO_PROCESSING: str =""
    S3_BUCKET : str = ""
    S3_KEY:str = ""
    S3_PROCESSED_VIDEOS_BUCKET: str = ""
    BACKEND_URL: str = ""