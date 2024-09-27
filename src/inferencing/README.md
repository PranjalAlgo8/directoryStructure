
# inferencing Submodule

## Overview
The `inferencing` submodule is responsible for managing the entire process of model inference in the project. It includes scripts for selecting the appropriate pre-trained model, loading the model, preparing input data, and generating predictions. This submodule is designed to be flexible and scalable, allowing for easy integration of multiple models and complex inference workflows.

## Submodule Structure
The `inferencing` submodule is organized as follows:

```
inferencing/
├── __init__.py
├── inferencing.py
├── model_selection.py
└── models/
    ├── __init__.py
    ├── model1.sav
    ├── model2.sav
    └── ...
```

### Files and Directories

#### 1. `__init__.py`
- **Description**: Initializes the `inferencing` submodule. This file can be used to set up initial configurations, import necessary dependencies, or initialize global variables needed for inference. It ensures that all components of the submodule are accessible when the submodule is imported. This has a caller function `getPredictions` that is an orchestrator for all the py files in inferencing module.

#### 2. `inferencing.py`
- **Description**: The main script for performing model inference. It handles the following tasks:
  - **Loading the Model**: It loads the selected model from the `models/` directory.
  - **Preparing Input Data**: Takes input data, preprocesses it, and prepares it for the model.
  - **Generating Predictions**: Uses the loaded model to generate predictions on the prepared data.

- **Key Functions**:
  - `load_model(model_path)`: Loads the pre-trained model from the specified path.
  - `prepare_data(input_data)`: Prepares and preprocesses the input data for inference.
  - `predict(prepared_data)`: Generates predictions using the loaded model.

- **Usage Example**:
  ```python
  from inferencing.inferencing import load_model, prepare_data, predict, post_process

  model = load_model('models/model1.sav')
  data = prepare_data(input_data)
  predictions = predict(data)
  results = post_process(predictions)
  print(results)
  ```

#### 3. `model_selection.py`
- **Description**: Contains logic for selecting the best model based on predefined criteria. This can include model performance metrics, model availability, or user input.
- **Key Functions**:
  - `select_model(criteria)`: Selects and returns the path of the best model based on the specified criteria.
  - `list_available_models()`: Lists all available models in the `models/` directory.
  - `evaluate_model_performance(model_path)`: Evaluates the performance of a given model.

- **Usage Example**:
  ```python
  from inferencing.model_selection import select_model, list_available_models

  available_models = list_available_models()
  print("Available Models:", available_models)

  best_model_path = select_model(criteria="accuracy")
  print("Selected Model:", best_model_path)
  ```

#### 4. `models/`
- **Description**: Directory containing pre-trained models and serialized model files. Each model file is stored with a `.sav` extension, indicating that it has been serialized using a library such as `joblib` or `pickle`.
  
  - **Files**:
    - `model1.sav`: Serialized file for the first pre-trained model.
    - `model2.sav`: Serialized file for the second pre-trained model.
    - `__init__.py`: Initializes the `models` directory as a submodule, allowing for the dynamic import of models.

- **Adding a New Model**:
  1. Train and save your model using `joblib` or `pickle`:
     ```python
     from sklearn.externals import joblib
     joblib.dump(model, 'models/new_model.sav')
     ```
  2. Add the new model file to the `models/` directory.
  3. Update `model_selection.py` if necessary to include the new model in the selection logic.

## Usage Workflow

1. **Select the Model**: Use the `model_selection.py` script to choose the best model based on the desired criteria.
2. **Load the Model**: Use the `inferencing.py` script to load the selected model.
3. **Prepare Input Data**: Preprocess your input data using the `prepare_data()` function.
4. **Generate Predictions**: Pass the prepared data to the `predict()` function to get model predictions.
5. **Post-Process Results**: Use the `post_process()` function to format the predictions as needed.

## Dependencies
- **Libraries**: The `inferencing` submodule depends on the following libraries:
  - `scikit-learn`: For model loading and evaluation.
  - `joblib` or `pickle`: For model serialization and deserialization.
  - `pandas`: For data manipulation and preparation.

Install the required dependencies using:
```bash
pip install scikit-learn pandas joblib
```

## Best Practices
- **Model Versioning**: Maintain versioning for models stored in the `models/` directory to track changes and updates.
- **Model Evaluation**: Regularly evaluate model performance and update the `model_selection.py` logic as needed.
- **Error Handling**: Implement robust error handling in `inferencing.py` to manage issues like missing models or incorrect data formats.

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

