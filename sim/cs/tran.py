#!/usr/bin/env python3
import pandas as pd
import numpy as np
import yaml
import cicsim as cs
import random
import os
import string

def main(name):
  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)


  obj["a_input"] = obj["vpp_vg"]/obj["vpp_vin"]
  obj["a_input_dB"] = float(20*np.log10(obj["a_input"]))
  obj["a_gain"] = obj["vpp_vout"]/obj["vpp_vg"]
  obj["a_gain_dB"] = float(20*np.log10(obj["a_gain"]))

  #- use a random string to fool browser caches
  rss = ""
  if(os.environ.get("CIC_RANDOM_PLOTNAME")):
    rss = "_" + "".join(random.choice(string.ascii_uppercase+string.digits) for _ in range(5))


  fname = name + rss + "_vin_vout.png"
  print(f"Saving {fname}")
  cs.rawplot(name + ".raw","time","v(vg),v(vout)",ptype="same",fname=fname)

  # Save new yaml file
  with open(yamlfile,"w") as fo:
    yaml.dump(obj,fo)
