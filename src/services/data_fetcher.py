from api_clients import ClinicalTrialsClient
from api_clients import StockMarketClient
import requests
from config import key_

class DataFetcher:
    
    def get_ticker(self, company_name):
    # Yahoo Finance API endpoint for searching companies
        yfinance_url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        
        # Parameters for the API request
        params = {
            "q": company_name,
            "quotes_count": 1,  # Limit to one result
            "country": "United States"
        }

        # Make the request to the Yahoo Finance API
        try:
            response = requests.get(url=yfinance_url, params=params, headers={'User-Agent': user_agent})
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the JSON response
            data = response.json()

            # Extract the ticker symbol from the response
            if data['quotes']:
                company_code = data['quotes'][0]['symbol']
                return company_code
            else:
                return None  # No ticker found
        except requests.exceptions.RequestException as e:
            print(f"Error fetching ticker: {e}")
            return None
    
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
            company = {'company' : '', 'intervention' : ''}
            sponsor = study.get('protocolSection', {}).get('sponsorCollaboratorsModule', {}).get('leadSponsor', {}).get('name')
            if self.get_ticker(sponsor):
                company['company'] = sponsor
                company['intervention'] = study.get('protocolSection', {}).get('armsInterventionsModule', {}).get('interventions', {})
                companies.append(company)
        return companies

    
    

