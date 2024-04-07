# SQUID V1 software setup for the xyz alignment and imaging stage, here used for microfluidic droplet sorting
This is the set-up and driver material for a custom SQUID (beta version) setup that has been set-up in a custom arrangement as part of our microfluidic droplet cytometry and sorting laboratory instrument. It is used for z-positioning (focus) of the detector arm objective, and for x/y positioning of the sorting chip on a 6cm movement range stage.

## Introduction
Squid (Simplifying Quantitive Imaging Development and Deployment) provides a full suite of hardware and software components for rapidly configuring high-performance microscopes tailored to users' applications with reduced cost, effort and turnaround time. Besides increasing accessibility of research microscopes and available microscope hours to labs, it is also designed to simplify development and dissemination of new or otherwise advanced microscopy techniques.

- main software repo: [GitHub](https://github.com/wenzel-lab/SQUID-for-FADS) (this repo)
- CAD models/photos of assembled squids: [Google Drive](https://drive.google.com/drive/folders/1JdVp34HtERGpBCBlFX6jFDwMUdeBLCEx?usp=sharing)
- BOM for the microscope, including CAD files for CNC machining: [link](https://docs.google.com/spreadsheets/d/1WA64HySj9I7XROtTXuaRvjlbhHXRGspvoxb_20CWDR8/edit?usp=drivesdk)
- BOM for the control panel: [link](https://docs.google.com/spreadsheets/d/1z2HjibIG9PHffiDsbuzQXmvf2gSFMduHrXkPwDbcXRY/edit?usp=sharing)

## Software Instructions
The microscope is controled by a teensy microcontroler and a computer running Ubuntu. Instructions for using the firmware and software can be found in the respective folders.

## References
Refer to the SQUID website: www.squid-imaging.org

[1] Hongquan Li, Deepak Krishnamurthy, Ethan Li, Pranav Vyas, Nibha Akireddy, Chew Chai, Manu Prakash, "**Squid: Simplifying Quantitative Imaging Platform Development and Deployment**." BiorXiv [ link | [website](https://squid-imaging.org)]
