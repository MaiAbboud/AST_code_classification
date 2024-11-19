import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from numpy import inf

'''
In order to run the analysis, it is necessary a database with the datasets.
It is possible to obtain a copy of it at https://www.reflection.uniovi.es/bigcode/download/2022/java-patterns/
'''
POSTGRES_USERNAME = "<USER_NAME>"
POSTGRES_PASSWORD = "<USER_NAME>"
POSTGRES_ADDRESS = "<HOST>"
POSTGRES_PORT = 5432
POSTGRES_DBNAME = "finaldataset"


def get_postgresql_engine():
    return create_engine(
        'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,
                                                                                password=POSTGRES_PASSWORD,
                                                                                ipaddress=POSTGRES_ADDRESS,
                                                                                port=POSTGRES_PORT,
                                                                                dbname=POSTGRES_DBNAME))


def get_bin(bins, value):
    for x, y in bins:
        if value >= x:
            if y == 100 and value < 100:
                return "[" + str(x) + "_" + str(y) + ")"
            if y == 100 and value == 100:
                return "100_100"
            if value < y:
                return "[" + str(x) + "_" + str(y) + ("]" if y == inf else ")")
    return "unknown"


def create_bins(df, column, bins):
    return df[column].apply(lambda value: get_bin(bins, value))


def discretize_columns(df, columns):
    for k in columns:
        df[k] = create_bins(df, k, columns[k])


def get_statistics(df, columns, size):
    total = len(df.index)
    result = df.groupby(columns) \
        .size() \
        .reset_index(name='count') \
        .sort_values(['count'], ascending=False) \
        .head(size)
    result['percentage'] = (result['count'] * 100) / total
    return result.to_string(index=False) + '\n'


def execute_query(query):
    engine = get_postgresql_engine()
    return pd.read_sql_query(query, engine)
