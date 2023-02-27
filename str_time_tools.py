import streamlit as st
from datetime import datetime


def check_space(string):
    # counter
    count = 0
    # loop for search each index
    for i in range(0, len(string)):
        # Check each char
        # is blank or not
        if string[i] == " ":
            count += 1
    return count

def run_sentiment_analysis(txt):
    length = "Total length:" + str(len(txt))
    length_utf8 = ", Total length(UTF8):" + str(len(txt.encode('utf-8')))
    space_count = ", Space count:" + str(check_space(txt))
    return length + length_utf8 + space_count

st.subheader('String Tool')

txt = st.text_area('Text to analyze', '''Input text here, Press Ctrl + Enter to apply''')
    
st.write("Result", run_sentiment_analysis(txt))

def get_datetime(timestamp):
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%Y/%m/%d %H:%M:%S")

def get_timestamp(date):
    format = "%Y/%m/%d %H:%M:%S"  # The format
    datetime_str = datetime.strptime(date, format)
    timestamp = int(round(datetime_str.timestamp()))
    return timestamp

def get_current_timestamp():
    return get_timestamp(get_current_date())

def get_current_date():
    #current date and time
    now = datetime.now()
    #date and time format: YYYY/mm/dd H:M:S
    format = "%Y/%m/%d %H:%M:%S"
    #format datetime using strftime() 
    return now.strftime(format)

st.subheader('Timestamp to datetime Tool')
current_timestamp = str(get_current_timestamp())
st.write('Current timestamp is ' + current_timestamp)
timestamp = st.text_input('Timestamp to datetime, input a timestamp ')
if timestamp != '':
    st.write('The date is ', get_datetime(int(timestamp)))#get_datetime(timestamp)
else:
    st.write(timestamp)

st.subheader('Datetime to timestamp Tool')
default_datetime = get_current_date()
st.write('Current datetime is ' + default_datetime)
date = st.text_input('Datetime to timestamp, input a date(format %Y/%m/%d %H:%M:%S) ')
if date != '':
    st.write('The date is ', str(get_timestamp(date)))