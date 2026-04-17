def category_analysis(df):
    return df.groupby('category')['amount'].sum()

def monthly_analysis(df):
    return df.groupby('month')['amount'].sum()
