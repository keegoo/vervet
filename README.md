## README

#### Install

Make sure you have `python` and `pip` installed.

    shell$ pip --version
    pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)

    shell$ python --version
    Python 3.6.1

Install `requests` and `psutil` libraries with `pip`.

    pip install requests psutil

#### Run vervet.py locally

`Vervet.py` will run at `standalone` mode by defaut.

`Config.json` will be generated at first run.

If you want it to run at `server` mode, simply change `mode` to `server` in config.json.

You don't have to stop application when you did any change to config.

    python vervet.py

#### Howto find application name

Checking application name to be monitored in `Python` console:

```python
import psutil
list(map(lambda x: psutil.Process(x).name(), psutil.pids()))

# outpu will be:
#
# ['System Idle Process', 'System', 'smss.exe', 'csrss.exe', 'wininit.exe', 'csrss
# .exe', 'winlogon.exe', 'services.exe', 'lsass.exe', 'lsm.exe', 'svchost.exe', 'V
# BoxService.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'sv
# chost.exe', 'audiodg.exe', 'svchost.exe', 'svchost.exe', 'spoolsv.exe', 'svchost
# .exe', 'svchost.exe', 'svchost.exe', 'TeamViewer_Service.exe', 'sppsvc.exe', 'sv
# chost.exe', 'wmpnetwk.exe', 'WmiPrvSE.exe', 'SearchIndexer.exe', 'taskhost.exe',
#  'userinit.exe', 'taskeng.exe', 'dwm.exe', 'explorer.exe', 'VBoxTray.exe', 'WmiP
# rvSE.exe', 'svchost.exe', 'cmd.exe', 'conhost.exe', 'python.exe', 'wuauclt.exe']

```

# Road Map

  - `vervet.py` is going to be a system(CPU/MEM/Network/Process) monitoring tool running in local.
  - `vervet.py` will running in one of two modes: 1). standalone mode or 2). server mode.
  - In standalone mode, `vervet.py` will records system data locally. 
  - In server mode, `vervet.py` will post the data to a remote server(this remote server will be accomplished in another repo.).
  - `vervet.py` will be configurable at runtime in both modes.
  - `vervet.py` will be `a single file` python scripts for easy distribution.
  - `vervet.py` will be easy to use and robust.
  - should support both Linux and Windows.