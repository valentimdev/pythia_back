from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    thread_id: str | None = Field(None, description="The ID of the chat thread")
    message: str = Field(..., description="The message to send in the chat")
    class Config:
        json_schema_extra = {
            "example": {
                "thread_id": "123e4567-e89b-12d3-a456-426614174000",
                "message": "Crie um nome para uma taverna de anões."
            }
        }

class ChatResponse(BaseModel):
    thread_id: str = Field(..., description="The ID of the chat thread")
    message: str = Field(..., description="The response message from the chat service")
    class Config:
        json_schema_extra = {
            "example": {
                "thread_id": "123e4567-e89b-12d3-a456-426614174000",
                "message": "Que tal 'A Bigorna Fulgurante' ou 'O Barril de Mithril'?"
            }
        }