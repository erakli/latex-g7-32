#!/usr/bin/env python3
"""Installer for g7-32 LaTeX style

Usage:
    install.py ([move] | copy | symlink) ([--keep-existing] | --overwrite-existing) ([--update-packages] | --no-update-packages)
    install.py --help
    install.py --version

Options:
    -k --keep-existing       Keep existing files
    -o --overwrite-existing  Overwrite existing files
    -u --update-packages     Update packages
    -n --no-update-packages  Don't update packages
    -h --help                Show this screen
    --version                Show version
"""
__version__ = '1.1.0'

import os
import sys
from os import symlink, remove
from pathlib import Path
from shutil import copyfile as copy, move
from docopt import docopt
from subprocess import call
import logging
# logging.basicConfig(level=logging.DEBUG)

def main():
    args = docopt(__doc__, version=__version__)

    current_dir = Path(sys.argv[0]).parent.absolute()
    src_style = Path(current_dir/"../tex")
    src_bibtex = Path(current_dir/"../bibtex-styles")
    src_lyx = Path(current_dir/"../lyx")
    
    texmf = Path(os.environ.get('TEXMFHOME', os.path.expanduser("~/texmf")))
    bibtex = texmf/"bibtex/bst/gost780u"
    latex = texmf/"tex/latex"
    g2_105 = latex/"G2-105"
    g7_32 = latex/"G7-32"
    base = latex/"base"
    local = latex/"local"

    lyx = Path(os.path.expanduser("~/.lyx/layouts"))

    move_function = lambda src, dst: move(str(src), str(dst))
    if args['copy']:
        move_function = lambda src, dst: copy(str(src), str(dst))
    elif args['symlink']:
        move_function = lambda src, dst: symlink(str(src), str(dst/src.name))

    destination_source = {
        g2_105: [src_style/"G2-105.sty"],
        g7_32: [src_style/"G7-32.sty", src_style/"cyrtimespatched.sty", src_style/"GostBase.clo"],
        base: [src_style/"G7-32.cls"],
        local: list(src_style.glob("local-*.sty")) + list(src_style.glob("*.inc.tex")),
        bibtex: [src_bibtex/"gost780u.bst"],
        lyx: src_lyx.glob("layouts/*"),
    }
    
    logging.debug("dict {}".format(destination_source))
    for destination, source in destination_source.items():
        logging.debug("creating destination {}".format(destination))
        destination.mkdir(parents=True, exist_ok=True)

        logging.debug("copying to {}".format(destination))
        for f in source:
            if args['--overwrite-existing']:
                try:
                    logging.debug("trying to remove {}".format(destination/f.name))
                    (destination/f).unlink()
                except FileNotFoundError:
                    pass
            move_function(f.absolute(), destination.absolute())

    if args['--update-packages']:
        try:
            call("texhash", shell=True)
        except:
            pass

if __name__ == '__main__':
    main()