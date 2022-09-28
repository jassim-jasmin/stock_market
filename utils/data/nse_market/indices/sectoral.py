#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 14-09-2022 11:24 AM

@author: Mohammed Jassim
"""
from utils.data.nse_market.indices.api import API


class Sectoral(API):
    name = 'Sectoral'

    class Bank(API):
        name = 'NIFTY BANK'

    class Auto(API):
        name = 'NIFTY AUTO'

    class FinService(API):
        name = 'NIFTY FIN SERVICE'

    class Fmcg(API):
        name = 'NIFTY FMCG'

    class It(API):
        name = 'NIFTY IT'

    class Media(API):
        name = 'NIFTY MEDIA'

    class Metal(API):
        name = 'NIFTY METAL'

    class Pharma(API):
        name = 'NIFTY PHARMA'

    class PsuBank(API):
        name = 'NIFTY PSU BANK'

    class PvtBank(API):
        name = 'NIFTY PVT BANK'

    class Reality(API):
        name = 'NIFTY REALTY'
