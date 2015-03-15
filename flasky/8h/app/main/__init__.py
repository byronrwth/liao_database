<<<<<<< HEAD
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
=======
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
>>>>>>> 8708ed7762be8c036b56ef197d7060bc34628865
