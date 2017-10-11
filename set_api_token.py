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
Set Pivotal Tracker API token
"""

from __future__ import division, print_function, unicode_literals, absolute_import

import sys

from workflow import Workflow, web, ICON_WEB



def main(wf):
    # import argparse
    # import re
    # import requests
    # import json    # Get args from Workflow, already in normalized Unicode

    text = " ".join(wf.args)
    print(text)

    wf.save_password('aol', 'hunter2')

    password = wf.get_password('aol')

    wf.delete_password('aol')

    # raises PasswordNotFound exception
    # password = wf.get_password('aol')

    # wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))