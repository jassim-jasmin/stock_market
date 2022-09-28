#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
todo: Change name apt to api_handling
Created on 14-09-2022 12:29 PM

@author: Mohammed Jassim
"""
from json import loads
from requests import Session
from utils.data.nse_market.common.constant.api_headers import equity_stock_indices
from utils.data.nse_market.common.constant.general import page_url, URL


class API(URL):
    def __init__(self):
        self.session = Session()
        self.session.headers.update(equity_stock_indices)
        self.session.get(page_url)
        self.params = {}
        self.time_out = 5

    def get(self, route, params):
        if response := self.session.get(self.url(route), params=params):
            return loads(response.content)
