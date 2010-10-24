# -*- coding: utf-8 -*-
"""Setup the barcamp.roc.fall.2010 application"""

import logging
import transaction
from tg import config

def setup_schema(command, conf, vars):
    """Place any commands to setup melissa_is_a_babe here"""
    # Load the models

    # <websetup.websetup.schema.before.model.import>
    from melissa_is_a_babe import model
    # <websetup.websetup.schema.after.model.import>

    
    # <websetup.websetup.schema.before.metadata.create_all>
    print "Creating tables"
    model.metadata.create_all(bind=config['pylons.app_globals'].sa_engine)
    # <websetup.websetup.schema.after.metadata.create_all>
    transaction.commit()
