import argparse
import os
from autogluon.tabular import TabularDataset, TabularPredictor
from logger import logger


def predict():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate predictions using AutoGluon.")
    parser.add_argument(
        "--test_data",
        type=str,
        required=True,
        help="Path to the test data file (required)."
    )
    parser.add_argument(
        "--model_path",
        type=str,
        required=True,
        help="Path to the saved model (required)."
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="predictions.csv",
        help="Path to save the predictions (default: 'predictions.csv')."
    )
    args = parser.parse_args()

    # Log the start of the process
    logger.info(f"Loading test data from: {args.test_data}")
    test_data = TabularDataset(args.test_data)

    # Load the saved model
    if not os.path.exists(args.model_path):
        logger.error(f"Model path '{args.model_path}' does not exist.")
        return

    logger.info(f"Loading model from: {args.model_path}")
    predictor = TabularPredictor.load(args.model_path, require_py_version_match=False)

    # Generate predictions
    logger.info(f"Generating predictions for test data...")
    predictions = predictor.predict(test_data)

    # Save predictions to the specified output path
    predictions.to_csv(args.output_path, index=False)
    logger.info(f"Predictions saved to: {args.output_path}")


if __name__ == "__main__":
    predict()
