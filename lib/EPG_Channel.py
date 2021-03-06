#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EPG_Channel(object):
    """A Interface Class for EPG"""

    def fetch(self, utc_date = None, utc_time = None, day = None):
        """Return the EPG of today by default"""
        raise NoImplementedError()

    def store(self, db_type = None, db_config = None):
        """Print the EPG by default"""
        raise NoImplementedError()
