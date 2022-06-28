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

############### ################### #####################
#                  1st witness
############### ################### #####################


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
    where person_id = 16371
    '''

'''
I saw the murder happen,
and I recognized the killer from my gym
when I was working out last week on January the 9th.
'''

first_attempt = '''
SELECT *
FROM interview
where witness_name = "Annabel"
and witness_address = "Franklin Ave";
'''

FIND_GYM_MEMBER_ID_NO = '''
    SELECT *
    FROM get_fit_now_member
    WHERE person_id = 16371
'''

'''
id	person_id	name	membership_start_date	membership_status
90081	16371	Annabel Miller	20160208	gold
'''


FIND_AM_GYM_TIME_ON_DATE = '''
    SELECT *
    FROM get_fit_now_check_in
    WHERE  check_in_date = 20180109
    AND membership_id = 90081
'''

'''
### WITH JUST ANNABEL:

membership_id	check_in_date	check_in_time	check_out_time
90081	20180109	1600	1700
'''

FIND_ALL_MEMBERS_AT_SPECIFIC_TIME = '''
    SELECT *
    FROM get_fit_now_check_in
    WHERE  check_in_date = 20180109
    AND check_in_time <= 1600
    AND check_out_time >= 1700
    '''

'''
### WITH ALL MEMBERS AT SPECIFIC TIME:

membership_id	check_in_date	check_in_time	check_out_time
48Z7A	20180109	1600	1730
48Z55	20180109	1530	1700
90081	20180109	1600	1700
'''

############### ################### #####################
#                  2nd witness
############### ################### #####################


'''
The first witness lives at the last house on "Northwestern Dr".
'''
