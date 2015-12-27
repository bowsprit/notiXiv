"""
"""
import logging

import sqlalchemy as sqla
import sqlalchemy_utils as sqla_utils


import utils

DATABASE = {
    # 'drivername': 'mysql',
    'drivername': 'mysql+pymysql',
    'host': 'host126.hostmonster.com',
    # 'port': '',
    'username': 'mhastery_krustee',
    'password': '6#g!UW%@3%ry',
    'database': 'mhastery_krustee'
}


def main():
    log = utils.getLogger(__name__, strLevel=logging.DEBUG, fileLevel=logging.DEBUG,
                          tofile='log_krustee.txt')
    log.debug("main()")

    url = sqla.engine.url.URL(**DATABASE)
    log.debug("-   Creating Engine with url '{}'.".format(url))
    engine = sqla.create_engine(url)
    
    # Create Database if it doesnt exist
    db_exists = sqla_utils.database_exists(engine.url)
    log.debug("-   Database exists: ", db_exists)
    '''
    if not db_exists:
        sqla_utils.create_database(engine.url)
        log.debug("    +   Database created.")

    self.Session = sqla.orm.sessionmaker(bind=engine)
    '''

    return

if __name__ == "__main__":
    main()
