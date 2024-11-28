import argparse
from autogluon.tabular import TabularDataset, TabularPredictor

from logger import logger


def train():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Train a model using AutoGluon.")
    parser.add_argument(
        "--train_data",
        type=str,
        help="Path to the training data file (required)."
    )
    parser.add_argument(
        "--target_column",
        type=str,
        default="target",
        help="Name of the target column (default: 'target')."
    )
    parser.add_argument(
        "--time_limit",
        type=int,
        default=None,
        help="Maximum training time in seconds (default: 360)."
    )
    args = parser.parse_args()

    # Log the start of the process
    logger.info(f"Loading training data from: {args.train_data}")
    train_data = TabularDataset(args.train_data)

    # Train the model with time limit
    logger.info(f"Training model with target column: {args.target_column} and time limit: {args.time_limit} seconds")
    TabularPredictor(label=args.target_column).fit(
        train_data,
        time_limit=args.time_limit
    )


if __name__ == "__main__":
    train()
