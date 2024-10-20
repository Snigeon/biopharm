import requests
import json
from pprint import pprint as pp
url = 'https://clinicaltrials.gov/api/v2'
study_params = {
    'format' : 'json',
    'pageSize' : 100,
    'sort' : 'LastUpdatePostDate',
    'filter.advanced' : 'AREA[CompletionDate]2024-10-05',
    'fields' : 'NCTId,LocationCountry,LeadSponsorClass'
}

stats_params = {

}
pp(requests.get(url + '/version').json())
studies = requests.get(url + '/studies', params=study_params)
pp(studies)
stud = studies.json()
if studies.status_code == 200:
    # Parse the JSON response
    data = studies.json()

    # Filter for studies in the United States
    us_studies = []
    for study in data.get('studies', []):
        locations = study.get('protocolSection', {}).get('contactsLocationsModule', {}).get('locations', [])
        for location in locations:
            if location.get('country') == 'United States':
                us_studies.append(study)
                break  # No need to check further locations for this study
    industry_studies = []
    for study in data.get('studies', []):
        leadSponsor = study.get('protocolSection', {}).get('sponsorCollaboratorsModule', {}).get('leadSponsor', [])
        for location in locations:
            if leadSponsor.get('class') == 'INDUSTRY':
                industry_studies.append(study)

    # Pretty print the filtered studies
    pp(industry_studies)
class AMOGUS:
    def __init__(self):
        pass


amogus = AMOGUS()