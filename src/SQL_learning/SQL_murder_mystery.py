# SQL Mystery...
#               https://mystery.knightlab.com/

# NOTE_BENE: SQLite database


SEE_TABLES_IN_DB = '''
    SELECT name
    FROM sqlite_master
    where type = "table"'''

'''response:
name
#####
crime_scene_report
drivers_license
person
facebook_event_checkin
interview
get_fit_now_member
get_fit_now_check_in
income
solution
'''

SEE_SQL_STRUCTURE_OF_TABLE_NAME = '''
    SELECT sql
    FROM sqlite_master
    where name = "crime_scene_report";
    '''

SEE_CRIME_SCENE_REPORT = '''SELECT *
    FROM crime_scene_report
    where city = "SQL City"
        and date = "20180115"
        and type = "murder";'''

'''response:
date: 20180115
type: murder
description:
    Security footage shows that there were 2 witnesses.
    The first witness lives at the last house on "Northwestern Dr".
    The second witness, named Annabel, lives somewhere on "Franklin Ave".
city: SQL City'''

FIND_PERSONS_ON_FRANKLIN_AVE ='''
    SELECT *
    FROM person
    where address_street_name = "Franklin Ave"
    '''

FIND_PERSON_ID_FOR_ANNABEL_MILLER ='''
    SELECT *
    FROM person
    where address_street_name = "Franklin Ave"
    and name = "Annabel Miller"
    '''

'''
id	         name	   license_id	address_number	address_street_name	  ssn
16371	Annabel Miller	490173	    103	            Franklin Ave	      318771143
'''


FIND_WITNESS_INTERVIEW ='''
    SELECT transcript
    FROM interview
    where person_id = INT
    '''

first_attempt = '''
SELECT *
FROM interview
where witness_name = "Annabel"
and witness_address = "Franklin Ave";
'''
