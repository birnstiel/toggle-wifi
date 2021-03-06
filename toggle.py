#!/usr/bin/env python3
import os
import subprocess

out = subprocess.check_output(['networksetup', '-getairportpower', 'en0'])
out = out.decode().split(':')[-1].strip().lower()

if out == 'on':
    os.system('networksetup -setairportpower en0 off')
    print('off')
else:
    os.system('networksetup -setairportpower en0 on')
    print('on')
