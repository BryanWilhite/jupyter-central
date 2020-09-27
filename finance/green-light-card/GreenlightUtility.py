from datetime import date
import pandas as pd

class GreenlightUtility:
    '''Shared members for Greenlight data processing'''

    @staticmethod
    def get_all_dates_in_month(first_day_of_month):
        '''return a pandas DataFrame of all the days in the month'''

        days_in_month = pd.Period(first_day_of_month, freq='D').days_in_month

        all_dates_in_month = [
            date(first_day_of_month.year, first_day_of_month.month, d) for d in range(1, days_in_month + 1)
        ]

        return pd.DataFrame({ 'Dates': all_dates_in_month })

    @staticmethod
    def get_csv_data_frame(filename):
        '''return a pandas DataFrame based on the specified file name'''

        data_frame = pd.read_csv(filename)
        return data_frame.fillna('')

    @staticmethod
    def get_transactions_data_frame(df_csv, starting_balance):
        '''return a pandas DataFrame of CSV transaction dates by rolling balance'''

        date_series = df_csv['Date']

        amount_series = df_csv['Amount']
        amount_series[0] += starting_balance

        transactions_series = amount_series.cumsum()

        d = {
            date_series.name: date_series,
            'Transactions': transactions_series
        }

        return pd.DataFrame(d)
