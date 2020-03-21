# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:00:30 2020

@author: Vaibhav Haswani
"""

import cx_Freeze as cx
import sys


base=None

if sys.platform == 'win32':
	base = "Win32GUI"
	
executables= [cx.Executable("password_gen.py",base=base,icon="icon.ico")]	

cx.setup(
		name ="Password Generator v1.0",
		options={"build_exe":{"packages":["tkinter","random"],"include_files":["icon.ico"]}},
		version="1.0",
		description="Application to generate strong passwords developed by ~ VAIBHAV HASWANI",
		executables=executables
		)