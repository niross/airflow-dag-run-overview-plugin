from airflow.plugins_manager import AirflowPlugin

from .plugin import (
    dro_blueprint,
    dro_view,
)


class DagRunOverviewPlugin(AirflowPlugin):
    name = "dag_run_overview"

    admin_views = [dro_view]
    flask_blueprints = [dro_blueprint]
