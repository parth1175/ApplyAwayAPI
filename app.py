import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Url, db_drop_and_create_all


def insert_readings(urlValue, companyName, description):
    toBeInserted = Url(urlValue, companyName, description)
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
            # reqs = request.get_json()
            reqs = request.get_data().decode('utf-8')
            # print(reqs)
            # if not reqs:
            #     raise JsonRequiredError()
            try:
                # reqs['name']
                reqs[:10]
                # make an object from script here
                # call methods on the object down in the insert_readings() functions
                # insert_readings(reqs['name'], reqs['html'][:15], reqs['html'][16:31])
                insert_readings(reqs[:5], reqs[5:10], reqs[10:15])

                # reqs['html'][:15], reqs['html'][16:31] are temporary placeholders

                # insert the url into the database
                # send the html text to the script for processing and that script will then insert into the database
                return jsonify(
                    {
                        "success": True,
                        "url": reqs[:10]
                    }
                ), 200
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
    # migrate = Migrate(app, db)
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port,debug=True)
