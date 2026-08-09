"""
Pydantic API Request/Response Schemas
Experiment 08 — Image Retrieval / Visual QA System (MR23-1CS0436)
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class ImageMetadata(BaseModel):
    image_id: str
    title: str
    category: str
    resolution: str
    format: str
    labels: List[str]
    visual_description: str
    detected_objects: List[str]
    metadata_properties: Dict[str, Any]

class SearchRequest(BaseModel):
    query: str = Field(default="cybersecurity dashboard", description="Text or label search query for image catalog")
    category_filter: Optional[str] = Field(default="All", description="Category filter ('All', 'Cybersecurity Operations', 'Cloud Infrastructure', etc.)")
    top_k: int = Field(default=3, ge=1, le=10, description="Top K search results")

class ImageSearchResult(BaseModel):
    image: ImageMetadata
    similarity_score: float
    matched_features: List[str]

class SearchResponse(BaseModel):
    query: str
    category_filter: str
    results_count: int
    results: List[ImageSearchResult]
    retrieval_duration_ms: float

class VisualQARequest(BaseModel):
    image_id: str = Field(default="IMG-SOC-01", description="Target image ID to ask question about")
    question: str = Field(
        default="What critical alerts and monitored endpoint counts are displayed on this dashboard?",
        description="Natural language visual question about image content"
    )

class VisualQAResponse(BaseModel):
    image_id: str
    image_title: str
    question: str
    answer: str
    grounded_evidence: List[str]
    confidence_score: float
    detected_objects_referenced: List[str]
    vqa_duration_ms: float
