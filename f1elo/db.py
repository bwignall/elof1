import __main__
from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json

config = json.load(open(path.dirname(__main__.__file__) + '/config/db.json'))
engine = create_engine("mysql://{0[user]}:{0[pass]}@{0[host]}/{0[db]}?charset=utf8".format(config))
Session = sessionmaker(bind=engine)

from f1elo.model import Driver

def find_driver(name, country, session):
    driver = session.query(Driver).filter(Driver.driver==name).first()
    if driver:
        return driver
    else:
        driver = Driver()
        driver.driver = name
        driver.country = country
        session.add(driver)
        return driver

