## Unlike other python code I wrote before this is same code but implemented DataFrame from pandas and exported dataset to excel file. 

import pandas as pd
file = open('D:/Gaurav - Docs/Projects/Python/Fetch Table Data/baby1998.html', 'r')
r = file.read()
ref = str(r)

def data(ref):
	### Rank
	find_tr = ref.find('<tr align="right"')
	find_td = ref.find('<td>', find_tr + 1)
	find_td_open = ref.find('>', find_td + 1)
	find_td_close = ref.find('</', find_td_open + 1)
	rank = ref[find_td_open + 1:find_td_close]
	### Male Names
	find_td1 = ref.find('<td>', find_td_close + 1)
	find_m_td_open = ref.find('>', find_td1 + 1)
	find_m_td_close = ref.find('</td>', find_m_td_open + 1)
	male = ref[find_m_td_open + 1: find_m_td_close]
	### Female Names
	find_td2 = ref.find('<td>', find_m_td_close + 1)
	find_f_td_open = ref.find('>', find_td2 + 1)
	find_f_td_close = ref.find('</td>', find_f_td_open + 1)
	female = ref[find_f_td_open + 1: find_f_td_close]
	return (find_f_td_close, male, female, rank)

def final(ref):
    r = []
    m = []
    f = []
    while True:
        end_pos, m1, f1, r1 = data(ref)
        if end_pos:
            r.append(r1)
            m.append(m1)
            f.append(f1)
            ref = ref[end_pos:]
            if r1 == '1000':
                break
    #male = pd.Series(m)
    #female = pd.Series(f)
    #rank = pd.Series(r)
    return (pd.DataFrame({'Male':m, 'Female':f}, index=r))   # Creating dataframe and returning it

x = final(ref)                  # Assigning DataFrame to X
#print (final(ref))
writer = pd.ExcelWriter('D:/Gaurav - Docs/Projects/Python/Fetch Table Data/PythonExport.xlsx')   # Writing it to new Excel file
z = x.to_excel(writer,'Sheet1')

# CODED BY - GAURAV PADAWE
