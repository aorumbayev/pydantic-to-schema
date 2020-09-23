# Standard Library
from argparse import ArgumentParser
from inspect import getmembers, isclass
from os import makedirs, path
from shutil import rmtree
import pathlib
import importlib.util

# Third party
from pydantic import BaseModel


def export_models(input_folder: str, output_folder: str):
    dirpath = path.join(pathlib.Path().absolute(), input_folder)
    out_path = path.join(pathlib.Path().absolute(), output_folder)

    if path.exists(out_path) and path.isdir(out_path):
        rmtree(out_path)

    makedirs(out_path)

    spec = importlib.util.spec_from_file_location(
        "dum", path.join(dirpath, "__init__.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for key, obj in getmembers(module):
        if isclass(obj) and issubclass(obj, BaseModel):
            schema_path = path.join(out_path, f'{key}.json')
            with open(schema_path, 'w', encoding='utf-8') as file:
                file.write(obj.schema_json(indent=2))
                print(f"Exporting {key} model as {key} JSON Schema")

    print("Models exported!")


def main():
    parser = ArgumentParser(description=(
        'Convert pydantic models to JSON Schemas under specified folder'))
    parser.add_argument("--input",
                        help="Input folder with schemas",
                        metavar="FILE",
                        required=True)

    parser.add_argument("--output",
                        help="Output folder path",
                        metavar="FILE",
                        required=True)

    args = parser.parse_args()
    export_models(args.input, args.output)


if __name__ == "__main__":
    main()
