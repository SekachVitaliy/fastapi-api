from database import engine
from tables import Base, User

print("Creating database ....")

Base.metadata.create_all(engine)
