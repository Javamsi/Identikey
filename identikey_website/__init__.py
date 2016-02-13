from flask import (Flask, g, render_template, session, url_for, send_from_directory)
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.migrate import Migrate
import socket

app = Flask('__name__')
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
migrate = Migrate(app, db)

from blog import views
from user import views
    
if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True)