#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 16-09-2022 10:40 AM

@author: Mohammed Jassim
"""
from datetime import datetime, timedelta, date


def live_cache(app_name):
    """Caches the output for time_out specified. This is done in order to
    prevent hitting live quote requests to NSE too frequently. This wrapper
    will fetch the quote/live result first time and return the same result for
    any calls within 'time_out' seconds.

    Logic:
        key = concat of args
        try:
            cached_value = self._cache[key]
            if now - self._cache['tstamp'] < time_out
                return cached_value['value']
        except AttributeError: # _cache attribute has not been created yet
            self._cache = {}
        finally:
            val = fetch-new-value
            new_value = {'tstamp': now, 'value': val}
            self._cache[key] = new_value
            return val

    """
    def wrapper(self, *args, **kwargs):
        """Wrapper function which calls the function only after the timeout,
        otherwise returns value from the cache.

        """
        # Get key by just concating the list of args and kwargs values and hope
        # that it does not break the code :P
        inputs =  [str(a) for a in args] + [str(kwargs[k]) for k in kwargs]
        key = app_name.__name__ + '-'.join(inputs)
        now = datetime.now()
        time_out = self.time_out
        try:
            cache_obj = self._cache[key]
            if now - cache_obj['timestamp'] < timedelta(seconds=time_out):
                print("caching..........................................")
                return cache_obj['value']
        except:
            self._cache = {}
        value = app_name(self, *args, **kwargs)
        self._cache[key] = {'value': value, 'timestamp': now}
        return value

    return wrapper
