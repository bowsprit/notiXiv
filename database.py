"""
"""
import sqlalchemy as sqla
import sqlalchemy_utils as sqla_utils

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    # 'port': '',
    'username': '',
    'password': '',
    'database': 'test_db'
}

DeclarativeBase = sqla.ext.declarative.declarative_base


class ArticleModel(DeclarativeBase):
    """SQLAlchemy Model for the Articles Table.
    """
    __tablename__ = "articles"

    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column('title', sqla.String)
    link = sqla.Column('link', sqla.String)
    authors = sqla.Column('authors', sqla.String, nullable=True)
    published_date = sqla.Column('published_date', sqla.String, nullable=True)

    def __init__(self, title, link, authors=[], published=''):
        self.title = title
        self.link = link
        self.authors = authors
        self.published_date = published
        return

    def __repr__(self):
        return "{}(title={}, link={}, authors={}, pubished={})".format(
            self.__class__, self.title, self.link, self.authors, self.published)

    def __str__(self):
        return "{} - {} - {}".format(self.authors, self.title, self.published)


class UserModel(DeclarativeBase):
    """SQLAlchemy Model for the Users Table.
    """
    __tablename__ = "users"
    id = sqla.Column(sqla.Integer, primary_key=True)
    name_user = sqla.Column('name_user', sqla.String)
    password = sqla.Column('password', sqla.String)
    email = sqla.Column('email', sqla.String)
    name_full = sqla.Column('name_full', sqla.String, nullable=True)

    def __init__(self, username, password, email, fullname=''):
        self.name_user = username
        self.password = password
        self.email = email
        self.fullname = fullname
        return


class Pipeline(object):
    """
    """
    def __init__(self):
        url = sqla.engine.url.URL(**DATABASE)
        engine = sqla.create_engine(url, echo=True)





def main():
    print("main()")

    # Create Database if it doesnt exist
    db_exists = sqla_utils.database_exists(engine.url)
    print("-   Database exists: ", db_exists)
    if not db_exists:
        sqla_utils.create_database(engine.url)
        print("    +   Database created.")

    # Create all Tables
    DeclarativeBase.metadata.create_all(engine)

    # Delete Database
    sqla_utils.drop_database(engine.url)
    print("-   Database dropped.")
    db_exists = sqla_utils.database_exists(engine.url)
    print("    +   Database exists: ", db_exists)

    return

if __name__ == "__main__":
    main()
