from random import choices

CHOICES = ["yes", "no"]


def create_predictions(n_predictions: int = 100) -> list:
    return choices(CHOICES, k=n_predictions)
