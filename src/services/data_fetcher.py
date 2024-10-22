from api_clients.CTapi import ClinicalTrialsClient
from api_clients.Stockapi import StockMarketClient
import requests
from config import key_

class DataFetcher:
    
    def get_ticker(self, company_name):
        # god help me
        return
    
    def findCompanies(self, completionDate):

        study_params = {
            'format' : 'json',
            'pageSize' : 1000,
            'fields' : 'LeadSponsorName,LeadSponsorClass,Phase,LocationCountry,InterventionName',
            'filter.advanced' : 'AREA[CompletionDate]' + completionDate
        }

        studies = ClinicalTrialsClient.fetch_studies(self, params=study_params)
        companies = []
        for study in studies.get('studies', []):
            company = {'company' : '', 'ticker' : '', 'intervention' : ''}
            sponsor = study.get('protocolSection', {}).get('sponsorCollaboratorsModule', {}).get('leadSponsor', {}).get('name')
            if self.get_ticker(sponsor):
                company['company'] = sponsor
                company['intervention'] = study.get('protocolSection', {}).get('armsInterventionsModule', {}).get('interventions', {})[0]
                company['ticker'] = self.get_ticker(sponsor)
                companies.append(company)
        return companies

    
    

