def create_report(predictions: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    """Count yes and no predictions separately for each input key."""
    return {
        key: {"yes": outcomes.count("yes"), "no": outcomes.count("no")}
        for key, outcomes in predictions.items()
    }
