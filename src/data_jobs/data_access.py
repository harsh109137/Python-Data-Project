from datasets import load_dataset
import pandas as pd
from pathlib import Path


def load_data():

    """
    Load dataset either from local parquet file
    or from HuggingFace dataset if not found locally.
    """

    project_root = Path(__file__).resolve().parents[2]

    data_path = project_root / "data" / "raw_data" / "job_postings_data.parquet"

    if data_path.exists():

        df = pd.read_parquet(data_path)

    else:

        dataset = load_dataset("lukebarousse/data_jobs")
        df = dataset["train"].to_pandas()

    return df