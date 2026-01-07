# dataURI
Convert any kind of data (images, files, etc.) to a data URI.

## Installation

Create a virtual environment and activate it, then install the `python-datauri` module.

```bash
python3 -m venv venv
source venv/bin/activate
pip install python-datauri
```

## Usage

```bash
python data_uri_from_file.py -h


      _       _        _    _ _____  _____ 
     | |     | |      | |  | |  __ \|_   _|
   __| | __ _| |_ __ _| |  | | |__) | | |  
  / _` |/ _` | __/ _` | |  | |  _  /  | |  
 | (_| | (_| | || (_| | |__| | | \ \ _| |_ 
  \__,_|\__,_|\__\__,_|\____/|_|  \_\_____|  v1.0.0
                                            
  Copyright (c) 2026, blazr
 
usage: data_uri_from_file.py [-h] -i <FILE IN> [-o <FILE OUT>] [-f] [-q]

dataURI v1.0.0 — a new dataURI in seconds

options:
  -h, --help            show this help message and exit

Mandatory:
  -i, --file-input <FILE IN>
                        path to input file

Optional:
  -o, --file-output <FILE OUT>
                        path to output file (optional)
  -f, --force           overwrite existing output files without warning
  -q, --quiet           do not print unnecessary stuff to standard out

USAGE EXAMPLES:
data_uri_from_file.py --file-input funny_meme.png
data_uri_from_file.py -i funny_meme.jpg -o funny_out.html -f
data_uri_from_file.py -i funny_meme.png --file-output funny_out.html -q
```

## Convert image or file to html
To convert a file into a URI that you can preview and see in a custom html file just call following.

```bash
python data_uri_from_file.py -i data_uri_from_file.py -o my_data_uri.html
```

## Convert image or file to data
To convert and directly copy to the pasteboard justr call the following.

```bash
python data_uri_from_file.py -i data_uri_from_file.py -q | pbcopy
```

