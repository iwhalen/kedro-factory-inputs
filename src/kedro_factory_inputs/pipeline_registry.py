"""Project pipelines."""

from __future__ import annotations

from kedro.pipeline import Pipeline, pipeline

from kedro_factory_inputs.pipelines.predict import (
    create_pipeline as create_predict_pipeline,
)
from kedro_factory_inputs.pipelines.report import (
    create_pipeline as create_report_pipeline,
)
from kedro_factory_inputs.settings import models


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = {}

    for model in models:
        pipelines[f"predict-{model}"] = pipeline(
            create_predict_pipeline(),
            namespace=model,
        )

    pipelines["report"] = create_report_pipeline()

    pipelines["__default__"] = sum(pipelines.values(), start=Pipeline([]))

    return pipelines
