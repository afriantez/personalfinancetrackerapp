import sqlite3
import pandas as pd

def get_monthly_summary(month, year):
    conn = sqlite3.connect('finance.db')
    query = '''
        SELECT type, category, SUM(amount) as total
        FROM transactions
        WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY type, category
    '''
    df = pd.read_sql_query(query, conn, params=(month, year))
    conn.close
    return df