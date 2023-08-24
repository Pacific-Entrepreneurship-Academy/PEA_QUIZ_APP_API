from app import app, db,api
from app.models import Admin

app.register_blueprint(api)

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Admin':Admin }