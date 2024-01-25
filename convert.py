import numpy as np
import pandas as pd
import os
from utils.files_reader import opusFilesReader
from utils.parsedFiles import create_parser
from utils.files_list import list_OpusFiles
from utils.grp_wvn import group_arrays_by_wavenumbers, are_arrays_equal


def create_output_folder(output_folder):
    """
    Check if the output folder exists, and create it if not.

    Parameters:
    - output_folder (str): Path to the output folder.

    Returns:
    - str: Path to the existing or newly created output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f'Created output folder: {output_folder}')
    else:
        print(f'Output folder already exists: {output_folder}')

    return output_folder

def process_csv_mode(wavenumbers, absorbance, params, file_names, args):
    df = []
    add_params = []

    if are_arrays_equal(wavenumbers):
        df = pd.DataFrame(absorbance, columns=wavenumbers[0])
        df['File Name'] = file_names
        add_params = params
    else:
        grouped_arrays = group_arrays_by_wavenumbers(wavenumbers)
        for idx, group in enumerate(grouped_arrays, 1):
            common_wvn = group['wavenumbers']
            #print(f"  Indices: {group['indices']}")
            #print(f"  wvn: {common_wvn.shape}")
            idxs = group['indices']
            sel_absorbance = [absorbance[idx] for idx in idxs]
            #print(f"{[x.shape for x in absorbance]}")
            df.append(pd.DataFrame(sel_absorbance, columns=common_wvn))
            add_params.append(params[idx])

    if args.out:
        out_folder = create_output_folder(args.out)
        if isinstance(df, pd.DataFrame):
            df.to_csv(f'{out_folder}/output.csv', index=False)
            np.save(f'{out_folder}/output.npy', add_params)

        if isinstance(df, list):
            for i, x in enumerate(df, 1):
                x.to_csv(f'{out_folder}/output_{i}.csv')
                np.save(f'{out_folder}/output_{i}.npy', add_params)
                
    else:
        print(f"Output path not specified. Please provide a valid output path.")

def process_array_mode(wavenumbers, absorbance, params, file_names, args):
    df = np.array([np.array(wavenumbers), np.array(absorbance), np.array(params), np.array(file_names)])
    
    if args.out:
        out_folder = create_output_folder(args.out)
        np.save(f'{out_folder}/output.npy', df)
    else:
        print(f"Output path not specified. Please provide a valid output path.")

def main():
    parser = create_parser()
    args = parser.parse_args()

    files = list_OpusFiles(args.folder_path)

    wavenumbers, absorbance, params, file_names = opusFilesReader(files)

    if args.mode == ['csv'] and len(args.mode) == 1:
        process_csv_mode(wavenumbers, absorbance, params, file_names, args)
    elif args.mode == ['array'] and len(args.mode) == 1:
        process_array_mode(wavenumbers, absorbance, params, file_names, args)
    elif args.mode == ['csv', 'array'] and len(args.mode) == 2:
        print("Still working on this. Try either csv or array.")
    else:
        print("Invalid mode specified.")

if __name__ == "__main__":
    main()