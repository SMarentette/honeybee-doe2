import os
from pathlib import Path

from honeybee_doe2.writer import model_to_inp
from honeybee.model import Model


hbjson_file_path = r"C:\Users\Steve.marentette.IG\Desktop\IES Projects\Cowichan\Cowichan.hbjson"

model = Model.from_file(hbjson_file_path)

inp_string = model_to_inp(
    model, hvac_mapping='Story',
    equest_version= '3.64'
)

# Get the directory of the HBJSON file
hbjson_dir = Path(hbjson_file_path).parent

# Create the output INP file path in the same directory
inp_file_path = hbjson_dir / f"{Path(hbjson_file_path).stem}.inp"

# Write the INP string to the file
with open(inp_file_path, 'w') as f:
    f.write(inp_string)

print(f"INP file written to: {inp_file_path}")