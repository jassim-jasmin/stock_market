#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 13-09-2022 10:12 AM

@author: Mohammed Jassim
"""
from utils.data.nse_market.indices import *
from utils.data.nse_market.common.constant.general import Route
from utils.data.nse_market.common.api_request_caching import live_cache


class Live(API):
    time_out = 5

    @live_cache
    def chart_data(self, symbol: str, indices=False):
        data = {"index": symbol + "EQN"}

        if indices:
            data["index"] = symbol
            data["indices"] = "true"

        return self.get(Route.ChartData, data)

    @staticmethod
    def live_index(index_object):
        data = {"index": index_object.name}

        return index_object.get(Route.LiveIndex, data)


if __name__ == '__main__':
    live = Live()
    # result = live.live_index(BroadMarketIndices.Nifty50())
    result = live.live_index(BroadMarketIndices.MidCap50())
    print(result['data'][1])
    live_chart = live.chart_data(result['data'][1]['symbol'], indices=False)
    print(live_chart)
