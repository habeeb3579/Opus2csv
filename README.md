
------------------------------------------------------------------------

# Opus to Array/CSV Converter

------------------------------------------------------------------------

The **Opus to Array/CSV** Converter is a Python tool designed to convert
Opus Binary Files to Arrays or CSV format. This tool is useful for
extracting data from Opus Binary Files and storing it in a more
accessible format for further analysis. It is a command-line tool that
allows users to convert Opus Binary Files to either CSV or Array format.
It currently supports two different storage modes (CSV and np arrays)
and provides flexibility in specifying the output path.

## Table of Contents

------------------------------------------------------------------------

-   [Introduction](#intro)

-   [Installation](#install)

-   [Usage](#use)

-   [Options](#opt)

-   [Folder Structure](#fold)

-   [Example](#ex)


### Introduction {#intro}

------------------------------------------------------------------------

The Opus to Array Converter is a command-line tool that allows users to
convert Opus Binary Files to either CSV or Array format. It supports
different storage modes and provides flexibility in specifying the
output path.

### Installation {#install}

------------------------------------------------------------------------

To install the Opus to Array Converter, follow these steps:

1.  Clone the repository:

`git clone [https://github.com/habeeb3579/Opus2csv.git](https://github.com/habeeb3579/Opus2csv.git)`

2.  Change into the project directory:

`cd OPUS2CSV`

3.  Install the required dependencies:

`pip install -r requirements.txt`

### Usage {#use}

------------------------------------------------------------------------

Run

`python3 converter.py -h`

The usage of the converter is as follows:

usage: opus2arr_converter [options] input_file

Function to Convert Opus Binary Files to Arrays or CSV

positional arguments: FOLDER_PATH Path to the folder containing Opus
Binary Files to be converted

options:

-h, ---help show this help message and exit

-m {csv,array} [{csv,array} ...], ---mode {csv,array} [{csv,array} ...]

Storage mode (csv or array) (default: array)

-o out, ---out out CSV/Array output path, the default is the current
directory (default: .)

### Options {#opt}

------------------------------------------------------------------------

-h, --help: Show the help message and exit.

-m, --mode: Specify the storage mode (csv or array). Default is array.

-o, --out: Specify the output path for CSV/Array files. Default is the
current directory.

### Folder Structure {#fold}

------------------------------------------------------------------------

The project follows a specific folder structure:

-   Bruker_Opus_CSV/

    -   utils/

        -   `file_list.py`

        -   `file_reader.py`

        -   `grp_wvn.py`

        -   `parsedFiles.py`

    -   test_data/

    -   `convert.py` (main file)

    -   `requirements.txt`

    -   `README.md`

    -   `requirements.txt`

### Example

------------------------------------------------------------------------

To convert Opus Binary Files in the `input_folder` to CSV format, you
can use the following command:

`python3 convert.py input_folder -m csv -o output_folder`

To convert Opus Binary Files in the `input_folder` to Array format, you
can use the following command:

`python3 convert.py input_folder -m array -o output_folder`

### Requirements

------------------------------------------------------------------------

Ensure you have the required dependencies installed. You can install
them using:

`pip install -r requirements.txt`
