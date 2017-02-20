#!/usr/bin/env python3

import os
import shutil

dotfiles_dir = os.path.dirname(os.path.abspath(__file__))

with open('dotfiles') as f:
	for line in f:
		dotfile = line.strip()
		dotfile_home = os.path.expanduser('~/' + dotfile)
		if os.path.islink(dotfile_home):
			print('unlinking',dotfile_home)
			os.unlink(dotfile_home)
		elif os.path.exists(dotfile_home):
			print('removing', dotfile_home)
			if os.path.isdir(dotfile_home):
				shutil.rmtree(dotfile_home)
			else:
				os.remove(dotfile_home)


		dotfile_abs = os.path.join(dotfiles_dir, dotfile)
		print('linking', dotfile_abs, 'to', dotfile_home)
		os.symlink(dotfile_abs, dotfile_home)
