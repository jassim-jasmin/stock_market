#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 12-09-2022 01:17 PM

@author: Mohammed Jassim
"""
from utils.data.nse_market.common.inner_class_list import InnerClassList
base = "https://www.nseindia.com/api/{route}"
page_url = "https://www.nseindia.com/get-quotes/equity?symbol=LT"


class Route:
    name = "route"

    class StockMeta:
        name = "/equity-meta-info"

    class StockQuote:
        name = "/quote-equity"

    class StockDerivativeQuote:
        name = "/quote-derivative"

    class MarketStatus:
        name = "/marketStatus"

    class ChartData:
        name = "/chart-databyindex"

    class MarketTurnover:
        name = "/market-turnover"

    class EquityDerivativeTurnover:
        name = "/equity-stock"

    class AllIndices:
        name = "/allIndices"

    class LiveIndex:
        name = "/equity-stockIndices"

    class IndexOptionChain:
        name = "/option-chain-indices"

    def __call__(self):
        return InnerClassList.inner_classes_name_list(self)


class URL:
    name = 'url'
    # url = base.format(route="equity-stockIndices")

    @staticmethod
    def url(route_object: Route) -> str:
        return base.format(route=route_object.name)


if __name__ == '__main__':
    route = Route()()
    print(route)
