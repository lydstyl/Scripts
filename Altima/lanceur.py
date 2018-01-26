#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Lanceur d'application pour gérer mon travail Altima

https://askubuntu.com/questions/141229/how-to-add-a-shell-script-to-launcher-as-shortcut

~/.local/share/applications/name.desktop

https://doc.ubuntu-fr.org/menulibre
"""


import os
# os.system('gnome-terminal -x "htop" &')
os.system('thunderbird &')
os.system('/home/lyd/eclipse_light/eclipse &')
# os.system('/opt/google/chrome/google-chrome --profile-directory=Default &')
os.system('/opt/google/chrome/google-chrome --profile-directory=Default https://papaly.com/ &')
os.system('nautilus &')
# os.system('code &')
os.system('gitkraken &')
os.system('gedit n.txt &')

# os.system('~/.dropbox-dist/dropboxd')
os.system('exit 0')