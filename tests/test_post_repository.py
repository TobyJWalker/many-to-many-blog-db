from lib.post_repository import PostRepository
from lib.post import Post

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepository(db_connection)

    posts = repo.find_by_tag('coding')

    assert len(posts) == 4
    assert posts[0].title == 'How to use Git'
    assert posts[-1].title == 'SQL basics'