from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class VideoModel(db.Model):
#     id = db.Column(db.Interger, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     views = db.Column(db.Integer, nullable=False)
#     likes = db.Column(db.Integer, nullable=False)

#     def __repre__(self):
#         return f"Video(name = {name}, views = {views}, likes = {likes})"

# db.create_all() # create database after defining the model, the comment the line to dont do it multiple time

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)


videos = {

}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid...")

def abort_if_vidoe_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Video(Resource):

    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        "likes"
        "nanme"
        "views"
        abort_if_vidoe_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return  videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return  '', 204 # delete succesfully

api.add_resource(Video, "/video/<int:video_id>")



# names = {
#     "tim": {"age": 19, "gender": "male"},
#     "bill": {"age": 20, "gender": "male"},
#     }

# class  HelloWorld(Resource):

#     def get(self, name, age):
#         return names[name]

#     # def post(self):
#     #     return {"data": "Posted"}

# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")


if __name__ == '__main__':
    app.run(debug=True)

