import sqlite3

conn = sqlite3.connect('/home/hsth/code/hughharford/data_ex_repos/euro_soccer_database.sqlite')
# use this row_factory to get easier access to the data (i.e. key:value etc)
conn.row_factory = sqlite3.Row
print(type(conn))

c = conn.cursor()
print(type(c))

a = c.execute('SELECT * FROM Country WHERE Country.id = 1')
b = c.execute('SELECT "Match".id \
            ,"Match".season \
            ,"Match".stage \
            ,"Match".date \
            FROM "Match" AS m')  # with: AS alias, the AS isn't required

c.execute('''SELECT league_id, c.name, COUNT(*)
FROM "Match" AS m
JOIN Country c on c.id = m.country_id
GROUP BY 1,2 ''')

third = '''SELECT m.id
            ,m.season
            ,m.stage
            ,m.league_id
            ,m.date
FROM "Match" AS m
WHERE m.country_id = 1 IN (1, 1729)'''

fourth = '''SELECT *
FROM Player
WHERE UPPER(Player.player_name) LIKE "JOHN %"'''

fifth = '''SELECT COUNT(Player.id)
FROM Player
WHERE Player.height >= 200'''

sixth = '''SELECT *
FROM Player
ORDER BY Player.weight DESC
LIMIT 10'''

seventh = '''SELECT COUNT(matches.id), matches.country_id AS num_matches
FROM "Match" AS matches
WHERE num_matches > 3000
GROUP BY matches.country_id
ORDER BY num_matches'''
# this has a logic issue with

eighth = '''SELECT COUNT(matches.id), matches.country_id AS num_matches
FROM "Match" AS matches
GROUP BY matches.country_id
HAVING num_matches > 3000
ORDER BY num_matches'''  # CHECK That this is any better!

ninth = '''SELECT id
	,home_team_goal
	,away_team_goal
	,CASE
		WHEN home_team_goal > away_team_goal
			THEN "Home Team Win"
		WHEN away_team_goal = home_team_goal
			THEN "Tie"
		ELSE "Away Team Win"
	END as outcome
	,COUNT(*)
FROM "Match" AS m
GROUP BY outcome
	'''

tenth_join = '''SELECT l.name as league_name, c.name as country_name
FROM League l
JOIN Country c ON l.country_id = c.id'''

# SQL is not case sensitive, SELECT === select etc

eleventh_groupby_indexing = '''SELECT league_id, c.name, COUNT(*)
FROM "Match" AS m
JOIN Country c on c.id = m.country_id
GROUP BY 1,2 '''

# The order of SQL statements matters

rows = c.fetchall()
# print(rows[0]['name'])
print(rows[0])
# print(rows)
