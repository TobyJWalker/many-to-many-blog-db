from lib.tag_repository import TagRepository
from lib.tag import Tag

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = TagRepository(db_connection)

    tags = repo.find_by_post(2)

    assert len(tags) == 2
    assert tags == [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ]
