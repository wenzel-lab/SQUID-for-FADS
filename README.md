# SQUID V1 setup for droplet sorting microfluidic chips 
This is the set-up and driver material for a custom SQUID / OCTOPI V1 (beta) setup that has been set-up in a custom arrangement as part of our microfluidic droplet sorting laboratory instrument. It is used for z-positioning (focus) of the detector arm objective, and for x/y positioning of the sorting chip on a 6cm movement range stage.

## Introduction
Squid (Simplifying Quantitive Imaging Development and Deployment) provides a full suite of hardware and software components for rapidly configuring high-performance microscopes tailored to users' applications with reduced cost, effort and turnaround time. Besides increasing accessibility of research microscopes and available microscope hours to labs, it is also designed to simplify development and dissemination of new or otherwise advanced microscopy techniques.

## Assets
- main software repo: [GitHub](https://github.com/wenzel-lab/SQUID-for-FADS) (this repo)
- CAD models/photos of assembled squids: [Google Drive](https://drive.google.com/drive/folders/1JdVp34HtERGpBCBlFX6jFDwMUdeBLCEx?usp=sharing)
- BOM for the microscope, including CAD files for CNC machining: [link](https://docs.google.com/spreadsheets/d/1WA64HySj9I7XROtTXuaRvjlbhHXRGspvoxb_20CWDR8/edit?usp=drivesdk)
- BOM for the control panel: [link](https://docs.google.com/spreadsheets/d/1z2HjibIG9PHffiDsbuzQXmvf2gSFMduHrXkPwDbcXRY/edit?usp=sharing)

## Eearly Results, Related Work and Possible Applications
Refer to our website: www.squid-imaging.org

## References
[1] Hongquan Li, Deepak Krishnamurthy, Ethan Li, Pranav Vyas, Nibha Akireddy, Chew Chai, Manu Prakash, "**Squid: Simplifying Quantitative Imaging Platform Development and Deployment**." BiorXiv [ link | [website](https://squid-imaging.org)]

For scale-free vertical tracking microscopy, check out our work at:

[2] Deepak Krishnamurthy, Hongquan Li, François Benoit du Rey, Pierre Cambournac, Adam G. Larson, Ethan Li, and Manu Prakash. "**Scale-free vertical tracking microscopy.**" Nature Methods 17, no. 10 (2020): 1040-1051. [ [link](https://www.nature.com/articles/s41592-020-0924-7) | [website](https://gravitymachine.org) ]

## Acknowledgement
The Squid software was developed with structuring inspiration from [Tempesta-RedSTED](https://github.com/jonatanalvelid/Tempesta-RedSTED).

## Software Instructions
The microscope is controled by a teensy microcontroler and a computer running Ubuntu. Instructions for using the firmware and software can be found in the respective folders.
