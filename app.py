import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Url, db_drop_and_create_all


def insert_readings(urlValue):
    toBeInserted = Url(urlValue)
    toBeInserted.insert()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    """ uncomment at the first time running the app """
    # db_drop_and_create_all()

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'Hello,hello, World!'})


    @app.route("/movies", methods=['GET', 'POST'])
    def get_movies():
        if(request.method == 'POST'):
            #do this
            reqs = request.get_json()
            if not reqs:
                raise JsonRequiredError()
            try:
                reqs['name']
                insert_readings(reqs['name'])
                return HelloResult(name=reqs['name'])
            except KeyError:
                raise JsonInvalidError()
        else:
            try:
                urls = Url.query.order_by(Url.id).all()
                url=[]
                url=[mov.url for mov in urls]
                return jsonify(
                    {
                        "success": True,
                        "url": url
                    }
                ), 200
            except:
                abort(500)


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500
    return app

app = create_app()
if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port,debug=True)
