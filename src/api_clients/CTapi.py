import requests

class ClinicalTrialsClient:

    def fetch_studies(self, params):
        response = requests.get('https://clinicaltrials.gov/api/v2/studies', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching studies: {response.status_code}")