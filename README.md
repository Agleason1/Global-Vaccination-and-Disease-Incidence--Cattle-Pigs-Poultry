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

Install all modules from 'requirements_geo.yml' in a Python **3.10.12** environment. You can do so by the below steps.

Using an anaconda terminal, navigate to the directory containing 'requirements_geo.yml' and run:

```bash
conda env create -f requirements_geo.yml -y
conda activate vax_inc_geo
python -m ipykernel install --user --name vax_inc_geo --display-name "vax_inc_geo"
```

### c) Incidence Environment

Install all modules from `requirements_incidence.yml` in a Python **3.7.16** environment.

Using an anaconda terminal, navigate to the directory containing `requirements_incidence.yml` and run:

```bash
conda env create -f requirements_incidence.yml -y
conda activate vax_inc_incidence
python -m ipykernel install --user --name vax_inc_incidence --display-name "vax_inc_incidence"
```

> The package **rpy2** requires that R is installed locally on your computer (version 4.1.3).


### d) (Optional) ArcGIS Environment (for maps color-coded by pixel)

This environment is only necessary to generate and visualize maps that are color-coded by pixel.

>Requires an ArcGIS subscription.

Clone the ArcGIS Conda environment from the application to a local destination (recommended under your 'anaconda/envs/' directory, e.g., 'C:\Users\[USER]\anaconda3\envs\vax_inc_arcgis').

Then run:

```bash
conda activate vax_inc_arcgis
conda env update --name vax_inc_arcgis --file requirements_arcgis.yml -y
python -m ipykernel install --user --name vax_inc_arcgis --display-name "vax_inc_arcgis"
```
---

## 2. Running the code

Each Jupyter Notebook specifies the relevant kernel to use. The program files can be run in any order as the repository contains intermediate data outputs from each '.ipynb' file. 

However, to reproduce findings from start (raw data) to finish (end results), run the code files in the following order:

**a) Common Source Data**
- `Imputation for missing vaccination coverage and disease incidence (30+ countries data threshold per disease).ipynb`

**b) Disease Incidence**
- `2005-2024 cattle incidence rate (yearly).ipynb`
- `2005-2024 poultry incidence rate (yearly).ipynb`
- `2005-2024 swine incidence rate (yearly).ipynb`
>The above three files can be run in any order.

**c) Vaccination Coverage**
- `2005-2024_part_cattle_vaccine_coverage_by_country.csv`
- `2005-2024_part_poultry_vaccine_coverage_by_country.csv`
- `2005-2024_part_swine_vaccine_coverage_by_country.csv`
>The above three files can be run in any order.

- `2005-2024_full_cattle_vaccine_coverage_by_country.csv`
- `2005-2024_full_poultry_vaccine_coverage_by_country.csv`
- `2005-2024_full_swine_vaccine_coverage_by_country.csv`
>The above three files can be run in any order.

**d) Imputation**
- `Imputation for missing vaccination coverage and disease incidence (30+ countries data threshold per disease).ipynb`

**e) Vaccination Coverage**
- `Combine ALL Vaccination Coverage Dataframes.ipynb`

**f)Disease Incidence**
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