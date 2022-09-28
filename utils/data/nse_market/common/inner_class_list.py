#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 16-09-2022 11:11 AM

@author: Mohammed Jassim
"""


class InnerClassList:
    @staticmethod
    def inner_classes_list(cls) -> dict:
        results = dict()

        for attrname in dir(cls):
            if not attrname.startswith('_'):
                obj = getattr(cls, attrname)

                if isinstance(obj, type):
                    results[obj.name] = obj

        return results

    @staticmethod
    def inner_classes_name_list(cls) -> list:
        results = []

        for attrname in dir(cls):
            if not attrname.startswith('_'):
                obj = getattr(cls, attrname)

                if isinstance(obj, type):
                    results.append(obj.name)

        return results
