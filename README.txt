You thought it was a database, but it is I, Brandon Waggoner!

This file shows a rough mockup of what we expect the database to look like.

DATABASE: check-ai
TABLES: User, Preferences
** Maybe use a table for each type of preference, i.e. location, skill, etc


==========
===USER===
==========
 --------------------
| UID | Name | Field |
 --------------------

=================
======Skills=====
=================
 ---------------------------
| skillID |   skill   | UID |
 ---------------------------


=====================
=====Preferences=====
=====================
 ---------------------
| prefID | pref | UID |
 --------------------


=====================
======Exclusions=====
=====================
 ---------------------
| exclID | excl | UID |
 ---------------------
