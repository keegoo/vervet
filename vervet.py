import json
import logging
import requests

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
    except ValueError, e:
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
# deal with logging system data
# ===================================
class IO:
  mode = "standalone"
  logging.basicConfig(filename='data.csv',level=logging.INFO)

  @classmethod
  def write(cls):
    if cls.mode == "standalone":
      logging.info("writing to %s", cls.__name__)
      cls.__to_file()
    else:
      logging.info("writing to %s", cls.__name__)
      cls.__post()

  @classmethod
  def __post(cls):
    #
    print("post")

  @classmethod
  def __to_file(cls):
    print("write to file")

# pseudo code
# io = IO(mode)
# io.write(data) # standalone: return ''; server: return HTTP response

print(IO.write())
print(IO.mode)