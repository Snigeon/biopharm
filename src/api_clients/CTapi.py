import requests

class ClinicalTrialsClient:
    BASE_URL = 'https://clinicaltrials.gov/api/v2'

    def fetch_studies(self, params):
        response = requests.get(f'{self.BASE_URL}/studies', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching studies: {response.status_code}")