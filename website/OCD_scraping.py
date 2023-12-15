from datetime import datetime
import requests
import json

class scraping:
        
    def get_data(symbol):
        url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.nseindia.com/",
        }

        try:
            print("started")
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                current_date = datetime.now()
                PE_data_list = []
                CE_data_list = []
                # Extracting all data from PE and CE options
                option_data = data['records']['data']
                for option in option_data:
                    
                    # Extracting PE data if available
                    pe_data = option.get('PE')
                    if pe_data:
                        PE_data_list.append(pe_data) 

                    # Extracting CE data if available
                    ce_data = option.get('CE')
                    if ce_data:
                        CE_data_list.append(pe_data)
            else:   
                print(f"Error: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")
        

        pe_data_json=json.dumps(PE_data_list)
        ce_data_json= json.dumps(CE_data_list)

        pe_json = json.loads(pe_data_json)
        ce_json = json.loads(ce_data_json)
        
        column_names = list(pe_data.keys())


        updation_time = current_date.strftime("%Y-%m-%d")
        print("DATA IS SCRAPED ")
        return  pe_json,ce_json,updation_time,column_names
    
    

