from lib.post import Post

def test_init():
    post = Post(1, 'title')
    assert post.id == 1
    assert post.title == 'title'

def test_repr():
    post = Post(1, 'title')
    assert repr(post) == 'Post(1, title)'

def test_eq():
    post1 = Post(1, 'title')
    post2 = Post(1, 'title')
    assert post1 == post2