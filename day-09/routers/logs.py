from fastapi import APIRouter,HTTPException
from services import logs_service

router=APIRouter()

@router.get("/logs")

def get_logs():
    result= logs_service.analyze_log()

    if result is None:
        raise HTTPException(
            status_code=404, 
            detail="Log file 'app.log' not found in the project root."
        )
        
    return result