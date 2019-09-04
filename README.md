# Flask-API
Restful API into Flask with help of module Flask-Restful


>  Retrieve single post (GET)

``` curl http://127.0.0.1:5000/post/1 ```

>  Delete post (DELETE)

``` curl http://127.0.0.1:5000/post/1 -X DELETE -v ```

>  Update post (PUT)

``` curl http://127.0.0.1:5000/post/1 -d "title=New" -d "content=Latest content" -X PUT -v ```

>  Add post (POST)

``` curl http://127.0.0.1:5000/posts -d "title=Post 3" -d "content=This is third post" -X POST -v ```
