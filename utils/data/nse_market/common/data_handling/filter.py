#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 14-09-2022 02:17 PM

@author: Mohammed Jassim
"""
from copy import deepcopy


class FilterData:
    @staticmethod
    def get_stock_by_affordable(source_data: dict, limit: int):
        data: list[dict] = deepcopy(source_data["data"])
        remove_value = []

        for index, each_data in enumerate(data):
            if last_price := each_data.get("lastPrice"):
                if last_price > limit:
                    remove_value.append(each_data)

        for remove in remove_value:
            source_data["data"].remove(remove)

        return source_data
