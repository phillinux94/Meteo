#!/usr/bin/env python3
# -*- mode: python -*-
# -*- coding: utf-8 -*-

from Meteo import Meteo

t = Meteo('Paris')

print(t.getCityName())
print(t.getCitySunrise())
print(t.getCurrentWindSpeed())
print(t.getCurrentHumidity())
print(t.getForecast1Pressure08())