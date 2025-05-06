# The test cases. Start by importing pytest and SentimentAnalyzer.

import pytest
from sentiment_analyzer import SentimentAnalyzer

# Initialize the model once for all tests
analyzer = SentimentAnalyzer("microsoft/phi-2")

# Create 3 test cases.
@pytest.mark.parametrize("headline,expected", [
    # Apple getting record profits is a good thing, so the AI should return Positive.
    ("Apple reports record profits in Q2", "Positive"),
    # Worsening humanitarian crisis is a bad thing, so the AI should return Negative.
    ("UN warns of worsening humanitarian crisis in Sudan", "Negative"),
    # As it is unchanged, it is a pure neutral thing, so the AI should return Neutral.
    ("Federal Reserve leaves interest rates unchanged", "Neutral"),
])
def test_sentiment_analysis(headline, expected):
    result = analyzer.analyze_sentiment(headline)
    # If any test cases do not work, let the user know. It will give the expected result and the result the AI actually gave. This should almost never be called though.
    assert result == expected, f"Expected {expected} but got {result} for: '{headline}'"