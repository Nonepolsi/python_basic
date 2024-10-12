from sqlalchemy import select, exists, func

from models import db, Post



class PostsStorage:

    def create(self, title: str, body: str, user_id: int) -> Post:
        post = Post(
            title=title,
            body=body,
            user_id=user_id
        )
        db.session.add(post)
        db.session.commit()
        return post


    def get(self) -> list[Post]:
        results = db.session.scalars(select(Post).order_by("id")).all()
        return list(results)


    def get_by_id(self, post_id: int) -> Post | None:
        return db.session.get(Post, ident=post_id)


    def title_exists(self, title_check: str) -> bool:
        stmt = exists().where(
            func.lower(Post.title) == title_check.lower()
        )
        return db.session.scalar(select(stmt))



posts_storage = PostsStorage()