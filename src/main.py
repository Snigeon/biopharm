from services.data_fetcher import DataFetcher

fetcher = DataFetcher()
companies = fetcher.findCompanies('2024-10-05')
print(companies)