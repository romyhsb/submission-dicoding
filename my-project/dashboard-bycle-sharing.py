import pandas as pd
import streamlit as st 
#import matplotlib.pyplot as plt
import seaborn as sns


# membuat fungsi untuk memproses data_day dan melakukan groupin peminjaman sepeda per bulannya di setiap tahun
def create_grouped_per_year(df):
    grouped_per_year = df.groupby(['yr','mnth']).agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'})
    return grouped_per_year.reset_index()


def create_grouped_per_hour(df):
    grouped_per_hour = df.groupby('hr').agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'})
    return grouped_per_hour.sort_values(by='cnt', ascending=False)


def create_grouped_per_season(df):
    grouped_per_season = df.groupby('season').agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'})
    return grouped_per_season

# Load dataset
data_day = pd.read_csv('data_day.csv')
data_hour = pd.read_csv('data_hour.csv')

# membuat object dari data
sharing_bycycle_per_year = create_grouped_per_year(data_day)
sharing_bycycle_per_hour = create_grouped_per_hour(data_hour)
sharing_bycycle_per_season = create_grouped_per_season(data_day)


st.subheader("Sharing Bycycle Data for casual and registered sharing")
 
col1, col2 = st.columns(2)
# Visualisasi
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.lineplot(
    y="cnt", 
    x="mnth",
    hue='yr',
    data=sharing_bycycle_per_year.sort_values(by="cnt", ascending=False)
    
)
    ax.set_title("Peminjaman sepeda per bulan", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.lineplot(
    y="cnt", 
    x="hr",
    data=sharing_bycycle_per_hour.sort_values(by="cnt", ascending=False)
    
)
    ax.set_title("Peminjaman sepeda setiap jam", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Barchart untuk peminjaman sepeda per seasonnya
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="season", 
    y="cnt",
    data=sharing_bycycle_per_season.sort_values(by="cnt", ascending=False),
    ax=ax
)
ax.set_title("Peminjaman sepeda setiap musimnya", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
