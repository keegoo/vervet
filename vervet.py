import json
import logging
import requests
import psutil
import re
import os
import time

# ===================================
# deal with config
# ===================================
class Config:

  DEFAULT_CONFIFG_FILE = 'config.json'
  DEFAULT_CONFIFG = {
      "description": [

        "monitor system",
        "  1: means switch it on",
        "  0: means switch it off",

        "monitor application",
        "  simply provide application names to `apps` array",
        "  vervet will capture the processes whose name includes this `name`"

      ],

      "system" : {
        "cpu_percent": 1,
        "mem_used": 1,
        "mem_free": 1,
        "bytes_sent": 0,
        "bytes_recv": 0
      },

      "apps" : ["chrome"],

      "mode" : "standalone"
    }

  def __init__(self, jsonstr=json.dumps(DEFAULT_CONFIFG)):
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

  @classmethod
  def create(cls):
    with open(cls.DEFAULT_CONFIFG_FILE, 'w') as outfile:
      json.dump(cls.DEFAULT_CONFIFG, outfile, indent=2)

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


# ===================================
# logging system data
# ===================================
class IO:
  # constant 
  MODE_POST_SERVICE = "http://127.0.0.1:3000/data"
  MODE_LOCAL_FILE = "data.csv"

  # logging
  logging.basicConfig(filename=MODE_LOCAL_FILE,level=logging.INFO)

  def __init__(self, mode="standalone"):
    self.mode = mode

  def write(self, data):
    if self.mode == "standalone":
      self.__to_file(data)
    else:
      self.__to_api(data)

  def __to_api(self, data):
    try:
      r = requests.post(self.MODE_POST_SERVICE, json=data)
      res = r.text
    except requests.exceptions.RequestException:
      res = ''
    except requests.exceptions.Timeout:
      res = ''
    return res

  def __to_file(self, data):
    logging.info(data)
    return ''


# ===================================
# get CPU/MEM/Network and Processes data
# ===================================
class Vervet:
  # ===================================
  # data format example:
  # data = {
  #   'system': {
  #     'cpu_percent':  3.1,
  #     'mem_used':     201928384,
  #     'mem_free':     201923849,
  #     'bytes_sent':   2918284,
  #     'bytes_recv':    19384748
  #   },
  #   'apps': [
  #     {
  #       'name': 'chrome',
  #       'pids': [
  #         {'n': 1234, 'v': 3.2},
  #         {'n': 1235, 'v': 3.3},
  #         {'n': 1236, 'v': 3.8}
  #       ]
  #     },
  #     {
  #       'name': 'top',
  #       'pids': [
  #         {'n': 1234, 'v': 3.2}
  #       ]
  #     }
  #   ]
  # }
  def __init__(self, config):
    self.data = {
      'system': self.get_system_data(config.system),
      'app': self.get_apps_data(config.apps)
    }

  def get_system_data(self, syscfg):
    res = {}
    if syscfg['cpu_percent'] == 1:
      res['cpu_percent'] = self.cpu_percent()
    if syscfg['mem_used'] == 1:
      res['mem_used'] = self.mem_used()
    if syscfg['mem_free'] == 1:
      res['mem_free'] = self.mem_free()
    if syscfg['bytes_sent'] == 1:
      res['bytes_sent'] = self.bytes_sent()
    if syscfg['bytes_recv'] == 1:
      res['bytes_recv'] = self.bytes_recv()

    return res

  def get_apps_data(self, apps):
    res = []
    for app in apps:
      res.append(self.app(app))
    return res

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

  # ===================================
  # apps data format example:
  # data = {
  #   'name': 'chrome',
  #   'pids': [
  #     {'n': 97, 'v': 10.1},
  #     {'n': 98, 'v': 20.4}
  #   ]
  # }
  def app(self, appname):
    regex = r'\W' + re.escape(appname) + r'\W'
    res = {
      'name': appname,
      'pids': []
    }
    for pid in psutil.pids():
      try:
        process = psutil.Process(pid)
        if re.search(regex, process.name(), re.IGNORECASE):
          res['pids'].append({'n': pid, 'v': process.cpu_percent()})
      except psutil.NoSuchProcess:
        pass  # do nothing
    return res


# ===================================
# entrance
# ===================================
def start():
  while True:
    before = time.time()

    # create default config if not found
    if not os.path.exists('config.json'):
      Config().create()

    # read config
    cfg = ""
    with open('config.json') as infile:
      cfg = Config(infile.read())

    # record data according to config
    vvt = Vervet(cfg)
    io = IO(cfg.mode)

    # write data
    io.write(vvt.data)

    interval = 6 - (time.time() - before)
    if interval > 0: 
      print('dida...')
      time.sleep(interval)


start()