# 전처리를 위해 survey 엑셀과 orders 엑셀을 병합하는 코드
import pandas as pd

def load_data(orders_file, survey_file):
    orders_df = pd.read_excel(orders_file)
    survey_df = pd.read_excel(survey_file)
    return orders_df, survey_df

def merge_data(orders_df, survey_df):
    # accountId를 통해 데이터프레임을 합침 >> (우리의 각 엑셀파일은) accountId만 공통변수기 때문에 accountId로만 merge
    merged_df = pd.merge(orders_df, survey_df, on=['accountId'])
    return merged_df

def preprocess_data(merged_df):
    # merged된 dataframe과 viewcount의 상관관계 따지기 >> 안 나온 경우는 0으로 채움
    # 우리는 각 survey의 field 하나하나 해주면 될 듯?
    merged_df['age'] = merged_df['age'].fillna(0)
    return merged_df

def export_data_to_excel(df, filePath):
    df.to_excel(filePath, index=False, engine='openpyxl')
    print(f"전처리 완료 : {filePath}")


orders_info_file = "travel_orders_data.xlsx"
survey_info_file = "survey_data.xlsx"
output_file = "preprocessed_orders_data.xlsx"

orders_df, survey_df = load_data(orders_info_file, survey_info_file)
merged_df = merge_data(orders_df, survey_df)
preprocessed_df = preprocess_data(merged_df)
export_data_to_excel(preprocessed_df, output_file)