
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Geospatial Analysis II:  buffers, cost surfaces, least cost path\n",
    "Resources:\n",
    "\n",
    "* [\n",
    "GRASS GIS overview and manual](http://grass.osgeo.org/grass74/manuals/index.html)\n",
    "*  [Recommendations](data_acquisition.html#commands)\n",
    "and [tutorial](./grass_intro.html)\n",
    "how to use GUI from the first assignment\n",
    "\n",
    "\n",
    "\n",
    "Text files with recode rules, color rules and site locations:\n",
    "\n",
    "* [noise_cats.txt](data/noise_cats.txt)\n",
    "* [friction_rules.txt](data/friction_rules.txt)\n",
    "* [friction_color.txt](data/friction_color.txt)\n",
    "* [fire_pt.json](data/fire_pt.json)\n",
    "* [lostperson.txt](data/lostperson.txt)\n",
    "\n",
    "\n",
    "### Start GRASS GIS\n",
    "In startup pannel set GIS Data Directory to path to datasets,\n",
    "for example on MS Windows, `C:\\Users\\myname\\grassdata`.\n",
    "For Project location select nc_spm_08_grass7 (North Carolina, State Plane, meters) and\n",
    "for Accessible mapset create a new mapset (called e.g. HW_buffers_cost) and\n",
    "click Start GRASS."
   ]
  }


```python
a = 6
b = 7
c = a * b
print "Answer is c"

```

    Answer is c
    


```python
import os
import sys
import subprocess
from IPython.display import Image
gisbase = subprocess.check_output(["grass", "--config", "path"]).strip()
os.environ['GISBASE'] = gisbase
sys.path.append(os.path.join(gisbase, "etc", "python"))
import grass.script as gs
import grass.script.setup as gsetup
rcfile = gsetup.init(gisbase, "/home/jovyan/grassdata", "nc_spm_08_grass7", "user1")
```


    ---------------------------------------------------------------------------

    WindowsError                              Traceback (most recent call last)

    <ipython-input-5-12b19d4e5a93> in <module>()
          3 import subprocess
          4 from IPython.display import Image
    ----> 5 gisbase = subprocess.check_output(["grass", "--config", "path"]).strip()
          6 os.environ['GISBASE'] = gisbase
          7 sys.path.append(os.path.join(gisbase, "etc", "python"))
    

    C:\Users\derekblackmon\Anaconda2\lib\subprocess.pyc in check_output(*popenargs, **kwargs)
        214     if 'stdout' in kwargs:
        215         raise ValueError('stdout argument not allowed, it will be overridden.')
    --> 216     process = Popen(stdout=PIPE, *popenargs, **kwargs)
        217     output, unused_err = process.communicate()
        218     retcode = process.poll()
    

    C:\Users\derekblackmon\Anaconda2\lib\subprocess.pyc in __init__(self, args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags)
        392                                 p2cread, p2cwrite,
        393                                 c2pread, c2pwrite,
    --> 394                                 errread, errwrite)
        395         except Exception:
        396             # Preserve original exception in case os.close raises.
    

    C:\Users\derekblackmon\Anaconda2\lib\subprocess.pyc in _execute_child(self, args, executable, preexec_fn, close_fds, cwd, env, universal_newlines, startupinfo, creationflags, shell, to_close, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite)
        642                                          env,
        643                                          cwd,
    --> 644                                          startupinfo)
        645             except pywintypes.error, e:
        646                 # Translate pywintypes.error to WindowsError, which is
    

    WindowsError: [Error 2] The system cannot find the file specified



```python
os.environ['GRASS_FONT'] = 'sans'
os.environ['GRASS_OVERWRITE'] = '1'
gs.set_raise_on_error(True)
gs.set_capture_stderr(True)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-514ee11542e5> in <module>()
          1 os.environ['GRASS_FONT'] = 'sans'
          2 os.environ['GRASS_OVERWRITE'] = '1'
    ----> 3 gs.set_raise_on_error(True)
          4 gs.set_capture_stderr(True)
    

    NameError: name 'gs' is not defined



```python
os.environ['GRASS_RENDER_IMMEDIATE'] = 'cairo'
os.environ['GRASS_RENDER_FILE_READ'] = 'TRUE'
os.environ['GRASS_LEGEND_FILE'] = 'legend.txt'
```

{
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remove MASK in case it was left over\n",
    "from previous assignment (use command `r.mask -r`).\n",
    "\n",
    "Change working directory:\n",
    "_Settings_ > _GRASS working environment_ > _Change working directory_ > select/create any directory\n",
    "or type `cd` (stands for change directory) into the GUI\n",
    "_Console_ and hit Enter:"
   ]
  }


```python
import urllib
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/noise_cats.txt", "noise_cats.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/friction_rules.txt", "friction_rules.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/friction_color.txt", "friction_color.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/fire_pt.json", "fire_pt.json")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/lostperson.txt", "lostperson.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/noise_cats.txt", "noise_cats.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/fire_pt.json", "fire_pt.json")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/friction_rules.txt", "friction_rules.txt")
urllib.urlretrieve("http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/data/lostperson.txt", "lostperson.txt")
```

Download all text files with recode rules, color rules and site locations (see above) to the selected directory. Now you can use the commands from the assignment requiring the text file without the need to specify the full path to the file.
