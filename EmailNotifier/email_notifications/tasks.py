from application import app


@app.task
def ping():
    print('pong!')
