from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

posts = {
    '1' : {
        'title' : 'Hello World',
        'content' : 'Lorem ipsum'
    },
    '2' : {
        'title' : 'Hello World',
        'content' : 'Lorem ipsum'
    }
}

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')

class Post(Resource):
    # retrieve single post
    # curl http://127.0.0.1:5000/post/1
    def get(self, post_id):
        return posts[post_id]

    # delete post
    # curl http://127.0.0.1:5000/post/1 -X DELETE -v
    def delete(self, post_id):
        del posts[post_id]
        return '', 204

    # update post
    # curl http://127.0.0.1:5000/post/1 -d "title=New" -d "content=Latest content" -X PUT -v
    def put(self, post_id):
        args = parser.parse_args()
        post = {'title' : args['title'], 'content' : args['content']}
        posts[post_id] = post
        return post, 201

class AllPosts(Resource):
    def get(self):
        return posts
    # curl http://127.0.0.1:5000/posts -d "title=Post 3" -d "content=This is third post" -X POST -v
    def post(self):
        args = parser.parse_args()
        post_id = int(max(posts.keys()))+1
        posts[post_id] = {'title': args['title'], 'content' : args['content']}
        return posts[post_id], 201
    
api.add_resource(Post, '/post/<post_id>')
api.add_resource(AllPosts, '/posts')

if __name__ == '__main__':
    app.run(debug=True)