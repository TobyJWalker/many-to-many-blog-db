from lib.tag import Tag

class TagRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_by_post(self, id):
        rows = self._connection.execute(
            "SELECT tags.id, tags.name FROM tags " \
            "JOIN posts_tags on tags.id = posts_tags.tag_id " \
            "JOIN posts on posts.id = posts_tags.post_id " \
            "WHERE posts.id = %s", [id]
        )

        return [Tag(row['id'], row['name']) for row in rows]