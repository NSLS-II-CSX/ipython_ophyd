import logging
session_mgr._logger.setLevel(logging.INFO)
from ophyd.userapi import *

from pyOlog import conf

def change_logbook(logbook_name):
    conf._conf.cf.set(conf._conf.heading,
                      'logbooks',
                      value=logbook_name)
