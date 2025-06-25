This repository contains the code to reproduce all statistics and figures presented in the paper **"Global Vaccination Coverage and Disease Incidence in Cattle, Pigs, and Poultry."**

Due to conflicting package dependencies, we recommend using three (or optionally four) separate Python environments to reproduce all results. The instructions below detail the setup for each environment and the order in which to run the files.

---

## 1. Environment Setup

The Python environments in this study were created using the Anaconda package manager. Following Anaconda installation, please ensure Conda is up-to-date for smoother setup:
```bash
conda update -n base -c conda-forge conda
```

### a) General Environment (for most of the code)

Install all modules from `requirements_general.txt` in a Python **3.8.8** environment. You can do so by the below steps.

Using an anaconda terminal, navigate to the directory containing `requirements_general.txt`, and run:

```bash
conda create -n vax_inc_general python=3.8.8 jupyter -y
conda activate vax_inc_general
pip install -r requirements_general.txt
python -m ipykernel install --user --name vax_inc_general --display-name "vax_inc_general"
```

### b) Geopandas Environment (general map plotting)

Install all modules from `requirements_geo.yml` in a Python **3.10.12** environment. You can do so by the below steps.

Using an anaconda terminal, run:

```bash
vax_inc_geo
conda create -n vax_inc_geo python=3.10.12 jupyter -y
conda activate vax_inc_geo
conda install -c conda-forge geopandas==0.10.2 rasterio==1.3.7 -y
pip install python-docx==0.8.11 jenkspy==0.3.2 matplotlib==3.5.2 numpy==1.23.5 pandas==1.4.2 pycountry==22.3.5
python -m ipykernel install --user --name vax_inc_geo --display-name vax_inc_geo
```

### c) Incidence Environment

Install all modules from `requirements_incidence.yml` in a Python **3.7.16** environment.

Using an anaconda terminal, run:

```bash
conda create -n vax_inc_incidence python=3.7.16 jupyter -y
conda activate vax_inc_incidence
conda install -c conda-forge r-base -y
conda install -c conda-forge rpy2=2.9.4 -y
pip install matplotlib==3.5.3 numpy==1.21.0 pandas==1.3.5 pycountry==22.3.5 scipy==1.7.3
python -m ipykernel install --user --name vax_inc_incidence --display-name "vax_inc_incidence"
conda install --force-reinstall pyzmq zeromq -y
pip install --force-reinstall jupyter_client ipykernel
```

> The package **rpy2** requires that R is installed locally on your computer (version 4.1.3).


### d) (Optional) ArcGIS Environment (for maps color-coded by pixel)

This environment is only necessary to generate and visualize maps that are color-coded by pixel.

>Requires an ArcGIS subscription.

Clone the ArcGIS Conda environment from the application to a local destination (recommended under your `anaconda/envs/` directory, e.g., `C:\Users\[USER]\anaconda3\envs\vax_inc_arcgis`).

Then run:

```bash
conda activate vax_inc_arcgis
conda env update --name vax_inc_arcgis --file requirements_arcgis.yml -y
python -m ipykernel install --user --name vax_inc_arcgis --display-name "vax_inc_arcgis"
```
---

## 2. Running the code

Each Jupyter Notebook specifies the relevant kernel to use. The program files can be run in any order as the repository contains intermediate data outputs from each `.ipynb` file. 

However, to reproduce findings from start (raw data) to finish (end results), run the code files in the following order:

**a) Common Source Data**
- `Extrapolating + interpolating populations - filling in missing datapoints.ipynb`

**b) Disease Incidence**
- `2005-2024 cattle incidence rate (yearly).ipynb`
- `2005-2024 poultry incidence rate (yearly).ipynb`
- `2005-2024 swine incidence rate (yearly).ipynb`
>The above three files can be run in any order.

**c) Vaccination Coverage**
- `cattle vaccine coverage_admin_reports.ipynb`
- `poultry vaccine coverage_admin_reports.ipynb`
- `swine vaccine coverage_admin_reports.ipynb`
>The above three files can be run in any order.

- `cattle vaccine coverage_all_data_sources.ipynb`
- `poultry vaccine coverage_all_data_sources.ipynb`
- `swine vaccine coverage_all_data_sources.ipynb`
>The above three files can be run in any order.

**d) Imputation**
- `Imputation for missing vaccination coverage and disease incidence (30+ countries data threshold per disease).ipynb`

**e) Vaccination Coverage**
- `Combine ALL Vaccination Coverage Dataframes.ipynb`

**f) Disease Incidence**
- `Combine ALL Incidence Dataframes.ipynb`

>*Run the remaining files in any order:*

**g) Vaccination Coverage**
- `Calculating global 2024 coverage levels, top countries at risk by unvaccinated, global cases.ipynb`
- `Plot vaccination_by_country (proportion vaccinated).ipynb`
- `Generate Arcpy datafiles for disease-specific vaccination plotting.ipynb`
- `Plot vaccination coverage (per pixel).ipynb`
- `Arcpy_Current pop size maps (Cattle, chickens, and swine).ipynb`
- `Plot population maps of animals.ipynb`

**h) Disease Incidence:**
- `Cases of disease over time.ipynb`
- `Plot incidence AND report top incidence countries 2024.ipynb`

---

## Overview of Folders
- **Common Source Data:**
Contains raw data from WAHIS, FAO, and other sources used to generate the findings in this study.
- **Disease Incidence:**
Contains the code used to calculate all disease incidence estimates and generate the relevant figures.
- **Vaccination Coverage:**
Contains the code used to calculate all vaccination coverage estimates and generate the relevant figures.
- **Imputation:**
Contains the code used to impute missing values via XGBoost (trained with Bayesian optimization) and other techniques outlined in the paper.

## License

This project is licensed under the [MIT License](LICENSE).  

If you use this codebase, please cite the accompanying manuscript:

> *Global Vaccination Coverage and Disease Incidence in Cattle, Pigs, and Poultry* — Gleason A, Impalli I, Sheen J, Cabezas A, Grenfell B, Levin S, Van Boeckel TP, Laxminarayan R. 2025.

