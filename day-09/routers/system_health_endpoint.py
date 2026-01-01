from fastapi import APIRouter,HTTPException
from services.system_health_logic import system_health

router=APIRouter()

@router.get("/metrics",status_code=200)
def get_system_health():
    try:
        metrics=system_health()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )