import os
from pathlib import Path
package_name="HousePricePrediction"
list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",#f is there is to replace variable name
]
for i in list_of_files:
    path_name=Path(i)
    dirname,filename=os.path.split(i)
    if dirname!="": #not blank,it is blank when path_name contains only filename
        os.makedirs(dirname,exist_ok=True)
    if(not os.path.exists(path_name)or os.path.getsize(path_name)==0):
        with open(filename,"w") as f:
            pass
    else:
        print(f"{filename} already exists")
