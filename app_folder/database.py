import psycopg2

def create_db():
## create db

    
        try:
        ### create or connect to db

                conn = psycopg2.connect(
                database='BIMS',
                user='postgres',
                password='postgres',
                host='localhost',
                port= '5432')

                conn.autocommit = True

                cursor = conn.cursor()

                

                cursor.execute("""CREATE TABLE IT_Devices (
                        code text PRIMARY KEY,
                        device_type text,
                        serial text UNIQUE,
                        location text,
                        label_printed boolean
                        );""")

        except:
                pass

        

        

    

create_db()