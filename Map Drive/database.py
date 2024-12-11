import sqlite3

def create_db():
## create db

    try:

        ### create or connect to db

        conn = sqlite3.connect("BIM.db")

        ### create curser
        c = conn.cursor()

        ## create table

        c.execute("""CREATE TABLE BIM (
                code text,
                device_type text,
                serial text,
                location text,
                label_printed boolean
                )""")
        conn.commit()

    except:
        pass



def add_column(name):
    conn = sqlite3.connect("BIM.db")
    c = conn.cursor()
    c.execute(f"""
              
            ALTER TABLE BIM
            ADD {name} text;
              
              """)
    conn.commit()