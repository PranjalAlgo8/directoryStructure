from src.configurations import ConfigReaderObj
from src.inferencing import getPredictions
from postProcessing import process as preprocessing
from preProcessing import process as postprocessing


def run():
    # This orchestrator function uses all the imported functions and returns no output. All the oututs are directly sent to the database from where the frontend/backend picks them up.
    return None