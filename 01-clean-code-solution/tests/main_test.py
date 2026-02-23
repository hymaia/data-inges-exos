from src.main import is_lock


def test_is_lock():
    # Given
    input_text = [
        "#####",
        "##.##",
        ".#.##",
        "...##",
        "...#.",
        ".....",
        ".....",
    ]
    expected = True

    # When
    actual = is_lock(input_text)

    # Then
    assert actual == expected

def test_is_lock_with_key():
    # Given
    input_text = [
        ".....",
        "##.##",
        ".#.##",
        "...##",
        "...#.",
        ".....",
        "#####",
    ]
    expected = False

    # When
    actual = is_lock(input_text)

    # Then
    assert actual == expected

def test_is_lock_with_bad_input():
    # Given
    input_text = [
        "tgsgb",
        "##.##",
        ".#.##",
        "...##",
        "...#.",
        ".....",
        "zqchj",
    ]
    expected = False

    # When
    actual = is_lock(input_text)

    # Then
    assert actual == expected
