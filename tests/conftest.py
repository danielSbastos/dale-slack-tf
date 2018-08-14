# import os
# import tempfile

# import pytest

# import flask


# @pytest.fixture
# def client():
#     db_fd, flask.app.config['DATABASE'] = tempfile.mkstemp()
#     flask.app.config['TESTING'] = True
#     client = flask.app.test_client()

#     with flask.app.app_context():
#         # flask.init_db()

#     yield client

#     os.close(db_fd)
#     os.unlink(flask.app.config['DATABASE'])
