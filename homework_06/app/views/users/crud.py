from sqlalchemy import select, exists, func

from models import db, User



class UsersStorage:

    def create(self, name: str, username: str, email: str) -> User:
        user = User(
            name=name,
            username=username,
            email=email
        )
        db.session.add(user)
        db.session.commit()
        return user


    def get(self) -> list[User]:
        results = db.session.scalars(select(User).order_by("id")).all()
        return list(results)


    def get_by_id(self, user_id: int) -> User | None:
        return db.session.get(User, ident=user_id)


    def username_exists(self, username_check: str) -> bool:
        stmt = exists().where(
            func.lower(User.username) == username_check.lower()
        )
        return db.session.scalar(select(stmt))
    

    def email_exists(self, email_check: str) -> bool:
        stmt = exists().where(
            func.lower(User.email) == email_check.lower()
        )
        return db.session.scalar(select(stmt))



users_storage = UsersStorage()