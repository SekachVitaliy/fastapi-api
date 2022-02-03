from typing import List
from fastapi import APIRouter, Depends
from workshop.models.user_list import BaseUsersList
from workshop.services.user_list import UserListService

router = APIRouter(
    prefix='/user-list',
)


@router.get('/', response_model=List[BaseUsersList])
def get_user_list(service: UserListService = Depends()):
    return service.get_list()
