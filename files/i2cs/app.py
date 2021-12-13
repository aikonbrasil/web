comment = """
The Creative Commons Attribution 4.0 International license (CC BY 4.0)
shall be used by the Finnish Meteorological Institute's open data service.
The license shall apply to the FMI's, the Finnish Transport Agency's,
and the Radiation and Nuclear Safety Authority's open data sets as well
as air quality data sets that are stored in the open data web-service.

License:

https://creativecommons.org/licenses/by/4.0/

More info at: https://en.ilmatieteenlaitos.fi/open-data-licence
"""


# In[7]:


# Part 1. Fetching data from external API

import datetime
from datetime import datetime as dt

from fmiopendata.wfs import download_stored_query
import json


# In[8]:


def get_weather_observations(start, end, bbox):
    start_str = start.isoformat(timespec="seconds") + "Z"
    end_str = end.isoformat(timespec="seconds") + "Z"

    query = "fmi::observations::weather::multipointcoverage"

    res = download_stored_query(query,
                                args=[f"bbox={bbox}",
                                      "starttime=" + start_str,
                                      "endtime=" + end_str])
    return res.data


def reorganize_samples(observations_data):
    samples = dict()
    for time, data in observations_data.items():
        for location, measurements in data.items():
            if location not in samples:
                samples[location] = []
            samples[location].append([time, measurements])
    return samples


def sort_samples(samples):
    def get_first_element(x):
        return x[0]

    for k, v in samples.items():
        v.sort(key=get_first_element)


def write_json_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


# In[ ]:





# In[9]:


import meteocalc
import yaml


def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    # JSON format preserves data types
    print("First 10 loaded records:")
    print(data[0:10])
    return data


def prepare_dew_point(record):
    temp = meteocalc.Temp(record['air_temperature_deg_c'], 'c')
    rh = record['relative_humidity']
    record['due_point_deg_c'] = meteocalc.dew_point(temp, rh).c


def prepare_feels_like(record):
    temp = meteocalc.Temp(record['air_temperature_deg_c'], 'c')
    rh = record['relative_humidity']
    wind_speed = record['wind_m_per_s']
    record['feels_like_deg_c'] = meteocalc.feels_like(temp, rh, wind_speed).c


def save_as_yaml(data, filename):
    with open(filename, "w") as f:
        yaml.dump(data, f)


# In[10]:


from yaml import Loader, Dumper
import sys
import requests


def fetch_payload_data(payload_server, payload_id):
    response = requests.get(f"{payload_server}/{payload_id}.yml")
    return yaml.load(response.text, Loader)


# In[14]:


def main():
    payload_server = "http://127.0.0.1:3080"
    payload_id = 1
    import sys
    if len(sys.argv) > 2:
        payload_server = sys.argv[1]
        payload_id = int(sys.argv[2])

    solver_configuration = fetch_payload_data(payload_server, payload_id)
    print(solver_configuration)

    bbox = solver_configuration["bbox"]
    location = solver_configuration["location"]
    start_time = solver_configuration["start"]
    duration = solver_configuration["duration"]

    end = start_time.replace(tzinfo=None) + datetime.timedelta(hours=duration)
    data_lpr = []

    for i in range(duration):
        start = end - datetime.timedelta(hours=1)

        observations_data = get_weather_observations(start, end, bbox)

        samples = reorganize_samples(observations_data)

        sort_samples(samples)

        if location in samples:
            for time, measurement in samples[location]:
                unix_time = int((time-dt(1970, 1, 1)).total_seconds())
                data_lpr.append({"time": unix_time,
                                 "air_temperature_deg_c":
                                 measurement['Air temperature']['value'],
                                 "relative_humidity":
                                 measurement['Relative humidity']['value'],
                                 "wind_m_per_s":
                                 measurement['Wind speed']['value'],
                                 "wind_direction_deg":
                                 measurement['Wind direction']['value']
                                 })
        end = start
    write_json_file(data_lpr, "data.json")
    data = load_data("data.json")
    for r in data:
        prepare_dew_point(r)
        prepare_feels_like(r)
    save_as_yaml(data, "/root/shared/results/data.yaml")


# In[16]:


main()

