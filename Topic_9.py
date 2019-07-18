#!/usr/bin/env python
# coding: utf-8

# {
#  "cells": [
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "## Geospatial Analysis II:  buffers, cost surfaces, least cost path\n",
#     "Resources:\n",
#     "\n",
#     "* [\n",
#     "GRASS GIS overview and manual](http://grass.osgeo.org/grass74/manuals/index.html)\n",
#     "*  [Recommendations](data_acquisition.html#commands)\n",
#     "and [tutorial](./grass_intro.html)\n",
#     "how to use GUI from the first assignment\n",
#     "\n",
#     "\n",
#     "\n",
#     "Text files with recode rules, color rules and site locations:\n",
#     "\n",
#     "* [noise_cats.txt](data/noise_cats.txt)\n",
#     "* [friction_rules.txt](data/friction_rules.txt)\n",
#     "* [friction_color.txt](data/friction_color.txt)\n",
#     "* [fire_pt.json](data/fire_pt.json)\n",
#     "* [lostperson.txt](data/lostperson.txt)\n",
#     "\n",
#     "\n",
#     "### Start GRASS GIS\n",
#     "In startup pannel set GIS Data Directory to path to datasets,\n",
#     "for example on MS Windows, `C:\\Users\\myname\\grassdata`.\n",
#     "For Project location select nc_spm_08_grass7 (North Carolina, State Plane, meters) and\n",
#     "for Accessible mapset create a new mapset (called e.g. HW_buffers_cost) and\n",
#     "click Start GRASS."
#    ]
#   }

# In[4]:


a = 6
b = 7
c = a * b
print "Answer is c"


# In[5]:


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


# In[6]:


os.environ['GRASS_FONT'] = 'sans'
os.environ['GRASS_OVERWRITE'] = '1'
gs.set_raise_on_error(True)
gs.set_capture_stderr(True)


# In[ ]:


os.environ['GRASS_RENDER_IMMEDIATE'] = 'cairo'
os.environ['GRASS_RENDER_FILE_READ'] = 'TRUE'
os.environ['GRASS_LEGEND_FILE'] = 'legend.txt'


# {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "Remove MASK in case it was left over\n",
#     "from previous assignment (use command `r.mask -r`).\n",
#     "\n",
#     "Change working directory:\n",
#     "_Settings_ > _GRASS working environment_ > _Change working directory_ > select/create any directory\n",
#     "or type `cd` (stands for change directory) into the GUI\n",
#     "_Console_ and hit Enter:"
#    ]
#   }

# In[ ]:


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


# Download all text files with recode rules, color rules and site locations (see above) to the selected directory. Now you can use the commands from the assignment requiring the text file without the need to specify the full path to the file.
