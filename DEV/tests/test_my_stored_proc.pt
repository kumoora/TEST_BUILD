import pytest
from sp.my_stored_proc import process_score
def test_process_score_excellent():
    assert process_score(95) == "Excellent"
def test_process_score_good():
    assert process_score(80) == "Good"
def test_process_score_average():
    assert process_score(65) == "Average"
def test_process_score_poor():
    assert process_score(45) == "Poor"
def test_process_score_invalid_low():
    with pytest.raises(ValueError, match="Score must be between 0 and 1000"):
        process_score(-5)
def test_process_score_invalid_high():
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        process_score(150)
