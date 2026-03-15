from retrieval.embed import embed_text
from retrieval.filters import filter_by_tag
from retrieval.index_store import IndexStore
from retrieval.retriever import retrieve_top_k


def test_embed_text_returns_length_based_vector() -> None:
    assert embed_text("abc") == [3.0]


def test_index_store_round_trip() -> None:
    store = IndexStore()
    store.add({"id": 1})
    assert store.all() == [{"id": 1}]


def test_retrieve_top_k_limits_results() -> None:
    records = [{"id": 1}, {"id": 2}, {"id": 3}]
    assert retrieve_top_k(records, k=2) == [{"id": 1}, {"id": 2}]


def test_filter_by_tag_matches_expected_records() -> None:
    records = [{"tags": ["model"]}, {"tags": ["testing"]}]
    assert filter_by_tag(records, "testing") == [{"tags": ["testing"]}]
