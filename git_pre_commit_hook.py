#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/2/23 10:10
import os
import pathlib

home = os.path.expanduser("~")

pre_commit = """#!/usr/bin/env python
import os
import sys

make_exist = False
for cmd_path in os.environ['PATH'].split(';' if "win" in sys.platform else ":"):
    if os.path.isdir(cmd_path) and ('make.exe' in os.listdir(cmd_path) or "make" in os.listdir(cmd_path)):
        make_exist = True
if not os.path.exists("Makefile") or not make_exist:
    sys.exit()
if "check:" not in open("Makefile","r",encoding="utf8").read():
    sys.exit()
command = os.popen("make check")
command_print = "".join(command)
if command.close() != 0:
    print("make check log:")
    print(command_print)
    sys.exit(command.close())
"""


def service():
    target_dir = os.path.join(home, ".git", "hooks")
    print("mkdir at {}".format(target_dir))
    pathlib.Path(os.path.join(home, ".git", "hooks")).mkdir(parents=True, exist_ok=True)
    print("write pre-commit")
    with open(os.path.join(target_dir, "pre-commit"), "w", encoding="utf-8") as f:
        f.write(pre_commit)
    print("set default pre-commit")
    os.popen("git.exe  config --global core.hooksPath {}".format(target_dir))


if __name__ == '__main__':
    service()
