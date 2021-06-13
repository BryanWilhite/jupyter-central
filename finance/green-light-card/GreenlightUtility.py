import pandas as pd

from datetime import datetime

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = 'all'


class GreenlightUtility:
    '''Shared members for Greenlight data processing'''

    @staticmethod
    def get_csv_data_frame(filename):
        '''return a pandas DataFrame based on the specified file name'''

        date_series_name = 'Date'
        data_frame = pd.read_csv(filename, parse_dates=[date_series_name])
        date_series = data_frame[date_series_name].apply(
            lambda i: i.strftime('%Y-%m-%d'))
        data_frame.insert(loc=0, column='CsvIndex', value=date_series)

        return data_frame.fillna('')

    @staticmethod
    def get_balance_data_frame(df_csv, starting_balance):
        '''return a pandas DataFrame of CSV transaction dates by rolling balance'''

        csv_index_series = df_csv['CsvIndex']
        amount_series = pd.Series(df_csv['Amount'])
        amount_series[0] += starting_balance

        transactions_series = amount_series.cumsum()

        return pd.DataFrame({
            csv_index_series.name: csv_index_series,
            'Balance': transactions_series
        })

    @staticmethod
    def get_balance_eod_data_frame(df_balances):
        '''return the EOD balances of the specified `DataFrame`'''

        return df_balances.groupby('CsvIndex', as_index=True, sort=True).last()

    @staticmethod
    def get_daily_balance_data_frame(first_day_of_month, starting_balance, df_eod_balances):
        '''return a pandas DataFrame of all the days in the month by rolling balance'''

        days_in_month = pd.Period(first_day_of_month, freq='D').days_in_month
        transactions = df_eod_balances.to_dict()['Balance']

        collection = {}
        balance = starting_balance

        for d in range(1, days_in_month + 1):

            day = datetime(first_day_of_month.year,
                           first_day_of_month.month, d)

            balance = transactions.get(day.strftime('%Y-%m-%d'), balance)

            collection[day] = balance

        return pd.DataFrame({
            'Dates': list(collection.keys()),
            'Balance': list(collection.values())
        })

    @staticmethod
    def get_final_data_frame(averages):
        '''return the collected averages'''

        collection = dict(averages)

        return pd.DataFrame({
            'Dates': list(collection.keys()),
            'Balance': list(collection.values())
        })

    @staticmethod
    def get_first_day_of_month(year, month):
        '''return the first day of the specified year and month'''

        return datetime(year, month, 1)
