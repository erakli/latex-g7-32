#!/usr/bin/env python3

__version__ = '1.1.0'

import os
import sys
from os import symlink, remove
from pathlib import Path
from shutil import copy, move
from subprocess import call
import logging
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Installer for g7-32 LaTeX style')

    parser.add_argument('-k', '--keep-existing',
                        dest='keep_existing',
                        action='store_true',
                        help='Keep existing files')

    parser.add_argument('-u', '--update-packages',
                        dest='update_packages',
                        action='store_true',
                        help='Update packages')

    parser.add_argument('-f', '--install-fonts',
                        dest='install_fonts',
                        action='store_false',
                        help='Install fonts')

    parser.add_argument('--install-lyx',
                        dest='install_lyx',
                        action='store_false',
                        help='Install LyX layouts')

    parser.add_argument('command',
                        choices=['move', 'copy', 'symlink'],
                        nargs='?',
                        default='copy',
                        help='What to do (default: %(default)s)')

    parser.add_argument('--debug',
                        dest='debug',
                        action='store_false',
                        help='Debug output')

    return parser.parse_args()


def print_paths(d, name):
    text = '%s contains:\n\t' % name
    return text + '\n\t'.join(['%s:\n\t\t%s' % (k, '\n\t\t'.join([str(x) for x in v])) for k, v in d.items()])


def main():
    args = parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.command == 'copy':
        move_function = lambda src, dst: copy(str(src), str(dst))
    elif args.command == 'symlink':
        move_function = lambda src, dst: symlink(str(src), str(dst / src.name))
    elif args.command == 'move':
        move_function = lambda src, dst: move(str(src), str(dst))
    else:
        raise ValueError('Unknown command')

    current_dir = Path(sys.argv[0]).parent.absolute()
    src_style = Path(current_dir / "../style")
    src_bibtex = Path(current_dir / "../bibtex-styles")

    texmf = Path(os.environ.get('TEXMFHOME', os.path.expanduser("~/texmf")))

    latex = texmf / "tex/latex"
    g2_105 = latex / "G2-105"
    g7_32 = latex / "G7-32"
    base = latex / "base"
    local = latex / "local"

    bibtex = texmf / "bibtex/bst/gost780u"

    if args.install_fonts:
        src_fonts = Path(current_dir / "../fonts")
        fonts = Path(os.path.expanduser("~/.fonts"))

    if args.install_lyx:
        src_lyx = Path(current_dir / "../lyx")
        lyx = Path(os.path.expanduser("~/.lyx/layouts"))

    destination_source = {
        g2_105: [src_style / "G2-105.sty"],
        g7_32: [src_style / "G7-32.sty", src_style / "cyrtimespatched.sty", src_style / "GostBase.clo",
                src_style / "gosttitleGost7-32.sty", src_style / "gosttitleGostRV15-110.sty"],
        base: [src_style / "G7-32.cls"],
        local: list(src_style.glob("local-*.sty")) + list(src_style.glob("*.inc.tex")),
        bibtex: [src_bibtex / "gost780u.bst"],
        lyx: list(src_lyx.glob("layouts/*")),
    }

    if args.install_fonts:
        destination_source[fonts] = [src_fonts]

    logging.debug(print_paths(destination_source, 'destination_source'))
    for destination, source in destination_source.items():
        logging.debug("creating destination {}".format(destination))
        destination.mkdir(parents=True, exist_ok=True)

        logging.debug("copying to {}".format(destination))
        for f in source:
            logging.debug("source is {}".format(f))
            if not args.keep_existing:
                try:
                    logging.debug("trying to remove {}".format(destination / f.name))
                    (destination / f).unlink()
                except FileNotFoundError:
                    pass
            move_function(f.absolute(), destination.absolute())

    if args.update_packages:
        try:
            call("texhash", shell=True)
        except:
            pass

    if args.install_fonts:
        try:
            call('fc-cache -f -v', shell=True)
            call('luaotfload-tool -u -f', shell=True)
        except:
            pass


if __name__ == '__main__':
    main()
