import streamlit as st
from arabic_support import support_arabic_text
import funcs

# Support Arabic text alignment in all components
# support_arabic_text(all=True)

keys_list = list(st.session_state.keys())
data_file = funcs.read_data()


def add_todo():
    new_todo = st.session_state['todo_input'] + '\n'
    funcs.new_todo(new_todo)
    st.session_state['todo_input'] = ''


st.title("Hello world!")
st.subheader("This is my todo app..")

st.text_input(label='', label_visibility="hidden", key='todo_input', placeholder='Enter your todo here',
              on_change=add_todo)

for index, data in enumerate(data_file):
    checkbox = st.checkbox(data, key=index)
    if checkbox:
        data_file.pop(index)
        funcs.write_data(data_file)
        del st.session_state[index]
        st.rerun()
