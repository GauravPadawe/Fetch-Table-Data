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
	m = []
	f = []
	while True:
		end_pos, m1, f1, r1 = data(ref)
		if end_pos:
			m.append(r1 + " " + m1)
			f.append(r1 + " " + f1)
			ref = ref[end_pos:]
			#print (m)
			#print (f)
			if r1 == '1000':
				break
	print (m)
	print (f)
    
print (final(ref))