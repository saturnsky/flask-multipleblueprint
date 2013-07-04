flask-multipleblueprint
=======================

Decorate function using multiple blueprints at once.

installation
------------

You can install the package using pip:

    $ pip install flask-multipleblueprint

Usage
-----

    import flask
    from flask_multipleblueprint import MultipleBlueprint

    foo_blueprint = flask.Blueprint('foo', __name__, url_prefix='/foo')
    bar_blueprint = flask.Blueprint('bar', __name__, url_prefix='/bar')

    multiple_blueprint = MultipleBlueprint(foo_blueprint, bar_blueprint)

    @multiple_blueprint.route('/')
    def index():
        return flask.render_template('index.html')

It's works perfectly alternate below one.

    import flask
    from flask_multipleblueprint import MultipleBlueprint

    foo_blueprint = flask.Blueprint('foo', __name__, url_prefix='/foo')
    bar_blueprint = flask.Blueprint('bar', __name__, url_prefix='/bar')

    @foo_blueprint.route('/')
    @bar_blueprint.route('/')
    def index():
        return flask.render_template('index.html')

Good Luck!
