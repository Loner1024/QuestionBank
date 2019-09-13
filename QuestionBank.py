from app import app
from app.model import User


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)