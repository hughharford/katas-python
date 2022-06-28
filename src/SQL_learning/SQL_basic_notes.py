

# CREATE TABLE, WITH CONSTRAINTS:

# new table, if not extant, with some constraints
DB_TABLE_CREATE = '''CREATE TABLE IF NOT EXISTS searches
(
   ID INT PRIMARY KEY NOT NULL,
   [search_input] TEXT NOT NULL,
   [postcode] BOOLEAN NOT NULL,
   [count_search] INTEGER,
   UNIQUE (ID, postcode)
);'''


INSERT_INTO_SEARCHES_TABLE = '''
        INSERT INTO searches (
            search_input,
            postcode,
            count_search)

        VALUES
        ('SE23 3YL','SE23 3YL', 45),
        ('G3 xxx','G3 xxx', 1001),
        ('latt long','SE23 3YL', 23)
        ;
    '''

CONFIRM_ALL_DATA_FROM_SEARCHES = '''
            SELECT
            search_input,
            postcode,
            count_search
            FROM searches
          '''
