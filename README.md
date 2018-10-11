# LammpsPostAnalysis

This code is no longer in development. For an updated version of these codes, go to https://github.com/MaginnGroup/PyLAT

For dielectric constant calculations, use the following command:
python calcDielectricConstant.py {Lammps Dump File} {Lammps Data File} {Temperature}

getatomcharges.py is called by calcDielectricConstant.py


For viscosity calculations, calcvisc (which calls lammpsio) reads in log files for multiple simulations in seperate directories. For each simulation, the cumulative integral for the pressure tensor autocorrelation function is calculated. The output is the average and standard deviation of the cumulative integrals at each timestep. 

fitvisc.py reads in the average and standard deviation and calculates the viscosity as outlined in dx.doi.org/10.1021/acs.jctc.5b00351
