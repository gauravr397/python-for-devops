from fastapi import APIRouter
from services import aws_service

router = APIRouter()

@router.get("/aws")
def get_aws():
    """
    Fetches S3 Buckets and EC2 instances using the host's AWS credentials.
    """
    result = aws_service.get_aws_resource()
    return result
