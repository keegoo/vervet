import json

config = """
{
  "system" : ["CPU", "MEM", "Network"],
  "app" : ["chrome", "mdworker"],
  "mode" : "standalone"
}
"""

a = json.loads(config)

# ===================================
# deal with config
# ===================================
class Config:
  def __init__(self, jsonstr):
    if self.__valid(jsonstr):
      print("pass")
    else:
      print("failed")

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

    for key in ['system', 'app', 'mode']:
      if key not in j.keys():
        return False

    return True

  def __is_valid_mode(self, jsonstr):
    j = json.loads(jsonstr)

    if not (j['mode'] == 'standalone' or j['mode'] == 'server'):
      return False

    return True

# pseudo codes
c = Config(config)

# config.validate
# config.app
# config.system
# config.mode

# config.update(str)