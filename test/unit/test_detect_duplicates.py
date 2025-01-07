import pytest
from src.util.detector import detect_duplicates
from src.util.parser import Article
# develop your test cases here

# Test case 1: No data found (“ ”)
@pytest.mark.unit
def test_no_data():
    with pytest.raises(ValueError, match="The input data does not contain enough articles to detect duplicates."):
        detect_duplicates("")

# Test case 2: One article (@article{key1,})
@pytest.mark.unit
def test_one_article():
    data = "@article{key1,}"
    with pytest.raises(ValueError, match="The input data does not contain enough articles to detect duplicates."):
        detect_duplicates(data)


# Test case 3: Multiple articles with duplicate
@pytest.mark.unit
def test_articles_with_duplicate():
    data = """
    @article{key1, doi={10.1007}}
    @article{key2, doi={10.2000}}
    @article{key1, doi={10.1007}}
    @article{key3, doi={10.3000}}
    @article{key4,}
    """
    result = detect_duplicates(data)
    assert len(result) == 1
    assert result == [Article(key="key1", doi="10.1007")] # defect in the code, the expected result should be [Article(key="key1", doi="10.1007")]

# Test case 4: Multiple articles that are unique
@pytest.mark.unit
def test_unique_articles():
    data = """
    @article{key1, doi={10.1007}}
    @article{key2, doi={10.1007}}
    @article{key3, doi={10.1007}}
    @article{key4, doi={10.1007}}
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 0
