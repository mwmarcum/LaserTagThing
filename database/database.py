import psycopg2
import psycopg2.extras
import os


class db:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def open(self):
        """ connect to the database """

        dbURL = os.environ.get("DATABASE_URL")
        self.connection = psycopg2.connect(dbURL, sslmode = "require")
        self.cursor = self.connection.cursor(cursor_factory = psycopg2.extras.DictCursor)


        """ create the player table """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS player (
                id INT PRIMARY KEY,
                first_name VARCHAR(30),
                last_name VARCHAR(30),
                codename VARCHAR(30)
            );
        """)
        self.connection.commit()


    def insert(self, id, first_name, last_name, codename):
        """
        inserts a new player

        returns a boolean for whether the insert was successful
        """

        try:
            self.cursor.execute("""
                INSERT INTO player (id, first_name, last_name, codename)
                VALUES (%s, %s, %s, %s);
            """, (id, first_name, last_name, codename))
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False


    def upsert(self, id, first_name, last_name, codename):
        """
        inserts a new player, updates the player if there already is one with the same id

        returns a boolean for whether the upsert was successful
        """

        try:
            self.cursor.execute("""
                INSERT INTO player (id, first_name, last_name, codename)
                VALUES (%(id)s, %(first_name)s, %(last_name)s, %(codename)s)
                ON CONFLICT (id)
                DO UPDATE
                SET first_name = %(first_name)s, last_name = %(last_name)s, codename = %(codename)s;
            """, {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "codename": codename
            })
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False


    def update(self, id, first_name, last_name, codename):
        """ update a player's data """

        try:
            self.cursor.execute("""
                UPDATE player
                SET first_name = %(first_name)s, last_name = %(last_name)s, codename = %(codename)s
                WHERE id = %(id)s;
            """, {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "codename": codename
            })
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False


    def delete(self, id):
        """ delete a player """

        self.cursor.execute("""
            DELETE FROM player
            WHERE id = %s;
        """, (id,))

        self.connection.commit()


    def fetch(self, id):
        """
        fetches a player

        returns a dictionary or None
        """

        self.cursor.execute("""
            SELECT first_name, last_name, codename FROM player
            WHERE id = %s;
        """, (id,))

        return self.cursor.fetchone()


    def close(self):
        """ close the database connection """

        self.cursor.close()
        self.connection.close()
