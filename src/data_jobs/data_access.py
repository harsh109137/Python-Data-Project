from datasets import load_dataset
import pandas as pd
from pathlib import Path


def get_project_root():
    """
    Returns the project root directory.
    """
    return Path(__file__).resolve().parents[2]


def load_data():
    """
    Load dataset.
    Priority:
    1. Local parquet file (faster)
    2. Download from HuggingFace if not found
    """

    project_root = get_project_root()

    raw_data_dir = project_root / "data" / "raw_data"
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    data_path = raw_data_dir / "job_postings_data.parquet"

    if data_path.exists():

        df = pd.read_parquet(data_path)

    else:

        dataset = load_dataset("lukebarousse/data_jobs")
        df = dataset["train"].to_pandas()

        # save locally for future runs
        df.to_parquet(data_path)

    return df

def clean_data():
    """
    Accessing already cleaned data
    """
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "processed_data" / "job_postings_data_cleaned.parquet"

    df = pd.read_parquet(data_path)

    return df
