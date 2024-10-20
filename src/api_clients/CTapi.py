import requests
import json
from pprint import pprint as pp
url = 'https://clinicaltrials.gov/api/v2'
study_params = {
    'format' : 'json',
    'pageSize' : 1000,
    'sort' : 'LastUpdatePostDate',
    'filter.advanced' : 'AREA[CompletionDate]2024-10-06',
    'fields' : 'NCTId,LocationCountry,LeadSponsorClass,LeadSponsorName'
}

stocks_params = {

}
pp(requests.get(url + '/version').json())
studies = requests.get(url + '/studies', params=study_params)
pp(studies)
stud = studies.json()
if studies.status_code == 200:
    # Parse the JSON response
    data = studies.json()

    # Filter for studies that fit criteria
    industry_studies = []
    for study in data.get('studies', []):
        leadSponsor = study.get('protocolSection', {}).get('sponsorCollaboratorsModule', {}).get('leadSponsor', [])
        locations = study.get('protocolSection', {}).get('contactsLocationsModule', {}).get('locations', [])
        for location in locations:
            if leadSponsor.get('class') == 'INDUSTRY' and location.get('country') == 'United States':
                industry_studies.append(leadSponsor)
                industry_studies.append(study.get('protocolSection', {}).get('identificationModule', {}).get('nctId', []))

    # Pretty print the filtered studies
    pp(industry_studies)