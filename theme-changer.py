#!/data/data/.termux/usr/bin/python3

# version 1.0
# this file has been created as a shortcut

import sys
import json
import requests
from shutil import copyfile
from os import path, system

# ---------- variables ----------

theme_json = json.load(open('themes.json')).get("themes-urls", {})
selected_theme = sys.argv[2]
select_theme = theme_json.get(selected_theme, "")

scheme_path = path.expanduser("~/.termux/colorschemes") # the function uses it to set themes

# ---------- theme install ----------

def install_theme(scheme_path_install):
  try:
    response = requests.get(select_theme)
    if response.status_code == 200:
      with open(scheme_path_install, 'wb') as file:
        file.write(response.text.encode("utf-8"))
        print("\033[33mInstalling theme...")
      print("\033[32mtheme successully installed")
    else:
      print("theme not found")
  except Exception as e:
    print(f"error {e}")
    
# ---------- set theme ----------

def set_theme(scheme_name):
  src_path = path.join(scheme_path, f"{scheme_name}.properties")
  dst_path = path.expanduser("~/.termux/colors.properties") 
  try:
    copyfile(src_path, dst_path)
    system("termux-reload-settings")
  except FileNotFoundError:
    print("\033[31mError: scheme file not found")

# ---------- argument function ----------

def main():
  if len(sys.argv) < 3:
    print("\033[33mUsage: python horse.py set <color-scheme>\n but if you not installed colorschemes\npython horse.py install <colors-cheme>")
    sys.exit(1)

  command = sys.argv[1]
  scheme_name = sys.argv[2]
  scheme_path_install = path.join(scheme_path, f"{scheme_name}.properties")
 
  if command == "install":
    install_theme(scheme_path_install)
  elif command == "set":
    set_theme(scheme_name)
  else:
    print("command not found")
# ---------- name main function ----------

if __name__ == "__main__":
  main()
