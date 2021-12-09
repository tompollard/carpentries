from carpentries import values


def test_our_values():
    """
    Check that our values are correct.
    """

    our_values = "\n    At The Carpentries we...\n\n    - Act Openly\n    - Empower One Another\n    - Value All Contributions\n\n    We are...\n\n    - Always Learning\n    - Inclusive of All\n\n    We champion...\n\n    - People First\n    - Access for All\n    - Community Collaboration\n    - Strength through Diversity\n    "

    assert values.our_values() == our_values
