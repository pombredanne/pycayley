#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pycayley is a simple python client for Cayley Database.

Homepage http://github.com/canerbasaran/pycayley

Copyright (c) 2014, Caner Başaran.
License: MIT (see LICENSE for details)
"""

__author__ = 'Caner Başaran'
__version__ = '0.1-dev'
__license__ = 'MIT'

import requests


def request(url, data):
    return requests.post(url, data=data).json()


class Graph(object):
    def __init__(self, url="http://localhost:64210", version="v1"):
        self.url = "%s/api/%s/" % (url, version)

    def qg(self, query):
        return request(self.url+"query/gremlin", query)

    def qm(self, query):
        return request(self.url+"query/mql", query)

    def sg(self, query):
        return request(self.url+"shape/gremlin ", query)

    def sm(self, query):
        return request(self.url+"shape/mql", query)

    def w(self, query):
        return request(self.url+"write", query)

    def wfn(self, query):
        return request(self.url+"write/file/nquad", query)

    def d(self, query):
        return request(self.url+"delete", query)