#!/usr/bin/env python3
# -*- mode: python -*-
# -*- coding: utf-8 -*-

import urllib.request
import json

class Meteo:
    
    # Constructeur
    def __init__(self):
        
        
        serviceMeteo = 'http://www.prevision-meteo.ch/services/json/paris'
            
        html_meteo = urllib.request.urlopen(serviceMeteo)
        donnees_meteo = html_meteo.read()
            
        self.arbre_meteo = json.loads(donnees_meteo.decode())
        
    # Methodes infos localite    
    def getCityName(self):
        #Nom de la localite
        return str(self.arbre_meteo['city_info']['name'])
    
    def getCityLatitude(self):
        # Latitude de la localite
        return str(self.arbre_meteo['city_info']['latitude'])
    
    def getCityLongitude(self):
        # Longitude de la localite
        return str(self.arbre_meteo['city_info']['longitude'])
    
    def getCityElevation(self):
        # Altitude de la localite
        return str(self.arbre_meteo['city_info']['elevation'])
    
    def getCitySunrise(self):
        # Heure de lever du soleil
        return str(self.arbre_meteo['city_info']['sunrise'])
    
    def getCitySunset(self):
        # Heure de coucher du soleil
        return str(self.arbre_meteo['city_info']['sunset'])
    
    # Methodes conditions actuelles
    def getCurrentDate(self):
        # Date actuelle
        return str(self.arbre_meteo['current_condition']['date'])
    
    def getCurrentHour(self):
        # Heure actuelle
        return str(self.arbre_meteo['current_condition']['hour'])
    
    def getCurrentTmp(self):
        # Temperature actuelle
        return str(self.arbre_meteo['current_condition']['tmp'])
    
    def getCurrentWindSpeed(self):
        # Vitesse actuelle du vent 
        return str(self.arbre_meteo['current_condition']['wnd_spd'])
    
    def getCurrentWindDirection(self):
        # Direction actuelle du vent 
        return str(self.arbre_meteo['current_condition']['wnd_spd'])
    
    def getCurrentPressure(self):
        # Direction actuelle du vent 
        return str(self.arbre_meteo['current_condition']['pressure'])
    
    def getCurrentHumidity(self):
        # Humidite actuelle
        return str(self.arbre_meteo['current_condition']['humidity'])
    
    def getCurrentCondition(self):
        # Conditions actuelles
        return str(self.arbre_meteo['current_condition']['condition'])
    
    def getCurrentIcon(self):
        # Icone actuelle
        return str(self.arbre_meteo['current_condition']['icon'])
    
    def getCurrentIconBig(self):
        # Icone actuelle
        return str(self.arbre_meteo['current_condition']['icon_big'])
    
    # Methodes previsions J0
    def getForecast0Date(self):
        # Date J0
        return str(self.arbre_meteo['fcst_day_0']['date'])
    
    def getForecast0Day(self):
        # Jour J0
        return str(self.arbre_meteo['fcst_day_0']['day_short'])
    
    def getForecast0Tmin(self):
        # Temperature minimum J0
        return str(self.arbre_meteo['fcst_day_0']['tmin'])
    
    def getForecast0Tmax(self):
        # Temperature maximum J0
        return str(self.arbre_meteo['fcst_day_0']['tmax'])
    
    def getForecast0Condition(self):
        # Conditions J0
        return str(self.arbre_meteo['fcst_day_0']['condition'])
    
    # Previsions J0 à 8H
    def getForecast0Icon08(self):
        # Icone J0 à 8H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['8H00']['ICON'])
    
    def getForecast0Temp08(self):
        # Temperature J0 à 8H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['8H00']['TMP2m'])
    
    def getForecast0Humidity08(self):
        # Humidite J0 à 8H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['8H00']['RH2m'])
    
    def getForecast0Pressure08(self):
        # Humidite J0 à 8H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['8H00']['PRMSL'])
    
    def getForecast0WindSpeed08(self):
        # Humidite J0 à 8H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['8H00']['WNDSPD10m'])
    
    
    # Previsions J0 à 14H
    def getForecast0Icon14(self):
        # Icone J0 à 14H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['14H00']['ICON'])
        
    def getForecast0Temp14(self):
        # Temperature J0 à 14H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['14H00']['TMP2m'])
        
    def getForecast0Humidity14(self):
        # Humidite J0 à 14H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['14H00']['RH2m'])
        
    def getForecast0Pressure14(self):
        # Humidite J0 à 14H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['14H00']['PRMSL'])
        
    def getForecast0WindSpeed14(self):
        # Humidite J0 à 14H
        return str(self.arbre_meteo['fcst_day_0']['hourly_data']['14H00']['WNDSPD10m'])
    
    
    
    
    # Methodes previsions J1
    def getForecast1Date(self):
        # Date J1
        return str(self.arbre_meteo['fcst_day_1']['date'])
    
    def getForecast1Day(self):
        # Jour J1
        return str(self.arbre_meteo['fcst_day_1']['day_short'])
    
    def getForecast1Tmin(self):
        # Temperature minimum J1
        return str(self.arbre_meteo['fcst_day_1']['tmin'])
    
    def getForecast1Tmax(self):
        # Temperature maximum J1
        return str(self.arbre_meteo['fcst_day_1']['tmax'])
    
    def getForecast1Condition(self):
        # Conditions J1
        return str(self.arbre_meteo['fcst_day_1']['condition'])
    
    # Previsions J1 à 8H
    def getForecast1Icon08(self):
        # Icone J1 à 8H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['8H00']['ICON'])
    
    def getForecast1Temp08(self):
        # TemperatureJ1 à 8H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['8H00']['TMP2m'])
    
    def getForecast1Humidity08(self):
        # Humidite J1 à 8H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['8H00']['RH2m'])
    
    def getForecast1Pressure08(self):
        # Humidite J1 à 8H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['8H00']['PRMSL'])
    
    def getForecast1WindSpeed08(self):
        # Humidite J1 à 8H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['8H00']['WNDSPD10m'])
    
    
    # Previsions J1 à 14H
    def getForecast1Icon14(self):
        # Icone J1 à 14H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['14H00']['ICON'])
        
    def getForecast1Temp14(self):
        # Temperature J1 à 14H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['14H00']['TMP2m'])
        
    def getForecast1Humidity14(self):
        # Humidite J1 à 14H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['14H00']['RH2m'])
        
    def getForecast1Pressure14(self):
        # Humidite J1 à 14H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['14H00']['PRMSL'])
        
    def getForecast1WindSpeed14(self):
        # Humidite J1 à 14H
        return str(self.arbre_meteo['fcst_day_1']['hourly_data']['14H00']['WNDSPD10m'])
    
    
    
    # Methodes previsions J2
    def getForecast2Date(self):
        # Date J2
        return str(self.arbre_meteo['fcst_day_2']['date'])
    
    def getForecast2Day(self):
        # Jour J2
        return str(self.arbre_meteo['fcst_day_2']['day_short'])
    
    def getForecast2Tmin(self):
        # Temperature minimum J2
        return str(self.arbre_meteo['fcst_day_2']['tmin'])
    
    def getForecast2Tmax(self):
        # Temperature maximum J2
        return str(self.arbre_meteo['fcst_day_2']['tmax'])
    
    def getForecast2Condition(self):
        # Conditions J2
        return str(self.arbre_meteo['fcst_day_2']['condition'])
    
    # Previsions J2 à 8H
    def getForecast2Icon08(self):
        # Icone J2 à 8H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['8H00']['ICON'])
    
    def getForecast2Temp08(self):
        # Temperature J2 à 8H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['8H00']['TMP2m'])
    
    def getForecast2Humidity08(self):
        # Humidite J2 à 8H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['8H00']['RH2m'])
    
    def getForecast2Pressure08(self):
        # Humidite J2 à 8H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['8H00']['PRMSL'])
    
    def getForecast2WindSpeed08(self):
        # Humidite J2 à 8H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['8H00']['WNDSPD10m'])
    
    
    # Previsions J2 à 14H
    def getForecast2Icon14(self):
        # Icone J2 à 14H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['14H00']['ICON'])
        
    def getForecast2Temp14(self):
        # Temperature J2 à 14H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['14H00']['TMP2m'])
        
    def getForecast2Humidity14(self):
        # Humidite J2 à 14H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['14H00']['RH2m'])
        
    def getForecast2Pressure14(self):
        # Humidite J2 à 14H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['14H00']['PRMSL'])
        
    def getForecast2WindSpeed14(self):
        # Humidite J2 à 14H
        return str(self.arbre_meteo['fcst_day_2']['hourly_data']['14H00']['WNDSPD10m'])
    
    
    
    # Methodes previsions J3
    def getForecast3Date(self):
        # Date J3
        return str(self.arbre_meteo['fcst_day_3']['date'])
    
    def getForecast3Day(self):
        # Jour J3
        return str(self.arbre_meteo['fcst_day_3']['day_short'])
    
    def getForecast3Tmin(self):
        # Temperature minimum J3
        return str(self.arbre_meteo['fcst_day_3']['tmin'])
    
    def getForecast3Tmax(self):
        # Temperature maximum J3
        return str(self.arbre_meteo['fcst_day_3']['tmax'])
    
    def getForecast3Condition(self):
        # Conditions J3
        return str(self.arbre_meteo['fcst_day_3']['condition'])
    
    # Previsions J3 à 8H
    def getForecast3Icon08(self):
        # Icone J3 à 8H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['8H00']['ICON'])
    
    def getForecast3Temp08(self):
        # Temperature J3 à 8H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['8H00']['TMP2m'])
    
    def getForecast3Humidity08(self):
        # Humidite J3 à 8H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['8H00']['RH2m'])
    
    def getForecast3Pressure08(self):
        # Humidite J3 à 8H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['8H00']['PRMSL'])
    
    def getForecast3WindSpeed08(self):
        # Humidite J3 à 8H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['8H00']['WNDSPD10m'])
    
    
    # Previsions J3 à 14H
    def getForecast3Icon14(self):
        # Icone J3 à 14H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['14H00']['ICON'])
        
    def getForecast3Temp14(self):
        # Temperature J3 à 14H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['14H00']['TMP2m'])
        
    def getForecast3Humidity14(self):
        # Humidite J3 à 14H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['14H00']['RH2m'])
        
    def getForecast3Pressure14(self):
        # Humidite J3 à 14H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['14H00']['PRMSL'])
        
    def getForecast3WindSpeed14(self):
        # Humidite J3 à 14H
        return str(self.arbre_meteo['fcst_day_3']['hourly_data']['14H00']['WNDSPD10m'])
    
    