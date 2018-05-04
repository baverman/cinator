from flaskish import Flaskish

import settings

app = Flaskish('cinator',
               root_path=settings.ROOT,
               static_url_path='/static',
               template_folder='web/template',
               static_folder='web/assets')

app.jinja_options = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'autoescape': True,
}

# Provide additional context for errors inside request scope
if settings.SENTRY:
    from raven.contrib.flask import Sentry
    sentry = Sentry(app, client=settings.sentry_client)

# close session after request
from .. import db
app.teardown_request(db.remove_session)

# import views
from . import views
from . import template_api

@app.context_processor
def template_context():
    return {
        'api': template_api
    }
