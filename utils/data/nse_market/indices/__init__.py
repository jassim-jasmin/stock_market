#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 14-09-2022 11:25 AM

@author: Mohammed Jassim
"""
from utils.data.nse_market.indices.broad_market import BroadMarketIndices
from utils.data.nse_market.indices.sectoral import Sectoral, API
from utils.data.nse_market.common.inner_class_list import InnerClassList


def indices() -> dict:
    indices_objects = dict()

    indices_objects[Sectoral.name] = InnerClassList.inner_classes_list(Sectoral)
    indices_objects[BroadMarketIndices.name] = InnerClassList.inner_classes_list(BroadMarketIndices)
    indices_objects['all'] = {**indices_objects[Sectoral.name], **indices_objects[BroadMarketIndices.name]}

    return indices_objects


if __name__ == '__main__':
    objects = indices()

    print(objects)