from movies import movies
from comparisons import sort_by_year, sort_by_title

# # Expected test output of test #1
# expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
#
# # Expected test output of test #2
# expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];

def test_by_year():
    actual = sort_by_year(movies)
    expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected1

def test_sort_by_title():
    actual = sort_by_title(movies)
    expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento",
                 "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];
    assert actual == expected2
