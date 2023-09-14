#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = u'Thomas Crha'
SITENAME = u'9bitbyte'
SITESUBTITLE = u'coffee | code | solder'
SITEURL = 'https://thomascrha.github.io'

PATH = 'content'
OUTPUT_PATH = '../thomascrha.github.io'
# OUTPUT_PATH = 'output'

COLOR_SCHEME_CSS = 'tomorrow_night.css'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/bitbyte9'),
          ('github', 'http://github.com/moosethemucha'),
	('linkedin', 'https://linkedin.com/in/thomascrha'))

DEFAULT_PAGINATION = 8
THEME='theme/clean-blog'

STATIC_PATHS = ['images', 'extra', 'static', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Uncomment following line if you want document-relative URLs when developing
GITHUB_URL = 'http://github.com/moosethemucha'
TWITTER_URL = 'http://twitter.com/bitbyte9'
DISQUS_SITENAME= 'thomascrha-github-io'
HEADER_COVER = 'images/background.jpg'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DELETE_OUTPUT_DIRECTORY = False

THEME_TEMPLATES_OVERRIDES = ['templates/pelican-resume']

# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['assets', 'sitemap']

# resume configuration

#Profile information
NAME = 'Thomas Crha'
TAGLINE = 'Full Stack Developer'
PIC = 'profile.png'

#sidebar links
EMAIL = 'thomas@9bitbyte.com'
PHONE = '(+61) 449 856 278'
WEBSITE = 'thomascrha.github.io'
LINKEDIN = 'thomascrha'
GITHUB = 'thomascrha'
LOCATION = 'https://goo.gl/maps/8v3rqbG4tePHxCNE6'
LOCATION_NAME = 'Sydney, Australia'

CAREER_SUMMARY = '''Hi I'm Tom, I'm a full stack software engineer with experience with large highly available, cloud-based web applications with a user base's in excess of 500k. I’ve worked closely with Python, AngularJS, JavaScript ES6 and AWS. I’ve also worked closely with various data science modules like pandas, NumPy and SciPy for doing data modelling and learning on various types of data (audio, video, text, lexicons). I also have vast experience with API integrations and creating and implementing ETL systems.'''


SKILLS = [
	{
		'title': 'Python &amp; Flask',
   		'level': '95'
   	},
  	{
  		'title': 'Javascript &amp; jQuery',
   		'level': '90'
   	},
    {
  		'title': 'HTML5 &amp; CSS',
  		'level': '95'
  	},
  	{
  		'title': 'AngularJS &amp; Vue.js',
  		'level': '90'
  	},
  	{
  		'title': 'BASH &amp; Perl',
  		'level': '85'
  	},
    {
  		'title': 'Linux',
  		'level': '95'
  	}
]

PROJECTS = [
	{
		'title': "Video transcription/annotation 'work page'",
		'tagline': '''allows users to mark the video using a view finder at multiple 
		points. These can be grouped into pairs (start and end) utilised for 
		transcription or singular points for annotations and tagging. It also allows 
		users to select areas in the video feed itself, this is utilised for 
		identifying specific object types specific to the collection.'''
	},
	{
		'title': 'End-to-end selenium testing suite',
		'tagline': '''a client-side testing suite implemented with server tests, 
		utilising selenium, docker and py-test allowing end-to-end testing of web 
		applications. The framework provides a simple methodology for working through 
		webpages via xpath's, allowing for DOM object waiting/checking.
								'''
	},
	{
		'title': 'Secure Transcription',
		'tagline': '''An application allowing for the automatic downloading of
		audio sources from a specialised body-cam provider. The application would listen 
		for new files to become available and download them, a separate application would 
		then host the files in air-gapped area allowing transcribers to-do their work. 
		The result is then sent to the body-cam provider. All this required a high level 
		of security and the utilisation of best practices.''' 
	}
]

INTERESTS = [
	'Gaming',
	'Electronics',
	'Metal Fabrication'
]

EXPERIENCES = [
	{
		'job_title': 'Front End Developer',
		'time': 'Jun 2019',
		'company': 'Wattwatchers Australia',
		'details': """One month contract working with Vue.js creating a onboarding app for there data trackers.""",
		'technologies': ["Vue.js", "python", "Django", "Timescale (PostgreSQL)", "webpack", "yarn", "bulma"]
	},
	{
		'job_title': 'System Developer',
		'time': 'Mar 2019',
		'company': 'Datatronic Australia',
		'details': """Two week contract integrating various systems (CRM, POS, Inventory) via there public API’s into one simple tool utilizing an internal DBMS system accessible via a simple SPA site.""",
		'technologies': ["Vue.js", "python", "Flask", "SQLAlchemy", "PostgresSQL", "Linux (Debian)", "xero", "reciptbank"]
	},
	{
		'job_title': 'Full Stack Software Engineer',
		'time': 'Mar 2018 - May 2019',
		'company': 'Appen Australia',
		'details': """Part of a small team maintaining Appen's language resource work tool, Ampersand. Running the day-to-day tasks of the site (dev-ops and infrastructure management), feature creation and bug fixing.""",
		'achievements': ["Helped move from our old system to Ampersand beginning 2018",
			"Managed our AWS cloud Infrastructure and CI deployments",
			"Managed tickets and bugs associated with the platform",
			"Developed features within a two-week sprint cycle",
			"Communicated and worked with product owners throughout the development cycle",
			"Helped increased testing code coverage too 85%",
			"Implemented our lexicon tool into Ampersand feature set",
			"Implemented the video transcription module used inside the tool allowing users to annotate video recordings."
		],
		'technologies': ["python", "flask", "SQLAlchemy", "PostgreSQL (AWS AZURE cloud)", "Elasticbeanstalk", "Travis", "Linux (Debian)", "AngularJS", "yarn", "webpack", "selenium", "docker-compose", "AWS", "JIRA", "pivotal", "Confluence",
		"Cloudwatch", "SNS", "celery", "EC2", "S3", "redis", "apache", "git", "git-flow", "lamda"]
	},
	{
		'job_title': 'Project Engineer',
		'time': 'Apr 2015 - Mar 2018',
		'company': 'Appen Australia',
		'details': "Creating custom solutions for various projects to meet client and business needs.",
		'achievements': ["Helped transition from python2 -> python3 (conversion of scripts and sites)",
			"Developed custom scripts/web applications for client projects",
			"Linux server work to deploy and manage the various scripts/web applications",
			"Maintaining data flow in and out of our various tools as the projects desired",
			"Automation of tasks for project management and organisation",
			"Worked closely with project managers to load and package data for clients",
			"Data Science (reporting, language analysis) utilizing various python modules",
			"Created multiple different packaging scripts and workflows for repeat clients",
			"Created a automated backup system utilising AWS's Glacier storage tier",
			"Various API and ETL integration’s"
		],
		'technologies': ["Python", "Flask", "SQLAlchemy","Linux (Debian)", "react", "Vue.js", "scrapy", "SciPy", "pandas", "selenium", "bash", "vim", "requests", "JIRA", "Confluence","sed", "awk", "GNU utils", "apache"]
	},
	{
		'job_title': 'Founder and Operator',
		'time': '2014 - present',
		'company': '9 Bit Byte',
		'details': 'A computer solution company providing mainly small business in my local area with various tech services and assistance.',
	},
	{
		'job_title': 'Lead Developer and System Administrator',
		'time': '2015 - 2017',
		'company': 'Outflanked Paytracker, AUS',
		'details': 'An application allowing workers to track there pay when they work unusual hours and on forever adjusting award rates.',
		'technologies': ["AngularJS", "node.js", "Heroku"]
	},
]

LANGUAGES = [
	{
		'name': 'English',
		'description': 'Native'
	},
	{
		'name': 'Czech',
		'description': 'Amateur'
	}
]

EDUCATIONS = [
	{
		'degree': 'B.E in Information Technology - Major System Admin ',
		'meta': 'Charles Sturt University CSU via distance',
		'time': '2011 - 2015'
	},
	{
		'degree': 'HSC &amp; SC',
		'meta': 'Blue Mountians Grammar School',
		'time': '1999-2000'
	},
	{
		'degree': 'OH/S Construction Induction Training Certificate',
		'meta': '',
		'time': ''
	},
	{
		'degree': 'RSA &amp; RCG',
		'meta': '',
		'time': ''
	}
]

MENUITEMS = (
  ('Home','/'),
  ('About','/about/'),
)
