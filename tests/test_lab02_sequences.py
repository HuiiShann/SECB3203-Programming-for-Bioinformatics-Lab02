import pytest
from lab02_sequences import find_motif

def test_find_motif_normal():
    """Test normal"""
    assert find_motif("ATCGATCG","CG") == [2,6]

def test_find_motif_boundary():
    """Test boundary"""
    assert find_motif("aAaA", "aA") == [0,1,2]

def test_find_motif_invalid_input():
    """Test invalid input"""
    with pytest.raises(ValueError, match="Motif is empty!"):
        find_motif("ATCG", "")