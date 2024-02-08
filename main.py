import streamlit as st

from streamlit_option_menu import option_menu 

import Hello , Check_Prizes, Analytics

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)


class MultiApp():

    def __init__(self):
        self.apps = []

    def add_app(self , title , function):
        self.apps.append({'title':title,
                          'function':function
                        })
        
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title= 'services',

                options = ['Hello' , 'Check_Prizes', 'Analytics']
                )
            
        if app == 'Hello':

            Hello.app()
                
        if app == 'Check_Prizes':

            Check_Prizes.app()

        if app == 'Analytics':

            Analytics.app()
    run()



