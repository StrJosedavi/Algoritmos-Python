class User():

    def __init__(self, postId, id, name, email, body):
        self.postId = postId
        self.id = id
        self.name = name
        self.email = email
        self.body = body

    def __str__(self):
        return f"User(postId={self.postId}, id={self.id}, name={self.name}, email={self.email}, body={self.body})"
