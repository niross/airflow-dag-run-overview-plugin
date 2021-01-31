from airflow.models import DagBag
from airflow.utils.db import provide_session
from airflow.utils.state import State
from flask import Blueprint
from flask_admin import BaseView, expose
from flask_login import login_required

dro_blueprint = Blueprint(
    'dag_run_overview_plugin',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/dro_plugin',
)


class DROView(BaseView):
    @expose('/')
    @provide_session
    @login_required
    def test(self, session=None):

        dags = [
            dag
            for dag in DagBag(include_examples=False).dags.values()
            if not dag.is_paused and dag.get_last_dagrun() is not None
        ]
        return self.render('main.html', dags=dags, State=State)


dro_view = DROView(category='Dag Runs', name='Dag Run Overview')
