"""
Purpose:
    This script used to read the data from the project.
    and pass these data to other modules in backend.
Inputs:
    - No inputs to this file
Outputs:
    The project configurations will be passed.
Author: Pasan Kamburugamuwa
"""

import configparser
import logging
import traceback
import os
import sys
from psycopg2 import pool
from contextlib import contextmanager

LOG_DIR = "/Users/pkamburu/IUNI/ECC-Project/log"
LOG_FNAME = "database_server.log"

def get_project_conf():
    """
    Get the mastodon configuration file.
    """
    try:
        config_file_path = "./config/project.config"
        config_parser = configparser.ConfigParser()
        config_parser.read(config_file_path)
        return config_parser
    except FileNotFoundError as fnf_error:
        traceback.print_tb(fnf_error.__traceback__)
        raise Exception('Unable to find the mastodon config file')

def get_database_host():
    """
    Get the database host.
    """
    try:
        config = get_project_conf()
        database_host = config["POSTGRESQL_DATABASE"]["database-host"]
        return database_host
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception('Unable to find the database host')

def get_database_port():
    try:
        config = get_project_conf()
        database_port = config["POSTGRESQL_DATABASE"]["database-port"]
        return database_port
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database port')

def get_database_name():
    try:
        config = get_project_conf()
        database_name = config["POSTGRESQL_DATABASE"]["database-name"]
        return database_name
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database name')

def get_database_username():
    try:
        config = get_project_conf()
        database_username = config["POSTGRESQL_DATABASE"]["database-username"]
        return database_username
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database username')

def get_database_password():
    try:
        config = get_project_conf()
        database_password = config["POSTGRESQL_DATABASE"]["database-password"]
        return database_password
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database password')

db = None


try:
    db = pool.SimpleConnectionPool(1,
                                10,
                                host=get_database_host(),
                                database=get_database_name(),
                                user=get_database_username(),
                                password=get_database_password(),
                                port=get_database_port())
except:
    pass

@contextmanager
def get_db_connection():
    con = db.getconn()
    try:
        yield con
    finally:
        db.putconn(con)


@contextmanager
def get_db_cursor():
    with get_db_connection() as connection:
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        finally:
            cursor.close()

def get_logger(LOG_DIR, LOG_FNAME, script_name=None, also_print=False):
    """
    Create logger for the project.
    """
    # Create log_dir if it doesn't exist already
    try:
        os.makedirs(f"{LOG_DIR}")
    except:
        pass

    # Create logger and set level
    logger = logging.getLogger(script_name)
    logger.setLevel(level=logging.INFO)

    # Configure file handler
    formatter = logging.Formatter(
        fmt="%(asctime)s-%(name)s-%(levelname)s - %(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S",
    )
    full_log_path = os.path.join(LOG_DIR, LOG_FNAME)
    fh = logging.FileHandler(f"{full_log_path}")
    fh.setFormatter(formatter)
    fh.setLevel(level=logging.INFO)
    # Add handlers to logger
    logger.addHandler(fh)

    # If also_print is true, the logger will also print the output to the
    # console in addition to sending it to the log file
    if also_print:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        ch.setLevel(level=logging.INFO)
        logger.addHandler(ch)
    return logger