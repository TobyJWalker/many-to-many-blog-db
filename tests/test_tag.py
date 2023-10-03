from lib.tag import Tag

def test_init():
    tag = Tag(1, 'coding')
    assert tag.id == 1
    assert tag.name == 'coding'

def test_repr():
    tag = Tag(1, 'coding')
    assert repr(tag) == 'Tag(1, coding, None)'

def test_eq():
    tag1 = Tag(1, 'coding')
    tag2 = Tag(1, 'coding')
    assert tag1 == tag2