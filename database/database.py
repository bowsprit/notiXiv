"""
"""
import sqlalchemy as sqla
import sqlalchemy_utils as sqla_utils
# from sqlalchemy_utils import database_exists, create_database

DB_NAME = "test_db"
_DB_SERVER_TYPE = "postgres"  # "mysql"
_DB_SERVER_ADDRESS = "localhost"


def db_url(name, server=_DB_SERVER_TYPE, address=_DB_SERVER_ADDRESS):
    url = "{}://{}/{}".format(name, address, server)
    return url


def main():
    print("main()")
    url = db_url(DB_NAME)
    print("-   URL: '{}'.".format(url))
    engine = sqla.create_engine(url)
    print("-   Engine created.")

    print("-   Database exists?: ", sqla_utils.database_exists(engine.url))
    sqla_utils.drop_database(engine.url)
    print(sqla_utils.database_exists(engine.url))


if __name__ == "__main__":
    main()
