# python code to recolor an svg
# export to png in specificed size
import re
import os
import subprocess
from glob import glob


#define replacement color
c = '#0165E1'

#define replacement height for png
h = 2000


def update_svg_color(color):

	g = glob('*.svg')

	for f in g:

		#Get SVG Elements
		svg = open(f, 'r')
		s = svg.read()
		p1 = re.split('(\<path)', s)
		p2 = re.split('(\")', p1[2], maxsplit=2)

		#New SVG
		out = '{0} <path {1} "{2}" fill="{3}" /></svg>'.format(p1[0], p2[0], p2[2], color)

		new_svg = open(f, 'w')
		new_svg.write(out)
		new_svg.close()


def svg_to_png(height=1500):

	ic = '''for file in *.svg; do inkscape "$file" --export-filename "${file%svg}png" --export-height=heightarg; done'''

	ic = ic.replace('heightarg', str(height))
	
	subprocess.call(ic, shell=True)



#Find All Folders and Loop
dirs = glob("*/", recursive=True)

for d in dirs:

	os.chdir(d)

	#Update Color of PNG
	update_svg_color(c)

	#Export SVG to PNG in Requested Size
	svg_to_png(h)

	os.chdir('..')





