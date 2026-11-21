from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import create_predictions

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            create_predictions, 
            None,
            "predictions",
        )
    ])
