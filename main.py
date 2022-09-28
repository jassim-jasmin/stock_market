#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 28-09-2022 03:24 PM

@author: Mohammed Jassim
"""
from utils.core_logic.stock_registry import StockRegistry, BroadMarketIndices


if __name__ == '__main__':
    capital = 1000
    loss_percent = 2
    stock_registry = StockRegistry(BroadMarketIndices.Nifty50, capital)
    stocks_under_budget = stock_registry.sort_price_change()
    for stock, changes in stocks_under_budget.items():
        print(stock, changes)