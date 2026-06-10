import os
import subprocess
import pandas as pd
import numpy as np
from rdkit import Chem
from mordred import Calculator, descriptors

# ---------- PATH ----------

data = pd.read_csv('/home/partha/Oshiya/ankita/RDA_mechano_data.csv')
data["reactant_log"] = data["reactant_log"].astype(str).str.strip()

log_files_dir = "/home/partha/Oshiya/ankita/log_f/"  # .log files
output_dir = "/home/partha/Oshiya/ankita/sdf_f/"  # .sdf files

os.makedirs(output_dir, exist_ok=True)  # create the output directory if it doesn't exist 

# --------------------------

print("Dataset size:", len(data))
print("Distribution:", data['target'].value_counts())

# ------- .log to .sdf ------

success_count = 0

for log_file in data['reactant_log']:
    if not log_file.endswith(".log"):
        log_file = log_file +".log"

    input_path = os.path.join(log_files_dir, log_file)
    
    output_file = log_file.replace('.log', '.sdf')
    output_path = os.path.join(output_dir, output_file)
    
    command = ['obabel', "-ilog", input_path, '-osdf', '-O', output_path]
    
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Converted {log_file}")
        success_count +=1
    except subprocess.CalledProcessError:
        print(f"Error converting {log_file}")

print(f"\nTotal successfully converted: {success_count}/{len(data)}")

# ------ Mordred Descriptor Calculator ------

calc = Calculator(descriptors, ignore_3D=False)

descriptors_list = [] # list to hold each molecule's descriptors

sdf_folder = "/home/partha/Oshiya/ankita/sdf_f/"
sdf_files = [f for f in os.listdir(sdf_folder) if f.endswith('.sdf')]

for sdf_file in sdf_files:
    sdf_path = os.path.join(sdf_folder, sdf_file)
    mol = Chem.MolFromMolFile(sdf_path, removeHs=False)
    if mol:
        desc = calc(mol)
        desc_dict = desc.asdict()  # convert descriptors to a dicts
        desc_dict['molecule'] = sdf_file.strip()
        descriptors_list.append(desc_dict)
    else:
        print(f"Failed to load {sdf_file}")

df_descriptors = pd.DataFrame(descriptors_list)  # convert list of dicts to DataFrame

cols = df_descriptors.columns.tolist()
cols.insert(0, cols.pop(cols.index('molecule')))
df_descriptors = df_descriptors[cols]

df_descriptors.to_csv("/home/partha/Oshiya/ankita/molecular_descriptors.csv", index=False)
print("Shape descriptor dataframe:",df_descriptors.shape)

# ---------- Merging Dataframes ----------

df1 = data.copy()
df2 = df_descriptors.copy()

df1['reactant_log'] = df1['reactant_log'].str.strip()
df2['molecule'] = df2['molecule'].str.strip()

df1['id'] = df1['reactant_log'].str.replace('.log', '', regex=False)
df2['id'] = df2['molecule'].str.replace('.sdf', '', regex=False)

df_merged = pd.merge(df1, df2, on='id', how='inner')
df_merged.drop(columns=['reactant_log', 'molecule'], inplace=True)

df_merged.to_csv("/home/partha/Oshiya/ankita/MC_RDA_dataset.csv", index=False)
print("Shape of merged final dataset for ML:",df_merged.shape)

