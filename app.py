import os
import base64
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    weather_dir = './weather'

    station_info = pd.read_csv('./input/관측지점코드.csv')
    location_dict = dict(zip(station_info['지점명'], station_info['지점']))

    location_list = list(location_dict.keys())

    selected_location = st.selectbox('지역 선택', location_list)
    location_dir = os.path.join(weather_dir, str(location_dict[selected_location]))
    exists_years = os.listdir(location_dir)
    exists_years = (sorted(exists_years, reverse=True))

    selected_year = st.selectbox('연도 선택', exists_years)
    year_dir = os.path.join(location_dir, str(selected_year))
    selected_df = pd.concat([pd.read_csv(os.path.join(year_dir, file))for file in os.listdir(year_dir)])
    df =selected_df.sort_values(by=['month', 'day'])


    df_pivot = df.pivot_table(index='month', columns='day', values='tavg')

    fig = plt.figure(figsize=(20, 8))
    ax = sns.heatmap(df_pivot, cmap='coolwarm', linewidths=1, square=True, annot=True)
    st.pyplot(fig)

    st.write(df)

if __name__ == '__main__':
    main()
