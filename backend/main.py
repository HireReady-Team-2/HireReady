import sys
import traceback

def create_error_app(error_msg: str):
    async def app(scope, receive, send):
        if scope['type'] == 'http':
            await send({
                'type': 'http.response.start',
                'status': 500,
                'headers': [(b'content-type', b'text/plain')],
            })
            await send({
                'type': 'http.response.body',
                'body': error_msg.encode('utf-8'),
            })
    return app

try:
    from api import app
except Exception as e:
    fatal_error = traceback.format_exc()
    print("CRITICAL IMPORT ERROR IN VERCEL SERVERLESS FUNCTION:\n", fatal_error)
    app = create_error_app(fatal_error)
