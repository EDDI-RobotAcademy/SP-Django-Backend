import pandas as pd

# 중복되는데이터 첫번째것만 빼고 삭제하기

def load_data(file_path):
    return pd.read_excel(file_path)

def remove_duplicates(df):
    # accountId와 productId가 동일한 행들 중에서 하나만 남기고 제거
    unique_df = df.drop_duplicates(subset=['accountId', 'travelId'], keep='first')
    return unique_df

def save_data(df, file_path):
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Saved unique data to {file_path}")


input_file = "preprocessed_orders_data.xlsx"
output_file = "orders_data_after_drop_duplication.xlsx"

df = load_data(input_file)
unique_df = remove_duplicates(df)
save_data = save_data(unique_df, output_file)
