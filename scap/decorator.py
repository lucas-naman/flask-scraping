from flask import request
from functools import wraps

def api_key_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'X-Api-Key' not in request.headers or request.headers['X-Api-Key'] != 'zozo':
            return "you need to give me the api key", 401

        return f(*args, **kwargs)

    return decorated_function