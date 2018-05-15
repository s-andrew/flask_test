from app import app

from controllers.hello import hello
from controllers.task_api import *
from controllers.error_handlers import *


if __name__ == '__main__':
    app.run(debug=True)