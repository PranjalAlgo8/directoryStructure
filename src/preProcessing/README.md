
# preProcessing Submodule

## Overview
The `preProcessing` submodule is responsible for all the data preprocessing steps required to prepare raw data for model training or analysis. This includes data cleaning, transformation, feature engineering, and other essential tasks that ensure data quality and consistency. The submodule is designed to be modular and flexible, allowing users to easily add or modify preprocessing steps as needed.

## Submodule Structure
The `preProcessing` submodule is organized as follows:

```
preProcessing/
├── __init__.py
├── data_cleaning.py
├── feature_engineering.py
└── data_transformation.py
```

### Files and Directories

#### 1. `__init__.py`
- **Description**: Initializes the `preProcessing` submodule. This file contains the `process()` function, which serves as the main orchestrator for all preprocessing steps. The `process()` function calls various functions from other scripts within the submodule to execute the complete preprocessing pipeline.
- **Key Function**:
  - `process(data)`: Orchestrates the entire preprocessing workflow by sequentially calling functions from `data_cleaning.py`, `feature_engineering.py`, and `data_transformation.py`. It takes raw data as input and returns cleaned and transformed data ready for further processing or model training.
  
- **Usage Example**:
  ```python
  from data_processing.preProcessing import process

  # Assuming 'raw_data' is your input DataFrame
  processed_data = process(raw_data)
  print("Processed Data:", processed_data)
  ```

#### 2. `data_cleaning.py`
- **Description**: Contains functions for cleaning the raw data. This includes handling missing values, removing duplicates, correcting data types, and standardizing formats.
- **Key Functions**:
  - `remove_missing_values(data)`: Removes or imputes missing values in the dataset.
  - `remove_duplicates(data)`: Removes duplicate records from the dataset.
  - `standardize_formats(data)`: Standardizes data formats (e.g., date formats, categorical labels).

- **Usage Example**:
  ```python
  from data_processing.preProcessing.data_cleaning import remove_missing_values

  cleaned_data = remove_missing_values(raw_data)
  print("Cleaned Data:", cleaned_data)
  ```

#### 3. `feature_engineering.py`
- **Description**: Contains functions for creating new features or modifying existing features to enhance the dataset for model training.
- **Key Functions**:
  - `create_interaction_features(data)`: Creates new features based on interactions between existing variables.
  - `normalize_features(data)`: Normalizes numerical features to a common scale.
  - `encode_categorical(data)`: Encodes categorical variables into numerical representations.

- **Usage Example**:
  ```python
  from data_processing.preProcessing.feature_engineering import encode_categorical

  engineered_data = encode_categorical(cleaned_data)
  print("Feature Engineered Data:", engineered_data)
  ```

#### 4. `data_transformation.py`
- **Description**: Contains functions for transforming the data into a format suitable for model training or analysis.
- **Key Functions**:
  - `log_transform(data, columns)`: Applies a logarithmic transformation to specified columns to handle skewness.
  - `scale_features(data)`: Scales numerical features using standardization or normalization techniques.
  - `pca_transform(data)`: Applies Principal Component Analysis (PCA) to reduce dimensionality of the dataset.

- **Usage Example**:
  ```python
  from data_processing.preProcessing.data_transformation import scale_features

  transformed_data = scale_features(engineered_data)
  print("Transformed Data:", transformed_data)
  ```

## Workflow
The typical workflow for using the `preProcessing` submodule is as follows:

1. **Raw Data Input**: Start with your raw data in the form of a DataFrame or similar structure.
2. **Call the `process()` Function**: Use the `process()` function in `__init__.py` to run all preprocessing steps sequentially.
3. **Data Cleaning**: The raw data is cleaned using functions in `data_cleaning.py`.
4. **Feature Engineering**: New features are created and existing features are modified using functions in `feature_engineering.py`.
5. **Data Transformation**: The cleaned and engineered data is transformed into the final format using functions in `data_transformation.py`.
6. **Output**: The `process()` function returns the fully preprocessed data, ready for model training or further analysis.

## Dependencies
- **Libraries**: The `preProcessing` submodule depends on the following libraries:
  - `pandas`: For data manipulation and cleaning.
  - `numpy`: For numerical operations.
  - `scikit-learn`: For scaling, encoding, and other feature engineering tasks.

Install the required dependencies using:
```bash
pip install pandas numpy scikit-learn
```

## Best Practices
- **Modular Design**: Each preprocessing step should be implemented as a separate function to maintain modularity and flexibility.
- **Error Handling**: Implement robust error handling to manage issues like missing columns, incorrect data types, or out-of-range values.
- **Logging**: Include logging at each preprocessing step to track changes and transformations applied to the data.

## Extending the Submodule
1. **Adding New Functions**: Create a new `.py` file for the new preprocessing step, or add the function to an existing file if relevant.
2. **Update `process()`**: Update the `process()` function in `__init__.py` to include the new function in the preprocessing workflow.
3. **Testing**: Test the new function independently and as part of the overall `process()` workflow to ensure compatibility.

## Usage Example
```python
from data_processing.preProcessing import process

# Example raw data
raw_data = pd.DataFrame({
    'feature1': [1, 2, 3, None, 5],
    'feature2': ['A', 'B', 'A', 'B', None],
    'feature3': [10.5, 20.1, None, 40.3, 50.7]
})

# Process the data
processed_data = process(raw_data)
print("Processed Data:", processed_data)
```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new preprocessing function'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
Special thanks to all contributors and the development community for their support and contributions.

