import math
import streamlit as st

from routes.upload import Upload
from routes.charts import Charts
from routes.maps import Maps

def main():
    # Set the page title and icon
    st.set_page_config(
        page_title='My Streamlit App',
        page_icon=':chart_with_upwards_trend:'
    )

    # Define the menu options
    menu = [
        'Upload',
        'Charts',
        'Map',
    ]

    # Display the menu
    choice = st.sidebar.radio('Select a page', menu)

    # Show the appropriate page based on the user's menu choice
    if choice == 'Upload':
        Upload()
    elif choice == 'Charts':
        Charts()
    elif choice == 'Map':
        Maps()


if __name__ == '__main__':
    main()
