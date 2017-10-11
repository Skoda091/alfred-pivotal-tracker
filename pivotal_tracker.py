#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2017 Adam Skołuda
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2017-10-11
#

"""
Manage Pivotal Tracker API
"""

from __future__ import division, print_function, unicode_literals, absolute_import

import sys

from workflow import Workflow, web, ICON_WEB

UPDATE_SETTINGS = {'github_slug': 'Skoda091/alfred-pivotal-tracker'}

ICON_PL = ''
ICON_EN = ''

# Shown in error logs. Users can find help here
HELP_URL = 'https://github.com/Skoda091/alfred-pivotal-tracker'

# Base API url for Pivotal Tracker API
API_URL = 'https://www.pivotaltracker.com/services/v5'

# Pivotal Tracker API V5 documentation
API_DOCS = 'https://www.pivotaltracker.com/help/api/rest/v5'

# How long to cache results for
CACHE_MAX_AGE = 20  # seconds

def main(wf):
    import argparse
    import re
    import requests
    import json    # Get args from Workflow, already in normalized Unicode

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))