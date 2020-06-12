import json


def json_body(request):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)
