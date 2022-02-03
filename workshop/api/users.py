from fastapi import APIRouter, Depends, status
from workshop.models.users import BaseUsers, UpdateUsers, Update_fields_Users
from workshop.services.users import UserService

router = APIRouter(
    prefix='/user',
)


@router.post('/', response_model=BaseUsers, status_code=status.HTTP_201_CREATED)
def add_user(user: UpdateUsers, service: UserService = Depends()):
    return service.add_user(user)


@router.get('/{user_id}', response_model=BaseUsers, status_code=status.HTTP_200_OK)
def get_user(user_id: int, service: UserService = Depends()):
    return service.get_user(user_id)


@router.put('/{user_id}', response_model=BaseUsers, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUsers, service: UserService = Depends()):
    return service.update_user(user_id, user)


@router.patch('/{user_id}', response_model=BaseUsers, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: Update_fields_Users, service: UserService = Depends()):
    return service.update_fields_user(user_id, user)


@router.delete('/{user_id}')
def delete_user(user_id: int, service: UserService = Depends()):
    return service.delete_user(user_id)
