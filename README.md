
[![Simulation](https://github.com/analogicus/jnw_spice_sky130A/actions/workflows/static.yml/badge.svg)](https://github.com/analogicus/jnw_spice_sky130A/actions/workflows/static.yml)

## Who

Carsten Wulff

## Why

Demo of running spice simulations on github actions

## How

The testbench is [sim/cs/tran.spi](sim/cs/tran.spi)

The measurements is [sim/cs/tran.meas](sim/cs/tran.meas)

The post processing is [sim/cs/tran.py](sim/cs/tran.py)

The simulation is run on every commit using github actions

## How to modify and use
1. Fork the repo 
1. Settings->Pages->Build and deployment, select github actions
1. Click About settings top right. Use your github pages webiste
1. Actions -> Enable workflows
1. Edit [sim/cs/tran.spi](sim/cs/tran.spi)
1. Wait for a minute or two before the action complets
1. Check the github pages

## Local run

Install all the tools, and the PDK. You could follow [Getting started](https://analogicus.com/aicex/started/)

Do 

``` bash
git clone git@github.com:analogicus/jnw_spice_sky130A.git
git clone git@github.com:wulffern/tech_sky130A.git
python3 -m pip install cicsim
cd jnw_spice_sky130A/sim/cs/
make test
cicsim wave output_tran/tran_SchGtKttTtVt.raw 
```

