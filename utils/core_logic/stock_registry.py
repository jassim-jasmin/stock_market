#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 28-09-2022 02:02 PM

@author: Mohammed Jassim
"""
from utils.data.nse_market.live import Live, BroadMarketIndices
from utils.data.nse_market.common.data_handling.filter import FilterData


class StockRegistry:
    def calculate_market_data(self, indices):
        self.market_data = Live.live_index(indices())

    def __init__(self, indices, capital: int):
        self.market_data = dict()
        self.calculate_market_data(indices)
        self.get_all_stocks_under_capital(capital)
        self.price_changes = self.price_change()

    def get_all_stocks_under_capital(self, capital: int):
        registry = []

        self.market_data = FilterData.get_stock_by_affordable(self.market_data, capital)

        for each_market_data in self.market_data["data"]:
            registry.append(each_market_data["symbol"])

        return registry

    def price_change(self):
        data = self.market_data["data"]
        price_change_results = dict()

        for each_stock in data:
            price_change_results[each_stock['symbol']] = {"change": each_stock["change"],
                                                          "percent_change": each_stock["pChange"],
                                                          "percent_change_365d": each_stock["perChange365d"],
                                                          "percent_change_30d": each_stock["perChange30d"]}

        return price_change_results

    def sort_price_change(self, price_change_key='percent_change'):
        data = dict(self.price_changes)
        sorted(data, key=lambda k: (data[k][price_change_key]),
               reverse=True)

        return data

    def sort_price_change_month(self):
        return self.sort_price_change('percent_change_30d')

    def sort_price_change_365(self):
        return self.sort_price_change('percent_change_365d')


if __name__ == '__main__':
    stock_registry = StockRegistry(BroadMarketIndices.Nifty50, 1000)
    # print(stock_registry.price_changes)
