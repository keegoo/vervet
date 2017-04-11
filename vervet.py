import json
import logging
import requests
import psutil
import re

config = """
{
  "system" : ["CPU", "MEM", "Network"],
  "apps" : ["chrome", "mdworker"],
  "mode" : "standalone"
}
"""

# ===================================
# deal with config
# ===================================
class Config:
  def __init__(self, jsonstr):
    if self.__valid(jsonstr):
      j = json.loads(jsonstr)
      self.json = jsonstr
      self.apps = j['apps']
      self.system = j['system']
      self.mode = j['mode']
    else:
      print("failed")

  def update(self, newjson):
    if not newjson == self.json:
      print("reload")
      self.__init__(newjson)

  def __valid(self, jsonstr):
    if (
        self.__is_valid_json(jsonstr) and
        self.__is_valid_setting(jsonstr) and
        self.__is_valid_mode(jsonstr)
      ):
      return True
    else:
      return False

  def __is_valid_json(self, jsonstr):
    try:
      j = json.loads(jsonstr)
    except ValueError:
      return False

    return True

  def __is_valid_setting(self, jsonstr):
    j = json.loads(jsonstr)

    for key in ['system', 'apps', 'mode']:
      if key not in j.keys():
        return False

    return True

  def __is_valid_mode(self, jsonstr):
    j = json.loads(jsonstr)

    if not (j['mode'] == 'standalone' or j['mode'] == 'server'):
      return False

    return True

c = Config(config)
print(c.apps)
print(c.system)
print(c.mode)
c.update(config + ' ')

# ===================================
# logging system data
# ===================================
class IO:
  # constant 
  MODE_POST_SERVICE = "http://127.0.0.1:3000/data"
  MODE_LOCAL_FILE = "data.csv"

  # class variable
  mode = "standalone"

  # logging
  logging.basicConfig(filename=MODE_LOCAL_FILE,level=logging.INFO)

  @classmethod
  def write(cls, data):
    if cls.mode == "standalone":
      logging.info("writing to %s", cls.__name__)
      cls.__to_file(data)
    else:
      logging.info("writing to %s", cls.__name__)
      cls.__post(data)

  @classmethod
  def __post(cls, data):
    try:
      r = requests.post(cls.MODE_POST_SERVICE, json=data)
      res = r.text
    except requests.exceptions.RequestException:
      res = ''
    except requests.exceptions.Timeout:
      res = ''
    return res

  @classmethod
  def __to_file(cls, data):
    logging.info(data)
    return ''

print(IO.mode)
IO.mode = "server"
print(IO.write({"a":1, "b":2}))

# ===================================
# get CPU/MEM/Network and Processes data
# ===================================
class Vervet:

  def __init__(self):
    pass

  def cpu_percent(self):
    return psutil.cpu_percent()

  def mem_used(self):
    return psutil.virtual_memory().used

  def mem_free(self):
    return psutil.virtual_memory().free

  def bytes_sent(self):
    return psutil.net_io_counters().bytes_sent

  def bytes_recv(self):
    return psutil.net_io_counters().bytes_recv

  def app(self, appname):
    regex = r'\W' + re.escape(appname) + r'\W'
    res = []
    for pid in psutil.pids():
      try:
        process = psutil.Process(pid)
        if re.search(regex, process.name(), re.IGNORECASE):
          res.append(process.cpu_percent())
      except psutil.NoSuchProcess:
        pass  # do nothing
    return res
      
v = Vervet()
print(v.cpu_percent())
print(v.mem_used())
print(v.mem_free())
print(v.bytes_sent())
print(v.bytes_recv())