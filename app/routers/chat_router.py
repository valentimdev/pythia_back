from fastapi import APIRouter, HTTPException
from app.schemas.chat_schemas import ChatRequest, ChatResponse
from app.services import chat_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def handle_chat_request(request_data: ChatRequest):
    try:
        response_data = chat_service.process_chat_interaction(
            thread_id=request_data.thread_id,
            user_message=request_data.message
        )
        return ChatResponse(**response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {str(e)}")