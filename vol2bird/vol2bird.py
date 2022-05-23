import pandas as pd
import h5py
import json
import subprocess
import pathlib
import sys
import re
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--input_file_list', action='store' , required='True', dest='input_file_list')

arg_parser.add_argument('--param_radar_db_source_name', action='store', type=str, required='True', dest='param_radar_db_source_name')

args = arg_parser.parse_args()

id = args.id

input_file_list = args.input_file_list

param_radar_db_source_name = args.param_radar_db_source_name

conf_output_dir = './output_dir' # Set this to something relevant to your machine. This needs to specify a path from where to upload from.

conf_output_dir = './output_dir' # Set this to something relevant to your machine. This needs to specify a path from where to upload from.

def translate_wmo_odim(radar_db, wmo_code):
    """"""

    # class FileTranslatorFileTypeError(LookupError):
    #    '''raise this when there's a filetype mismatch derived from h5 file'''

    if not isinstance(wmo_code, int):
        raise ValueError("Expecting a wmo_code [int]")
    else:
        pass

   
    odim_code = (
        radar_db.get(wmo_code).get("odimcode").upper().strip()
    )  # Apparently, people sometimes forget to remove whitespace..
    return odim_code

def extract_wmo_code(in_path):

    with h5py.File(in_path, "r") as f:

        # DWD Specific

        # Main attributes
        what = f["what"].attrs

        # Source block
        source = what.get("source")
        source = source.decode("utf-8")

        # Determine if we are dealing with a WMO code or with an ODIM code set
        # Example from Germany where source block is set as WMO
        # what/source: "WMO:10103"
        # Example from The Netherlands where source block is set as a combination of ODIM and various codes
        # what/source: RAD:NL52,NOD:nlhrw,PLC:Herwijnen
        source_list = source.split(sep=",")

    wmo_code = [string for string in source_list if "WMO" in string]

    # Determine if we had exactly one WMO hit
    if len(wmo_code) == 1:
        wmo_code = wmo_code[0]
        wmo_code = wmo_code.replace("WMO:", "")

    # No wmo code found, most likeley dealing with a dutch radar
    elif len(wmo_code) == 0:
        rad_str = [string for string in source_list if "RAD" in string]

        if len(rad_str) == 1:
            rad_str = rad_str[0]
        else:
            print(
                "Something went wrong with determining the rad_str and it wasnt WMO either, exiting"
            )
            sys.exit(1)
        # Split the rad_str
        rad_str_split = rad_str.split(":")
        # [0] = RAD, [1] = rad code
        rad_code = rad_str_split[1]

        rad_codes = {"NL52": "6356", "NL51": "6234", "NL50": "6260"}

        wmo_code = rad_codes.get(rad_code)

    return int(wmo_code)

def vol2bird(in_file, out_dir, radar_db, add_version=True, add_sector=False):
    # Construct output file
    date_regex = "([0-9]{8})"

    if add_version == True:
        version = "v0-3-20"
        suffix = pathlib.Path(in_file).suffix
        in_file_name = pathlib.Path(in_file).name
        in_file_stem = pathlib.Path(in_file_name).stem
        #
        out_file_name = in_file_stem.replace("pvol", "vp")
        out_file_name = "_".join([out_file_name, version]) + suffix

        # odim = odim_code(out_file_name)
        wmo = extract_wmo_code(in_file)
        odim = translate_wmo_odim(radar_db, wmo)

        datetime = pd.to_datetime(re.search(date_regex, out_file_name)[0])

        ibed_path = "/".join(
            [
                odim[:2],
                odim[2:],
                str(datetime.year),
                str(datetime.month).zfill(2),
                str(datetime.day).zfill(2),
            ]
        )

        out_file = "/".join([out_dir, ibed_path, out_file_name])

        # out_file = "_".join([out_file[:-len(suffix)], version + suffix])

    command = ["vol2bird", in_file, out_file]
    #command = ["/Users/nicolas_noe/vol2bird/opt/vol2bird/bin/vol2bird", in_file, out_file]

    result = subprocess.run(command, stderr=subprocess.DEVNULL)

    # if result.returncode != 0:
    #    print(result)
    #    print("Something went wrong, exitting")
    #    sys.exit(1)
    return [in_file, out_file]


out_dir_vp = "{}/{}".format(conf_output_dir,'vp')
output_file_list = []

with open(param_radar_db_source_name, mode="r") as f:
    radar_db_json = json.load(f)
    radar_db = {}
for radar_dict in radar_db_json:
    try:
        wmo_code = int(radar_dict.get("wmocode"))
        radar_db.update({wmo_code: radar_dict})
    except Exception:  # Happens when there is for ex. no wmo code.
        pass
    

file = input_file_list
output_file = vol2bird(file, out_dir_vp, radar_db)
output_file_list.append(output_file)

import json
filename = "/tmp/output_file_list_" + id + ".json"
file_output_file_list = open(filename, "w")
file_output_file_list.write(json.dumps(output_file_list))
file_output_file_list.close()
