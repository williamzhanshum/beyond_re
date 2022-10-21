from flask_app import app
from flask_app.controllers import users, properties, tenants, vendors


if __name__=="__main__":
    app.run(debug=True)