import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name = "job"

list_of_files = [
    "setup.py",
    "requirements.txt",
    "src/__init__.py",
    "src/job_api.py",
    "src/helper.py",
    "mcp_server.py",
    "app.py",
] 

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath,"w") as f:
            pass 
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created") 