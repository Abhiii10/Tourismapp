from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Nepal Rural Tourism Recommendation API"
    project_version: str = "2.0.0"

    # SBERT model - lightweight enough for local/offline backend use.
    model_name: str = "all-MiniLM-L6-v2"

    # Pipeline sizes.
    retrieve_top_k: int = 30
    final_top_k: int = 10

    # Stage-1 retrieval weights.
    retrieval_semantic_weight: float = 0.72
    retrieval_activity_weight: float = 0.18
    retrieval_category_weight: float = 0.10

    # Stage-2 reranking weights.
    semantic_weight: float = 0.50
    collaborative_weight: float = 0.20
    contextual_weight: float = 0.30

    # Contextual feature weights. These intentionally sum to 1.0 so the
    # contextual block stays normalized before it is blended into the final score.
    activity_weight: float = 0.22
    vibe_weight: float = 0.14
    season_weight: float = 0.16
    budget_weight: float = 0.16
    accessibility_weight: float = 0.10
    family_weight: float = 0.08
    accommodation_weight: float = 0.14

    # Diversity limits after reranking.
    max_results_per_district: int = 2
    max_results_per_category: int = 2

    # Paths.
    root_dir: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = root_dir / "data"

    destinations_file: Path = data_dir / "destinations.json"
    accommodations_file: Path = data_dir / "accommodations.json"
    interactions_file: Path = data_dir / "interactions.json"

    class Config:
        env_file = ".env"


settings = Settings()
