#!/usr/bin/env python

import requests
import json
import aqi

url = "https://www.purpleair.com/json?show=44089"

sensor_json = json.loads(requests.get(url).text)

pm2_5a = sensor_json["results"][0]["PM2_5Value"]

aqi_value = aqi.to_aqi([(aqi.POLLUTANT_PM25, pm2_5a)])

print (aqi_value)

if aqi_value <= 50:
    aqi_level = "Good - No health implications"
elif aqi_value <= 100:
    aqi_level = "Moderate - Some pollutants may slightly affect very few hypersensitive individuals"
elif aqi_value <= 150:
    aqi_level = "Unhealthy for sensitive groups - Healthy people may experience slight irritations and sensitive individuals will be slightly affected to a larger extent"
elif aqi_value <= 200:
    aqi_level = "Unhealthy - Sensitive individuals will experience more serious conditions. The hearts and respiratory systems of healthy people may be affected"
elif aqi_value <= 300:
    aqi_level = "Very Unhealthy - Healthy people will commonly show symptoms. People with respiratory or heart diseases will be significantly affected and will experience reduced endurance in activities"
else:
    aqi_level = "Hazardous - Healthy people will experience reduced endurance in activities and may also show noticeably strong symptoms. Healthy individuals should avoid outdoor activities"

print (aqi_level)
