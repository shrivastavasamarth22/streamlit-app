import streamlit as st

def largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title('Find the Largest Number')
    
    st.write('Enter three numbers')
    num1 = st.number_input('Enter the first number')
    num2 = st.number_input('Enter the second number')
    num3 = st.number_input('Enter the third number')
    
    if st.button('Find the largest number'):
        largest = largest_number(num1, num2, num3)
        st.write(f"The largest number is {largest}")
        

if __name__ == '__main__':
    main()