import boto3
import pandas as pd
import datetime

# Initialize AWS Cost Explorer client
client = boto3.client('ce')

def get_cost_data(start_date, end_date):
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start_date, 'End': end_date},
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )
    return response

def parse_cost_data(response):
    data = []
    for result in response['ResultsByTime']:
        date = result['TimePeriod']['Start']
        for group in result['Groups']:
            service = group['Keys'][0]
            cost = float(group['Metrics']['UnblendedCost']['Amount'])
            data.append([date, service, cost])
    return pd.DataFrame(data, columns=['Date', 'Service', 'Cost'])

if __name__ == "__main__":
    # Set date range (last 7 days)
    end_date = datetime.date.today().strftime('%Y-%m-%d')
    start_date = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    
    response = get_cost_data(start_date, end_date)
    df = parse_cost_data(response)
    
    # Save to CSV
    df.to_csv("aws_cost_report.csv", index=False)
    print("AWS cost report saved to aws_cost_report.csv")
