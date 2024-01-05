# Crime-Analysis

### Prerequisites

You will need to install these dependencies

```
pip3 install -r requirements.txt
```

### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)

## 1. Cleaning the Data

First we need to clean all of our original data

-   `python clean_data.py <year>`: Used to clean the raw data by year

## 2. Visualizing the Data

-   `python heatmap.py`: Produces heatmaps to identify crime hotspots

## 3. Running the Analysis

-   `python data_exploration.py`: Uses cleaned data to produce plots
-   `python chi_squared.py`: Uses cleaned data for inferential statistics

## Datasets

Dataset for Vancouver Crimes from VPD Open Data: https://geodash.vpd.ca/opendata/
