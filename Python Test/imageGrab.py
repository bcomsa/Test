#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dictionary.py
#  
#  Copyright 2014 Vu Quang Tam <vuquangtam@Acer-Aspire-5830G>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import autopy
import os
import time
 
def screenGrab():
	autopy.mouse.move(518,479)
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON);time.sleep(0.5)
	autopy.mouse.move(521,664)
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON);time.sleep(0.5)
	autopy.mouse.move(522,678)
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON);time.sleep(0.5)
	autopy.mouse.move(790,70)
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON);time.sleep(0.5)
	autopy.mouse.move(515,648)
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON);time.sleep(0.5)
	time.sleep(2)
	box = ((200,275),(640,480))
	im = autopy.bitmap.capture_screen(box)
	im.save(os.getcwd() + '//full_snap__' + str(int(time.time())) + '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()


