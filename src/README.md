
# src Module

## Overview
The `src` module is the core directory of the project, containing all the essential logic, functions, and classes needed for data processing, model inferencing, configuration management, and utility operations. This module is organized into several sub-modules, each serving a specific purpose in the overall workflow.

## Module Structure
The `src` module is structured as follows:

```
src/
├── __init__.py
├── config/
│   ├── __init__.py
│   ├── config.ini
│   └── configRead.py
├── data_processing/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── data_validation.py
│   └── post_processing.py
├── inferencing/
│   ├── __init__.py
│   ├── inferencing.py
│   ├── model_selection.py
│   └── models/
│       ├── __init__.py
│       ├── model1.sav
│       ├── model2.sav
├── utils/
    ├── __init__.py
    ├── helpers.py
    └── constants.py
```

## Sub-modules

### 1. `__init__.py`
- Initializes the `src` module and contains the `run` function, which serves as the entry point for executing the main application logic.

### 2. `config/`
- **Description**: Contains configuration-related modules and files.
    - `config.ini`: Configuration file that stores various settings required for the project.
    - `configRead.py`: Contains the `ConfigReader` class, which reads and parses configuration settings from the `config.ini` file.

### 3. `data_processing/`
- **Description**: Responsible for data manipulation and transformation.
    - `data_cleaning.py`: Functions for cleaning raw data, handling missing values, and removing duplicates.
    - `feature_engineering.py`: Functions for creating new features from existing data.
    - `data_validation.py`: Functions for validating the integrity and quality of data.
    - `post_processing.py`: Functions for processing the results after model inference.

### 4. `inferencing/`
- **Description**: Manages the process of model inferencing and model selection.
    - `inferencing.py`: Main script for performing model inference.
    - `model_selection.py`: Logic for selecting the best model based on predefined criteria.
    - `models/`: Directory containing pre-trained model files (`.sav` files).

### 5. `utils/`
- **Description**: Contains utility functions and shared resources that can be used across different sub-modules.
    - `helpers.py`: Helper functions for common tasks such as logging, file operations, and data manipulation.
    - `constants.py`: Constant values used throughout the project, such as file paths and configuration keys.

## Usage
To use any of the sub-modules, you can import them directly into your scripts. For example:

```python
from src.data_processing import data_cleaning
from src.utils.helpers import log_message
```

The `run` function in `src/__init__.py` serves as the main orchestrator for the application's workflow. It is called from the `app.py` file to execute the entire data processing and model inferencing pipeline.

## Dependencies
- The `src` module relies on various Python libraries. Ensure that all dependencies are installed by running:
```bash
pip install -r requirements.txt
```

## Configuration
- Configuration settings are managed through the `config/config.ini` file. You can update this file to change settings such as file paths, model parameters, or API keys.

## Logging
- Log files are stored in the `logs/` directory. Check `LatestLogs.log` for the most recent execution logs.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
Special thanks to all contributors and the development community for their support and contributions.

