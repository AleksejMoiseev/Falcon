from pydantic import BaseModel


class User(BaseModel):
    pk: int
    username: str


class Chat(BaseModel):
    pk: int
    title: str


class ChatMessage(BaseModel):
    pk: int
    chat: Chat
    user: User
    message: str
