
# JNW_SPICE_SKY130A

## Who
Carsten Wulff

## Why
 Demo of running spice simulations on github actions

## How

The testbench is [sim/cs/tran.spi](sim/cs/tran.spi)

The measurements is [sim/cs/tran.meas](sim/cs/tran.meas)

The post processing is [sim/cs/tran.py](sim/cs/tran.py)

## What 

The simulation results can be seen in [sim/cs/README](sim/cs/README.html)


## How to use it yourself

1. Fork the repo 
2. Edit [sim/cs/tran.spi](sim/cs/tran.spi)
3. Wait for a minute or two before the action complets
4. Check the github pages

## Local run

Install all the tools, and the PDK

[Getting started](https://analogicus.com/aicex/started/)

Do 

``` bash
git clone git@github.com:analogicus/jnw_spice_sky130A.git
git clone git@github.com:wulffern/tech_sky130A.git
python3 -m pip install cicsim
cd jnw_spice_sky130A/sim/cs/
make test
cicsim wave output_tran/tran_SchGtKttTtVt.raw 
```

