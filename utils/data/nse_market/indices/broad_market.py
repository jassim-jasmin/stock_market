#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 14-09-2022 11:25 AM

@author: Mohammed Jassim
"""
from utils.data.nse_market.indices.api import API


class BroadMarketIndices(API):
    name = 'Broad Market Indices'

    class Nifty50(API):
        name = 'NIFTY 50'

    class NiftyNext50(API):
        name = 'NIFTY NEXT 50'

    class Nifty100(API):
        name = 'NIFTY NEXT 50'

    class Nifty200(API):
        name = 'NIFTY 200'

    class Nifty500(API):
        name = 'NIFTY 500'

    class MidCap50(API):
        name = 'NIFTY MIDCAP 50'

    class MidCap100(API):
        name = 'NIFTY MIDCAP 100'

    class SmallCap100(API):
        name = 'NIFTY SMLCAP 100'

    class IndiaVix(API):
        name = 'INDIA VIX'

    class MidCap150(API):
        name = 'NIFTY MIDCAP 150'

    class SmallCap50(API):
        name = 'NIFTY SMLCAP 50'

    class SmallCap250(API):
        name = 'NIFTY SMLCAP 250'

    class MidSmall400(API):
        name = 'NIFTY MIDSML 400'
