from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import create_report

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            create_report,
            ["{model}.predictions"],
            "report",
        )
    ])
