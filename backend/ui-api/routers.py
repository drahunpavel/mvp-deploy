"""routers"""

from typing import Dict
from fastapi import APIRouter, Depends, Request

from shared.auth import get_current_user

router = APIRouter()

@router.get("/info", response_model=Dict)
async def get_info(
    request: Request,
    username: str = Depends(get_current_user)
) -> Dict:
    """endpoint get_info"""
    client_host = request.client.host
    user_agent = request.headers.get("user-agent")
    forwarded_for = request.headers.get("x-forwarded-for")

    return {
        "username": username,
        "client_ip": client_host,
        "user_agent": user_agent,
        "x_forwarded_for": forwarded_for
    }