from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('38d87a58279511d99db09cf5b52f2d65')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w.detailed_status)         # 'clouds'
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)                    # {}
print(w.heat_index)              # None
print(w.clouds)                  # 75

'''
# ---------- PAID API KEY example ---------------------

config_dict = config.get_default_config_for_subscription_type('professional')
owm = OWM('your paid OWM API key', config_dict)

# What's the current humidity in Berlin (Germany) ?
one_call_object = mgr.one_call(lat=52.5244, lon=13.4105)
one_call_object.current.humidity
'''