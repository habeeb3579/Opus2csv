import argparse
def create_parser():
    parser = argparse.ArgumentParser(
    prog='opus2arr_converter',
    usage='%(prog)s [options] input_file',
    description='Function to Convert Opus Binary Files to Arrays or CSV',
    epilog='Enjoy converting Opus files to CSV!',
    prefix_chars='-',
    fromfile_prefix_chars='@',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    #grp = parser.add_mutually_exclusive_group()
    #parser.add_argument("-v", "--verbose", action="store_true")
    #grp.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument('folder_path', metavar='FOLDER_PATH', type=str,
                        help='Path to the folder containing Opus Binary Files to be converted')

    parser.add_argument('-m', '--mode', choices=['csv', 'array'], nargs='+', help='Storage mode (csv or array)', default="array")
    # parser.add_argument('-o', '--out', help='CSV/Array output path, the default is the current directory', action="store_true", default='.')
    parser.add_argument('-o', '--out', help='CSV/Array output path, the default is the current directory', default='.')

    #parser.add_argument('-a', '--arr', help='Array output path', action="store_true", default=False)

    return parser