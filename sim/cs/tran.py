#!/usr/bin/env python3
import pandas as pd
import numpy as np
import yaml
import cicsim as cs

def main(name):
  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)


  obj["a_input"] = obj["vpp_vg"]/obj["vpp_vin"]
  obj["a_input_dB"] = float(20*np.log10(obj["a_input"]))
  obj["a_gain"] = obj["vpp_vout"]/obj["vpp_vg"]
  obj["a_gain_dB"] = float(20*np.log10(obj["a_gain"]))

  cs.rawplot(name + ".raw","time","v(vg),v(vout)",ptype="same",fname=name +"_vin_vout.png")

  # Save new yaml file
  with open(yamlfile,"w") as fo:
    yaml.dump(obj,fo)
