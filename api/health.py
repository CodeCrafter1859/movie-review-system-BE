from fastapi import APIRouter

router = APIRouter()

@router.get('/health')
async def health_api():
    return {
        'success': True,
        'message' : "working project"
    }