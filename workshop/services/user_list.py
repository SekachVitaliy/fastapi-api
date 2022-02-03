from fastapi import Depends
from .. import tables
from workshop.database import Session, get_session


class UserListService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self):
        users = self.session.query(tables.User).all()
        return users
