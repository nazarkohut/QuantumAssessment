import joblib
import random

import torch

import numpy as np
import torch.nn as nn
import torch.nn.functional as F

from abc import ABC, abstractmethod
from torchvision import transforms
from sklearn.ensemble import RandomForestClassifier


class DigitClassificationInterface(ABC):
    @abstractmethod
    def predict(self, image: np.ndarray) -> int:
        """
        Predict the class of the input image.

        :param image: A 28x28x1 numpy array representing the image.
        :return: An integer value representing the predicted digit (0-9).
        """
        pass

    def fit(self):
        """
        Train model on provided data.
        :return: trained model.
        """
        pass


class CNNModel(DigitClassificationInterface):
    def __init__(self, model_path: str = None):
        """
        Initialize the CNN model. Load a pre-trained model if a path is provided.

        :param model_path: Path to a pre-trained model file (optional).
        """
        self.model = SimpleCNN()
        if model_path:
            self.model.load_state_dict(torch.load(model_path))
        self.model.eval()  # Set model to evaluation mode
        self.transform = transforms.Compose([
            transforms.ToTensor(),  # Convert numpy array to tensor
        ])

    def predict(self, image: np.ndarray) -> int:
        if image.shape != (28, 28, 1):
            raise ValueError("Input shape must be (28, 28, 1) for CNNModel.")

        # Convert numpy array to tensor and normalize
        image = self.transform(image.squeeze(-1))  # Remove channel dimension for transforms
        image = image.unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            output = self.model(image)
            predicted_class = output.argmax(dim=1).item()
        return predicted_class


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)  # Flatten for fully connected layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


class RFModel(DigitClassificationInterface):
    def __init__(self, model_path: str = None):
        """
        Initialize the Random Forest model. Load a pre-trained model if a path is provided.

        :param model_path: Path to a pre-trained model file (optional).
        """
        if model_path:
            self.model = joblib.load(model_path)
        else:
            self.model = RandomForestClassifier(n_estimators=100)

    def predict(self, image: np.ndarray) -> int:
        if image.shape != (28, 28, 1):
            raise ValueError("Input shape must be (28, 28, 1) for RFModel.")

        # Flatten the image to a 1D array
        flattened_image = image.flatten().reshape(1, -1)
        return self.model.predict(flattened_image)[0]

    def fit(self):
        raise NotImplementedError("This method is not implemented.")


class RandomModel(DigitClassificationInterface):
    def __init__(self):
        self._lower_bound_digit = 0
        self._upper_bound_digit = 9

    def predict(self, image: np.ndarray) -> int:
        if image.shape != (28, 28, 1):
            raise ValueError("Input shape must be (28, 28, 1) for RandomModel.")
        # TODO: clarify why we need center crop.
        return random.randint(self._lower_bound_digit, self._upper_bound_digit)

    def fit(self):
        raise NotImplementedError("This method is not implemented. Reason: no training needed for this model")


class DigitClassifier:
    def __init__(self, algorithm: str):
        """
        Initialize the classifier with the selected algorithm.

        :param algorithm: One of 'cnn', 'rf', 'rand'.
        """
        self.model = self._initialize_model(algorithm)

    def _initialize_model(self, algorithm: str) -> DigitClassificationInterface:
        if algorithm == 'cnn':
            return CNNModel()
        elif algorithm == 'rf':
            return RFModel()
        elif algorithm == 'rand':
            return RandomModel()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    def predict(self, image: np.ndarray) -> int:
        """
        Predict the class of the input image using the selected algorithm.

        :param image: A 28x28x1 numpy array representing the image.
        :return: An integer value representing the predicted digit (0-9).
        """
        return self.model.predict(image)

    def fit(self):
        raise NotImplementedError("This method is not implemented.")



image = np.random.rand(28, 28, 1).astype(np.float32)  # Dummy test image
cnn_classifier = DigitClassifier(algorithm='cnn')
cnn_prediction = cnn_classifier.predict(image=image)

# TODO: implement fit and use trained model for inference
# Current implementation omits training of models
# rf_classifier = DigitClassifier(algorithm='rf')
# rf_classifier.predict(image=image)

random_classifier = DigitClassifier(algorithm='rand')
random_classifier_prediction = random_classifier.predict(image=image)

print(cnn_prediction, random_classifier_prediction)


