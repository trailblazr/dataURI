#!./venv/bin/python
# -*- coding: utf-8 -*-
"""
TOOL TO CONVERT ANY KIND OF DATA INTO A PROPER DATA-URI

 AUTHOR: blazr
 E-MAIL: trailblazr@noxymo.com
CREATED: JAN 2026
UPDATED: JAN 2026
"""

import os
import sys
import argparse
import datetime

from argparse import RawTextHelpFormatter
from datauri import DataURI

APP_VERSION = "1.0.0"

# BAIL ON WRONG PYTHON VERSION
if not sys.version_info.major == 3 and sys.version_info.minor >= 12:
    print("dataURI: Python 3.12 or higher is required.")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

global APP_DEBUG
APP_DEBUG = False
# https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Big&text=dataURI
APP_LOGO = """
      _       _        _    _ _____  _____ 
     | |     | |      | |  | |  __ \\|_   _|
   __| | __ _| |_ __ _| |  | | |__) | | |  
  / _` |/ _` | __/ _` | |  | |  _  /  | |  
 | (_| | (_| | || (_| | |__| | | \\ \\ _| |_ 
  \\__,_|\\__,_|\\__\\__,_|\\____/|_|  \\_\\_____|  \033[9{}mv{}\033[0m
                                            
  {}
 """
APP_COPYRIGHT_YEAR_START = 2026
APP_COPYRIGHT_YEAR_CURRENT = datetime.datetime.now().year
if APP_COPYRIGHT_YEAR_START == APP_COPYRIGHT_YEAR_CURRENT:
    APP_COPYRIGHT_YEARS = f"{APP_COPYRIGHT_YEAR_CURRENT}"
else:
    APP_COPYRIGHT_YEARS = f"{APP_COPYRIGHT_YEAR_START}-{APP_COPYRIGHT_YEAR_CURRENT}"
APP_COPYRIGHT_NOTICE = (
    f"A new dataURI in seconds — copyright (c) {APP_COPYRIGHT_YEARS}, blazr"
)
# DETERMINE LOGO COLOR FROM APP_VERSION
APP_LOGO_COLOR = 1
try:
    version = APP_VERSION.split('.')
    APP_LOGO_COLOR = 1 + (int(version[0])+int(version[1])+int(version[2]) % 7)
except:
    pass

APP_FILE_NAME = os.path.basename( os.path.abspath(__file__) )
APP_PATH = os.path.dirname(os.path.abspath(__file__))

# HELPER TO COLORIZE PRINT OUTPUT
class TerminalColor:
    def __init__(self):
        pass
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[98m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    BLINKOFF = "\033[25m"


def str_styled( text="",color="clear",style="plain",blink: str = None):
    color = color.lower()
    style = style.lower()
    if blink:
        blink = blink.lower()
    if color == "red":
        text = TerminalColor.RED + text
    if color == "green":
        text = TerminalColor.GREEN + text
    if color == "yellow":
        text = TerminalColor.YELLOW + text
    if color == "blue":
        text = TerminalColor.BLUE + text
    if color == "magenta":
        text = TerminalColor.MAGENTA + text
    if color == "black":
        text = TerminalColor.BLACK + text
    if color == "white":
        text = TerminalColor.WHITE + text
    if color == "cyan":
        text = TerminalColor.CYAN + text
    if style == "bold":
        text = TerminalColor.BOLD + text
    if style == "underlined":
        text = TerminalColor.UNDERLINE + text
    if blink == "blink":
        text = TerminalColor.BLINK + text
    text = text + TerminalColor.ENDC
    return text

def print_styled( text="",color="clear",style="plain",blink="none",should_log=True,log_colorized=True,end="\n",prefix="",debug=None):
    if debug is not None:
        if not debug:  # SKIP THIS IF WE DO NOT DEBUG STUFF
            return
    if not should_log:
        return
    if log_colorized:
        text = str_styled(text,color,style,blink)
        if prefix:
            text = f"{prefix}{text}"
    print(text,end=end,flush=True)

def print_logo():
    print_styled( APP_LOGO.format(APP_LOGO_COLOR,APP_VERSION,APP_COPYRIGHT_NOTICE), "white" )


def parse_cmdline_arguments() -> tuple: 
    # PARSE INPUT ARGUMENTS
    examples = f"\033[9{APP_LOGO_COLOR}mUSAGE EXAMPLES:\033[0m\n" 
    examples += f"{APP_FILE_NAME} --file-input funny_meme.png\n"
    examples += f"{APP_FILE_NAME} -i funny_meme.jpg -o funny_out.html -f\n"
    examples += f"{APP_FILE_NAME} -i funny_meme.png --file-output funny_out.html -q\n"
    examples += ' '
    version_str = f"\033[9{APP_LOGO_COLOR}mv{APP_VERSION}\033[0m"
    logo = APP_LOGO.format(APP_LOGO_COLOR,APP_VERSION,APP_COPYRIGHT_NOTICE)
    parser = argparse.ArgumentParser(
        description=f"\n{logo}",
        epilog=examples,
        formatter_class=RawTextHelpFormatter,
        exit_on_error=False
        )
    # mandatory = parser.add_mutually_exclusive_group( required=True )
    mandatory = parser.add_argument_group("Mandatory")
    optional = parser.add_argument_group("Optional")
    mandatory.add_argument('-i', '--file-input', dest='file_input', metavar='<FILE IN>', required=True, help=f"path to input file")
    optional.add_argument('-o', '--file-output', dest='file_output', metavar='<FILE OUT>', required=False, help='path to output HTML file (optional)')
    optional.add_argument('-f', '--force', dest='force_write', action='store_true', required=False, help='overwrite existing output files without warning')
    optional.add_argument('-q', '--quiet', dest='quiet', action='store_true', required=False, help='do not print unnecessary stuff to standard out')

    # DEFAULTS
    parser.set_defaults( file_input=None )
    parser.set_defaults( file_output=None )
    parser.set_defaults( force_write=False )
    parser.set_defaults( quiet=False )
    try:
        args = parser.parse_args()
        if not args.quiet:
            print_logo()
        return (
            args.file_input, 
            args.file_output,
            args.force_write,
            args.quiet
            )
    except Exception as e:
        print_logo()
        print_styled( f"WELCOME.", "blue", end="\n" )
        exit_with_code( 1, f"ERROR: {e}" )
        

def exit_with_code( code, optional_message=None, quiet=False ):
    should_log = not quiet
    exit_msg = ''
    if code == 0:
        print_styled( f"GOODBYE.", "blue",end="\n\n",prefix="\n" )
        pass
    else:
        if optional_message:
            exit_msg = exit_msg + '\n' + optional_message
        if not quiet:
            print_styled( exit_msg, "red", should_log=should_log )
            print_styled( f"GOODBYE.", "blue",end="\n\n",prefix="\n" )
        sys.exit( code )

def convert_file( filein, fileout, force_write, should_log ):
  should_log = not quiet
  try:
    data_uri = DataURI.from_file(filein)
    print_styled( f" INPUT: {filein}", "cyan", prefix="\n", end="\n", should_log=should_log )
    if not fileout:
        if should_log:
            print_styled( f"OUTPUT: {data_uri}", "cyan", prefix="", end="\n\n", should_log=should_log )
        else:
            print( data_uri, end=None )
    filename_input = os.path.basename( filein )
    if fileout:
        print_styled( f"OUTPUT: {fileout}", "cyan", prefix="", end="\n\n", should_log=should_log )
        was_existing = os.path.exists( file_output ) and force_write
        with open(fileout, 'w') as export_file:
            html_to_write = f"<html><body><p><b>Image/Preview:</b><br><img style='max-width:90%;background-color:white;padding:3px;border:1px solid gray;margin:10px;' src='{data_uri}'></p>"
            html_to_write += f"<p><b>Audio/Preview:</b><br><audio controls><source src='{data_uri}' type='{data_uri.mimetype}'>Your browser does not support the audio tag.</audio></p>"
            html_to_write += f"<p><b>Video/Preview:</b><br><video style='max-width:90%;'><source src='{data_uri}' type='{data_uri.mimetype}'>Your browser does not support the video tag.</video></p>"
            html_to_write += f"<p><b>File/Preview:</b><br><div style='padding:7px;'><a href='{data_uri}' download='{filename_input}' title='Download {filename_input}'>Download</a>&nbsp;{filename_input}</div></p>"
            html_to_write += f"<p><b>Data URI ({data_uri.mimetype}):</b><br><div style='background-color:#ddd;padding:7px;;overflow-wrap:break-word;font-family:Courier;margin:10px;'>{data_uri}</div></p></body></html>"
            export_file.write(html_to_write)
            if was_existing:
                print_styled( f"OK: Overwritten file '{fileout}' successfully.", "green", prefix="", should_log=should_log )
            else:
                print_styled( f"OK: Written to file '{fileout}' successfully.", "green", prefix="", should_log=should_log )
    else:
        print_styled( f"OK: No files created/written.", "yellow", prefix="", should_log=should_log )
  except Exception as e:
    exit_with_code( 1, f"ERROR: Writing file '{fileout}'.\n{e}", quiet=quiet )

########
# MAIN
########
if __name__ == "__main__":
    file_input, file_output, force_write, quiet = parse_cmdline_arguments()
    should_log = not quiet
    if should_log:
        print_styled( f"WELCOME.", "blue", end="\n" )
    if not os.path.exists( file_input ):
        exit_with_code( 1, f"ERROR: File '{file_input}' not found!", quiet=quiet )
    else:
        if not force_write and file_output and os.path.exists( file_output ):
            exit_with_code( 1, f"ERROR: File '{file_output}' already exists!", quiet=quiet )
        else:
            convert_file( file_input, file_output, force_write, quiet )

    print_styled( f"GOODBYE.", "blue",end="\n\n",prefix="\n", should_log=should_log )
