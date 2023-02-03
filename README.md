# README

## Use Case - Recolor and Export SVGs for Use in Presentations

- This script allows you to modify the color of a set of SVGs and export them as a high quality PNG suitable for use in popular presentation software like Google Slides, Powerpoint, or Keynote.

- This is ideal if you want to use high quality, customized graphics but do not have the ability to import SVGs to your presentation software on your operating system.


## Requirements

- Python 3
- Inkscape setup for command line functionality


## Use

- Ensure the script `recolor_export_svg.py` is in a directory containing sub-folder(s) of SVGs. 
- Modify the script to define the output color, e.g. `c = '#0165E1'`
- Define the replacement height in pixels of the PNGs (default = 2000px height)
- Save the modified script
- Run in terminal: `python3 recolor_export_svg.py`