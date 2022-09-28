#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 28-09-2022 11:50 AM

@author: Mohammed Jassim
"""


class StopLoss:
    @staticmethod
    def get_affordable_number_of_stock(buy_price: int, stop_loss_price: int, capital: int, stop_loss_percent: int = 2):
        return round((stop_loss_percent*capital)/((buy_price-stop_loss_price)*100))


if __name__ == '__main__':
    loss = 2
    capital_price = 10000
    p = 289
    p1 = 271
    n = StopLoss.get_affordable_number_of_stock(p, p1, capital_price, loss)
    print(n)
