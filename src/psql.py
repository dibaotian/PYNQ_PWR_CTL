#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import db_config

db_params = db_config.db_conn_config()

commands = (
        """
        CREATE TABLE IF NOT EXISTS power_status_table(
           power_status                    boolean                 NOT NULL default FALSE
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS power_process_table(
           serial                        serial                      PRIMARY KEY NOT NULL,
           power_status                  boolean                     NOT NULL default FALSE ,
           exec_time                     timestamp with time zone    NOT NULL DEFAULT now()
        )
        """
)

def create_tables():
    """ create tables in the PostgreSQL database"""
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        print (commands)
        # cur.execute(commands)
        # create table one by one
        for command in commands:
            print (command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
        print(error)
    finally:
        if conn is not None:
            print("create tables succeed")
            conn.close()
    return 0

def update_power_status(status):

    ret = False

    conn = None
    sql = 'UPDATE power_status_table SET power_status = %s'

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute(sql % (status))
        conn.commit()
        cur.close()
        ret = True
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
        print (error)
    finally:
        if conn is not None:
            conn.close()

    return ret

def recoder_power_process(status):

    ret = False

    conn = None
    sql = 'INSERT INTO power_process_table (power_status) VALUES (%s)'

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute(sql % (status))
        conn.commit()
        cur.close()
        ret = True
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
        print (error)
    finally:
        if conn is not None:
            conn.close()

    return ret

if __name__ == '__main__':
    
    # create_tables()
    ret = update_power_status(True)
    if ret:
        recoder_power_process(True)

    

