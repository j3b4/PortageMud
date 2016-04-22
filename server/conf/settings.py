"""
Evennia settings file.

The full options are found in the default settings file found here:

/home/aeon/Evennia/evennia/evennia/settings_default.py

Note: Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

"""

# Use the defaults from Evennia unless explicitly overridden
import os
from evennia.settings_default import *

######################################################################
# Portage Overloads
######################################################################

# WEBSOCKET_CLIENT_URL = 'ws://j3b.mdns.org'


#####################################################################
# Contrib config                                                    #
#####################################################################
GAME_INDEX_LISTING = {
        'game_status': 'pre-alpha',
        'game_website': 'http://j3b.mdns.org:8000/',
        'listing_contact': 'j3b@3b1.org',
        'telnet_hostname': 'j3b.mdns.org',
        'telnet_port': 4000,
        'short_description': 'Horatio Hornblower meets Dwarf Fortress',
        'long_description': '''
Horatio Hornblower is a fictional
Napoleonic Wars era Royal Navy officer who is the protagonist
of a series of novels by C. S. Forester. He was later the
subject of films and radio and television programs..... Dwarf
Fortress (officially called Slaves to Armok: God of Blood
Chapter II: Dwarf Fortress) is a part construction and
management simulation, part roguelike, indie video game
created by Tarn and Zach Adams.
'''
                }

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Portage"

# Path to the game directory (use EVENNIA_DIR to refer to the
# core evennia library)
GAME_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Place to put log files
LOG_DIR = os.path.join(GAME_DIR, "server", "logs")
SERVER_LOG_FILE = os.path.join(LOG_DIR, 'server.log')
PORTAL_LOG_FILE = os.path.join(LOG_DIR, 'portal.log')
HTTP_LOG_FILE = os.path.join(LOG_DIR, 'http_requests.log')

# Other defaults
PROTOTYPE_MODULES = ("world.prototypes",)

######################################################################
# Evennia Database config
######################################################################

# Database config syntax:
# ENGINE - path to the the database backend. Possible choices are:
#            'django.db.backends.sqlite3', (default)
#            'django.db.backends.mysql',
#            'django.db.backends.postgresql_psycopg2',
#            'django.db.backends.oracle' (untested).
# NAME - database name, or path to the db file for sqlite3
# USER - db admin (unused in sqlite3)
# PASSWORD - db admin password (unused in sqlite3)
# HOST - empty string is localhost (unused in sqlite3)
# PORT - empty string defaults to localhost (unused in sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(GAME_DIR, "server", "evennia.db3"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
        }}

######################################################################
# Django web features
# (don't remove these entries, they are needed to override the default
# locations with your actual GAME_DIR locations at run-time)
######################################################################

# Absolute path to the directory that holds file uploads from web apps.
# Example: "/home/media/media.lawrence.com"
MEDIA_ROOT = os.path.join(GAME_DIR, "web", "media")

# The master urlconf file that contains all of the sub-branches to the
# applications. Change this to add your own URLs to the website.
ROOT_URLCONF = 'web.urls'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure
# to use a trailing slash. Django1.4+ will look for admin files under
# STATIC_URL/admin.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(GAME_DIR, "web", "static")

# Directories from which static files will be gathered from.
STATICFILES_DIRS = (
    os.path.join(GAME_DIR, "web", "static_overrides"),
    os.path.join(EVENNIA_DIR, "web", "static"),)

# We setup the location of the website template as well as the admin site.
TEMPLATE_DIRS = (
    os.path.join(GAME_DIR, "web", "template_overrides", ACTIVE_TEMPLATE),
    os.path.join(GAME_DIR, "web", "template_overrides"),
    os.path.join(EVENNIA_DIR, "web", "templates", ACTIVE_TEMPLATE),
    os.path.join(EVENNIA_DIR, "web", "templates"),)

# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = '?/,yM-S9rnbqTjR"c7Z:CB#"@AIak^HusQ(;g`&N'
