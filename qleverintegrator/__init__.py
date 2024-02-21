import requests
from pydantic import BaseModel
from requests import Session


class ActionError(BaseException):
    pass


class QleverIntegrator(BaseModel):
    endpoint: str = "https://qlever.cs.uni-freiburg.de/api/wikidata"
    session: Session = requests.session()

    def execute_query(self, query: str, action: str = "json_export"):
        if action not in ["tsv_export", "json_export"]:
            raise ActionError(f"Action {action} is not supported")
        params = {
            'query': query,
            'action': 'json_export',
        }

        response = self.session.get('https://qlever.cs.uni-freiburg.de/api/wikidata', params=params)