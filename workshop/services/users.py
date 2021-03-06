from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import tables
from ..database import get_session
import bcrypt


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self):
        users = self.session.query(tables.User).all()
        return users

    def add_user(self, user):
        user_to_add = self.session.query(tables.User).filter(tables.User.username == user.username).first()
        if user_to_add:
            raise HTTPException(status_code=400, detail="The user already exists")
        new_user = tables.User(
            username=user.username,
            email=user.email,
            password=bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        )
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user(self, user_id):
        user = self.session.query(tables.User).filter(tables.User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail="The user does not exist")
        return user

    def update_user(self, user_id, user):
        user_to_update = self.get_user(user_id)
        user_to_update.username = user.username
        user_to_update.email = user.email
        user_to_update.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        self.session.commit()
        return user_to_update

    def update_fields_user(self, user_id, user):
        user_to_update_fields = self.get_user(user_id)
        if user.username:
            user_to_update_fields.username = user.username
        if user.email:
            user_to_update_fields.email = user.email
        if user.password:
            user_to_update_fields.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        self.session.commit()
        return user_to_update_fields

    def delete_user(self, user_id):
        user_to_delete = self.get_user(user_id)
        self.session.delete(user_to_delete)
        self.session.commit()
        return user_to_delete
