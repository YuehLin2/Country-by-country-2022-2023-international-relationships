#!/usr/bin/env python
# coding: utf-8

# In[1]:


# UN data extraction


import os
root = os.getcwd()
root = os.path.dirname(root)
root = os.path.dirname(root)

theme2vote = {}
files = os.listdir(os.path.join(root, "raw_data", "UN"))


for file in files:
    if file.endswith(".txt"):
        with open(os.path.join(root, "raw_data", "UN", file), 'r') as f:
            lines = f.readlines()
            theme2vote[file] = lines


# In[2]:


vote_example = list(theme2vote.values())[0]
print(vote_example[:10])


# In[3]:


# From the vote example, retrieve the set of countries
UN_countries = []
for s in vote_example:
    if s[0:2] in ['Y ', 'A ', 'N ']: # for now, yes/no/abstention is information that is not needed
        c = s[2:-1]  if  s[-1] == '\n' else s[2:]
    else:
        c = s[:-1] if s[-1] == '\n' else s[:]
    UN_countries.append(c.lower())


# In[4]:


# To improve the work, a consistent name using three letters are used. 
tri2name = {} # trigraph to name
name2tri = {} # name to trigraph
with open(os.path.join(root, "src", "utils", "trigraphs.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == '-':
            continue
        trigraph = line[0:3]
        fullname = line[4:-1]
        fullname = fullname.lower()
        name2tri[fullname] = trigraph
        tri2name[trigraph] = fullname


# In[5]:


# In other data, the country name can vary in format. To resolve this, we store all the aka's (alternative names) in a dictionary. 
tri2aka = {}
for (tri, name) in tri2name.items():
    tri2aka[tri] = [name]

def belongs_aka(name):
    """Check if a name had been recorded in the tri2aka dictionary. 
    If it exists, return its (unique) trigraph, return False otherwise"""
    name = name.lower()
    for (tri, names) in tri2aka.items():
        if name in names:
            return tri
    return False

def add_aka(name, aka):
    "Add the new aka to the country with the name that has already been recorded."
    for (tri, names) in tri2aka.items():
        name = name.lower()
        if name in names:
            aka = aka.lower()
            if aka in names:
                return None
            names.append(aka)
            return None
    raise Exception(f"{name} not found")

def add_aka3(tri, aka):
    "Add the new aka to the country with a given trigraph"
    aka = aka.lower()
    if aka in tri2aka[tri]:
        return None
    tri2aka[tri].append(aka)


# In[6]:


# This block is to add common alternative names. 
# A big part of them are country names with a title. Some documents put the title first while others put title after a comma.
# For instance : title first : Republic of Armenia / title last : Armenia, Republic of

add_aka3("RUS", "russian federation")
add_aka3("RUS", "Russia")
add_aka('russian federation', 'Russia')
add_aka('czechia', 'czech republic')
add_aka('turkiye', 'turkey')
add_aka('turkiye', 'Türkiye')
add_aka('republic of korea', 'south korea')

add_aka("cote d'ivoire", "côte d'ivoire")
add_aka3('AIA', 'Anguilla, United Kingdom-British Overseas Territory')
add_aka3('ARM', 'Armenia, Republic of')
add_aka3('ABW', 'Aruba, Kingdom of the Netherlands')
add_aka3('AZE', 'Azerbaijan, Republic of')
add_aka3('BHS', 'Bahamas, The')
add_aka3('BHR', 'Bahrain, Kingdom of')
add_aka3('BLR', 'Belarus, Republic of')
add_aka3('COM', 'Comoros, Union of the')
add_aka3('COG', 'Congo, Democratic Republic of the')
add_aka3('COG', 'Congo, Republic of')
add_aka3('HRV', 'Croatia, Republic of')
add_aka3("LAO", "Lao People’s Democratic Republic".lower())
add_aka3("GBR", "United Kingdom of Great Britain and Northern Ireland".lower())
add_aka3("USA", "United States of America".lower())
add_aka3('AFG', "Afghanistan, Islamic Republic of")
add_aka("andorra", "Andorra, Principality of")
add_aka3("BOL", 'bolivia')
add_aka('curacao', "Curaçao, Kingdom of the Netherlands")

add_aka3("MDG", "Madagascar, Republic of")
add_aka3("MHL", "Marshall Islands, Republic of the")
add_aka3("MRT", "Mauritania, Islamic Republic of")

add_aka3('CHN', "China, People's Republic of")
add_aka3('HKG', "Hong Kong Special Administrative Region, People's Republic of China")
add_aka3('IRN', "iran")
add_aka3('IRN', "Iran, Islamic Republic of")
add_aka3('KOR', 'Korea, Republic of')
add_aka3('KGZ', 'Kyrgyz Republic')
add_aka3('MAC', "Macao Special Administrative Region, People's Republic of China")
add_aka3('FSM', 'micronesia')
add_aka3('FSM', 'Micronesia, Federated States of')
add_aka3('MDA', 'moldova')
add_aka3('MDA', 'Moldova, Republic of')

add_aka3("MSR", "Montserrat, United Kingdom-British Overseas Territory")
add_aka3("MOZ", "Mozambique, Republic of")
add_aka3("NRU", "Nauru, Republic of")

add_aka('sao tome and principe', "São Tomé and Príncipe, Democratic Republic of")
add_aka('slovakia', 'slovak republic')

add_aka3('BLM', 'St. barthelemy')
add_aka3( 'SHN', 'St. helena, ascension, and tristan da cunha')
add_aka3( 'KNA', 'St. kitts and nevis')
add_aka3( 'LCA', 'St. lucia')
add_aka3( 'MAF', 'St. martin')
add_aka3( 'SPM', 'St. pierre and miquelon')
add_aka3( 'VCT', 'St. vincent and the grenadines')

add_aka3('TZA', 'tanzania')
add_aka3('TZA', 'Tanzania, United Republic of')
add_aka3('VEN', 'venezuela')
add_aka3('VEN', 'Venezuela, República Bolivariana de')
add_aka('viet nam', 'vietnam')
add_aka('cabo verde', 'cape verde')
add_aka('timor-leste', 'east timor')
add_aka3('KOR', 'Korea, South')
add_aka3("ALN", "Åland Islands")
add_aka('cape verde', 'Cabo Verde [Cape Verde]')
add_aka('bolivia', 'Plurinational State of Bolivia')
add_aka('iran', "Islamic Republic of Iran")
add_aka('micronesia', 'Federated States of Micronesia')
add_aka3("STP", "São Tomé and Príncipe")
add_aka3("VEN", "Bolivarian Republic of Venezuela")
add_aka3("PRK", "north korea")
add_aka3("COG", "Congo [Republic of the Congo]")
add_aka("cote d'ivoire", "Côte d'Ivoire [Ivory Coast]")
add_aka("curacao", "Curaçao")
add_aka("czechia", "Czechia [Czech Republic]")
add_aka3("PRK", "Democratic People's Republic of Korea [North Korea]")
add_aka("eswatini", "Eswatini [Swaziland]")
add_aka3("FLK", "Falkland Islands (Malvinas)")
add_aka("France", "France [French Republic]")
add_aka3("ATF", "French Southern Territories")
add_aka("cote d'ivoire", "Ivory Coast")
add_aka3("COG", "Republic of the Congo")
add_aka3("SYR", "Syria")
add_aka3("BRN", "brunei")
add_aka3("LAO", 'laos')
add_aka("bahamas", "the bahamas")
add_aka3("COD", 'D.R. Congo')
add_aka("china", "P.R. China")
add_aka3("VCT", 'saint vincent')
add_aka("eswatini", 'swaziland')
add_aka("macau", "macao")
add_aka("macau", "Macao, China")
add_aka("taiwan", "chinese taipei")

add_aka3("EGY", "Egypt, Arab Republic of")
add_aka3("GNQ", "Equatorial Guinea, Republic of")
add_aka3("ERI", "Eritrea, The State of")
add_aka3("EST", "Estonia, Republic of")
add_aka3("SWZ", "Eswatini, Kingdom of")
add_aka3("ETH", "Ethiopia, The Federal Democratic Republic of")
add_aka3("FJI", "Fiji, Republic of")
add_aka3("GMB", "Gambia, The")
add_aka3("KAZ", "Kazakhstan, Republic of")
add_aka3("XKS", "Kosovo, Republic of")
add_aka3("LVA", "Latvia, Republic of")
add_aka3("LSO", "Lesotho, Kingdom of")
add_aka3("LTU", "Lithuania, Republic of")
add_aka3("NLD", "Netherlands, The")
add_aka3("MKD", "North Macedonia, Republic of")
add_aka3("PLW", "Palau, Republic of")
add_aka3("POL", "Poland, Republic of")
add_aka3("SMR", "San Marino, Republic of")
add_aka3("SRB", "Serbia, Republic of")
add_aka3("SXM", "Sint Maarten, Kingdom of the Netherlands")
add_aka3("SVN", "Slovenia, Republic of")
add_aka3("SSD", "South Sudan, Republic of")
add_aka3("TJK", "Tajikistan, Republic of")
add_aka3("TLS", "Timor-Leste, Democratic Republic of")
add_aka3("TUR", "Türkiye, Republic of")
add_aka3("UZB", "Uzbekistan, Republic of")
add_aka3("YEM", "Yemen, Republic of")
add_aka3("COG", "Congo, Republic of the")
add_aka3("HKG", "Hong Kong, China")


# In[7]:


# stock all the trigraphs from UN countries
UN_tri = []
for name in UN_countries:
    name = name.lower()
    if name not in name2tri.keys():
        print(name)
        continue
    UN_tri.append(name2tri[name])


# In[8]:


import pandas as pd


# In[9]:


# create a dataframe where rows are themes ; columns are countries
df = pd.DataFrame(index=list(theme2vote.keys()), columns=UN_tri)
n_topics, n_countries = df.shape

len(UN_countries)


# In[10]:


# fill the dataframe with vote result (Yes/No/Abstain/Missing)
YAN_code = dict(Y=1, A=-1, N=0)
for policy_index, votes in enumerate(theme2vote.values()):
    for country_index, s in enumerate(votes):
        if s[0:2] in ['Y ', 'A ', 'N ']:
            vote = YAN_code[s[0]]
            if s[-1] == '\n':
                c = s[2:-1].lower()
            else:
                c = s[2:].lower()
            c = belongs_aka(c)
 
            df.iloc[policy_index, country_index] = vote
        else: # will stay N/A
            pass


# In[11]:


df


# In[12]:


# Next, proceed to organizations. 
import os
# os.chdir("..")
# os.chdir("org")


# In[13]:


# list of organizations are stored in txt form
# os.listdir()


# In[14]:


# create a dictionary orgs. Keys are name of organisation. Values are lists of member countries. 
orgs = {}
for filename in os.listdir(os.path.join(root, "raw_data", "org")):
    name, file_extension = os.path.splitext(filename)
    if '.txt' in file_extension:
        with open(os.path.join(root, "raw_data", "org", filename), 'r', encoding='utf-8') as f:
            orgs[name] = f.read()


# In[15]:


# However, due to diverse source for member countries, their naming is not consistent. In order to address them efficiently, 
# it is useful to work with aka2name. 

def try_add_comma(namewithcomma):
    """A function that helps writing the function add_aka3 when a country doesn't exist in tri2aka, 
    by dealing with the case with commaand the title in last, or by changing some countries starting with Saint. 
    and replace St. with Saint.  """
    
    if namewithcomma[:3] == 'St.':
        newname = 'saint '+namewithcomma[3:]
        if (the_tri:=belongs_aka(newname)):
            add_aka3(tri, namewithcomma)
            print(f'add_aka3("{the_tri}", "{namewithcomma}")')
            return None
        else:
            raise Exception(f"{namewithcomma} not found")

    if (pos:=namewithcomma.find(',')) == -1:
        raise Exception(f"{namewithcomma} no comma")
    name = namewithcomma[:pos].lower()
    if (the_tri:=belongs_aka(name)):
        add_aka3(the_tri, namewithcomma)
        print(f'add_aka3("{the_tri}", "{namewithcomma}")')
    else:
        raise Exception(f"{namewithcomma} and {name} not found")


# In[16]:


# Apply previous function to list of members in org. 

for (org, members) in orgs.items():
    l_mem = members.split('\n')
    for mem in l_mem:
        if mem.strip() == '':
            continue
        mem = mem.strip()
        if not belongs_aka(mem):
            try_add_comma(mem)


# In[17]:


# Keep track the total set of countries present in the data for the organizations

countries_org = set()
for (org, members) in orgs.items():
    l_mem = members.split('\n')
    for mem in l_mem:
        mem = mem.strip()
        if mem == '':
            continue
        if belongs_aka(mem):
            countries_org.add(belongs_aka(mem))
        else:
            print(mem)
            raise KeyboardInterrupt


# In[18]:


# examine whether there are countries present in org data but not UN data
countries_all = countries_org.union(UN_tri)
added = False


# In[19]:


# modify the dataframe by adding 0 as votes for countries outside UN
if not added:
    for c in countries_org.difference(UN_tri):
        df[c] = 0
        added = True


# In[20]:


# store organization data in dictionary form

orgs_d = {}

for (org, members) in orgs.items():
    d_mem = {}
    l_mem = members.split('\n')
    for mem in l_mem:
        mem = mem.strip()
        if mem == '':
            continue
        assert belongs_aka(mem)
        tri = belongs_aka(mem)
        d_mem[tri] = 1
    for tri in countries_org.difference(d_mem.keys()):
        d_mem[tri] = 0
    assert len(d_mem) == len(countries_org)
    orgs_d[org] = d_mem

class Nothing(Exception):
    pass

class Several(Exception):
    pass


show_guess_country = False
def guess_country(name, mother_tri=None, show_guess_country=show_guess_country):
    name = name.lower()
    found = []
    for (tri, akas) in tri2aka.items():
        for aka in akas:
            if name == aka:
                return tri
            if name in aka or aka in name:
                found.append(tri)
                break
    if len(found) == 0:
        print("country not found") if show_guess_country else None
        raise Nothing()
    elif len(found) == 1:
        tri = found[0]
        print("found exactly one, which is", tri, tri2aka[tri]) if show_guess_country else None
        return tri
    elif len(found) == 2 and mother_tri in found:
        found.remove(mother_tri)
        return found[0]
    else:
        print(found) if show_guess_country else None
        print("found several") if show_guess_country else None
        for tri in found:
            print("found one, which is", tri, tri2aka[tri]) if show_guess_country else None
        raise Several()


# # In[21]:


# # trigraphs.txt is in the same directory but is not one of the theme
# df.drop("trigraphs.txt")

# # keep track of where "Yes" is voted denoted by 1, everything else default to 0
# yes = df.where(df==1, 0) 

# # keep track of where "No" is voted denoted by 1, everything else default to 0
# no = (df+1).where(df==0, 0)


# # In[ ]:





# # In[22]:


# len(df.index)


# # In[23]:


# yes.to_csv("countries_yes.csv", index=False)
# no.to_csv("countries_no.csv", index=False)


# # In[24]:


# # start doing stats between countries


# # In[25]:


# # covotes = two countries voting the same. Namely Yes/Yes or No/No. 

# covotes = pd.DataFrame(0, columns= sorted(list(countries_org)), index=sorted(list(countries_org)))

# for dff in [yes, no]:
#     for t in range(n_topics):
#         print(t, end=' ')
#         votes = dff.iloc[t, :]
#         votes_filtered = votes[votes==1] # the list of countries that vote yes / no respectively
#         votes_filtered = votes_filtered.index 
#         for c in votes_filtered:
#             covotes[c][votes_filtered]+=1 # update covote of pairs of countries from the list votes_filtered


# # In[26]:


# # contravotes = two countries voting differently. 

# contravotes = pd.DataFrame(0, columns= sorted(list(countries_org)), index=sorted(list(countries_org)))

# for t in range(n_topics):
#     print(t, end=' ')
#     votes = yes.iloc[t, :]
#     votes_filtered = votes[votes==1]
#     votes_filtered = votes_filtered.index
#     negvotes = no.iloc[t, :]
#     negvotes_filtered = negvotes[negvotes==1]
#     negvotes_filtered = negvotes_filtered.index
#     for c in negvotes_filtered:
#         contravotes[c][votes_filtered] += 1


# # In[27]:


# import numpy as np
# arr = covotes.to_numpy()

# # Set diagonal elements to zero
# np.fill_diagonal(arr, 0)

# # Convert back to DataFrame
# covotes = pd.DataFrame(arr, columns=covotes.columns, index=covotes.index)


# # In[28]:


# # Inspect covotes' distribution

# import matplotlib.pyplot as plt
# plt.hist(covotes.to_numpy().flatten(), bins=15)


# # In[29]:


# # Inspect contravotes' distribution

# import matplotlib.pyplot as plt
# thelist = contravotes.to_numpy().flatten()
# thelist = [i for i in iter(thelist) if i!= 0]
# plt.hist(thelist, bins=15)


# # In[30]:


# import numpy as np


# # In[31]:


# 15, 26, 32
# np.percentile(covotes, 90)


# # In[ ]:





# # In[ ]:





# # In[ ]:





# # In[32]:


# # weighted adjacency matrix for country-country pair. 

# friendshipgraph = covotes.copy()
# enemyshipgraph = contravotes.copy()


# # In[33]:


# # A percentile-based requirement is applied. 

# min_covote = np.percentile(covotes, 25)
# max_contravote = np.percentile(contravotes, 75)

# pre_friends = []
# for c in countries_org:
#     for cc in countries_org:
#         if covotes[c][cc] >= min_covote and contravotes[c][cc] < max_contravote:
#             pre_friends.append([c, cc])
#             enemyshipgraph[c][cc] = 0
#             enemyshipgraph[cc][c] = 0
#         else:
#             friendshipgraph[c][cc] = 0
#             friendshipgraph[cc][c] = 0
            
# len(pre_friends)


# # In[34]:


# max_covote = np.percentile(covotes, 25)
# min_contravote = np.percentile(contravotes, 75)

# pre_enemies = []
# for c in countries_org:
#     for cc in countries_org:
#         if contravotes[c][cc] >= min_contravote and covotes[c][cc] < max_covote:
#             pre_enemies.append([c, cc])
#             friendshipgraph[c][cc] = 0
#             friendshipgraph[cc][c] = 0
#         else:
#             enemyshipgraph[c][cc] = 0
#             enemyshipgraph[cc][c] = 0
# len(pre_enemies)


# # In[ ]:





# # In[ ]:





# # In[35]:


# # dictionary of trade agreement. Key:country, value:list of countries with trade agreement.
# agree = {'ARM':['GEO'],'BLR':['ARM','SRB','TJK'],'KAZ':['ARM','AZE','RUS','UKR','UZB','KGZ','SRB'],'KGZ':['ARM','KAZ','MDA','RUS','UKR','UZB'],'MDA':['ARM','AZE','KGZ','TUR','GBR'],'RUS':['ARM','AZE','GEO','KAZ','KGZ','SRB','BRA','IND','CHN','ZAF'],'TKM':['ARM','AZE','GEO'],'TJK':['ARM','BLR','UKR','UZB'],'UZB':['ARM','AZE','GEO','KAZ','KGZ','TJK'],'VNM':['CHL','COL','CRI','GEO','EGY','HKG','ISR','IDN','JOR','LBN','MKD','MEX','MAR','PHL','SRB','SGP','KOR','TUN','TUR','UKR'],'CHN':['SLB','BRA','RUS','IND','ZAF'],'IRN':['IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'SRB':['TUR','GBR','VNM'],'SGP':['KOR','CHE','TUR','GBR','USA','VNM'],'BGR':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'HRV':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','MNE','MKD','FIN'],'CYP':['SGP','TUN','DNK','EGY','ALB','LTU','FRO','MNE','LVA','DEU','VNM','ISR','LBN','PER','COL','SMR','BEL','SWE','SVN','ITA','PRT','KOR','BGR','NLD','CHL','DZA','MAR','HRV','JOR','IRL','GBR','FRA','LUX','AND','CAN','GEO','MCO','JPN','CHE','BIH','TUR','POL','CYP','HUN','EST','ZAF','FIN','SVK','MEX','GRC','CRI','AUT','SRB','CZE'],'AUT':['SGP','TUN','DNK','EGY','ALB','LTU','FRO','MNE','LVA','DEU','VNM','ISR','LBN','PER','COL','SMR','BEL','SWE','SVN','ITA','PRT','KOR','BGR','NLD','CHL','DZA','MAR','HRV','JOR','IRL','GBR','FRA','LUX','AND','CAN','GEO','MCO','JPN','CHE','BIH','TUR','POL','CYP','HUN','EST','ZAF','FIN','SVK','MEX','GRC','CRI','AUT','SRB','CZE'],'BEL':['CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'CZE':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'DNK':['BEL','CAN','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'EST':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'FIN':['GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD'],'FRA':['CAN','DNK','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'DEU':['CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'GRC':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'HUN':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'IRL':['SGP','TUN','DNK','EGY','ALB','LTU','FRO','MNE','LVA','DEU','VNM','ISR','LBN','PER','COL','SMR','BEL','SWE','SVN','ITA','PRT','KOR','BGR','NLD','CHL','DZA','MAR','HRV','JOR','IRL','GBR','FRA','LUX','AND','CAN','GEO','MCO','JPN','CHE','BIH','TUR','POL','CYP','HUN','EST','ZAF','FIN','SVK','MEX','GRC','CRI','AUT','SRB','CZE'],'ITA':['CAN','DNK','FRA','ISL','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'LVA':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'LTU':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'LUX':['BEL','CAN','DNK','FRA','ISL','ITA','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'MLT':['SGP','TUN','DNK','EGY','ALB','LTU','FRO','MNE','LVA','DEU','VNM','ISR','LBN','PER','COL','SMR','BEL','SWE','SVN','ITA','PRT','KOR','BGR','NLD','CHL','DZA','MAR','HRV','JOR','IRL','GBR','FRA','LUX','AND','CAN','GEO','MCO','JPN','CHE','BIH','TUR','POL','CYP','HUN','EST','ZAF','FIN','SVK','MEX','GRC','CRI','AUT','SRB','CZE'],'NLD':['SGP','TUN','DNK','EGY','ALB','LTU','FRO','MNE','LVA','DEU','VNM','ISR','LBN','PER','COL','SMR','BEL','SWE','SVN','ITA','PRT','KOR','BGR','NLD','CHL','DZA','MAR','HRV','JOR','IRL','GBR','FRA','LUX','AND','CAN','GEO','MCO','JPN','CHE','BIH','TUR','POL','CYP','HUN','EST','ZAF','FIN','SVK','MEX','GRC','CRI','AUT','SRB','CZE'],'POL':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'PRT':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'SVK':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVN','ALB','HRV','MNE','MKD','FIN'],'SVN':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','ALB','HRV','MNE','MKD','FIN'],'ESP':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'SWE':['GBR'],'GEO':['CHE','TUR','GBR','VNM'],'UKR':['ARM','AZE','GEO','ISR','KAZ','KGZ','CHE','TJK','TUR','GBR','VNM'],'USA':['GBR','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'AUS':['USA'],'CHL':['VNM'],'HKG':['NZL','CHE','VNM'],'IND':['JPN','MYS','SGP','KOR','THA','BRA','RUS','CHN','ZAF'],'IDN':['CHE','VNM','IRN','IRQ','KWT','SAU','VEN','QAT','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'JPN':['GBR','USA'],'MYS':['NZL','TUR'],'NZL':['SGP','KOR','THA','USA'],'GIN':['AUS','BEN','BFA','CPV','CIV','GMB','GHA','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'PER':['SGP','KOR','CHE','THA','USA'],'KOR':['VNM','USA'],'THA':['AUS','IND','JPN','NZL','PER','CHL','USA'],'GBR':['CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'AZE':['GEO','TUR'],'BRN':['JPN','NZL','SGP'],'MAC':['CHN','HKG'],'PAK':['CHN','IDN','TUR','USA'],'CRI':['MEX','PAN','PER','SGP','KOR','CHE','USA','VNM','DOM'],'ISL':['GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'CHE':['GBR'],'COL':['USA'],'CAN':['GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'LIE':['COL','CRI','GBR'],'NOR':['GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'ISR':['USA'],'MEX':['PAN','PER','CHE','GBR','VNM'],'GTM':['COL','CRI','PAN','USA'],'SLV':['COL','CRI','PAN','USA'],'HND':['COL','CRI','PAN','USA'],'NIC':['CRI','MEX','PAN','USA'],'PAN':['PER','SGP','CHE','USA'],'FRO':['TUR','GBR'],'TUR':['GBR','USA','GRC','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'LHT':['GEO','HKG','IDN','PER','KOR'],'BTN':['IND'],'NPL':['IND'],'LKA':['IND','SGP'],'MUS':['IND','TUR'],'ARE':['IDN','LBY','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'MOZ':['IDN'],'PAL':['IDN','MAR'],'JOR':['USA','EGY','IRQ'],'MNG':['JPN'],'PHL':['JPN','KOR','CHE','VNM','USA'],'DZA':['JOR','TUN','IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','NGA','ECU','GAB','AGO','GNQ','COG'],'LBY':['JOR','TUN','IRN','IRQ','KWT','SAU','VEN','QAT','IDN','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'SYR':['JOR'],'KWT':['JOR','USA','IRN','IRQ','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'BHR':['USA'],'LBN':['IRQ','EU','CHE','GBR','VNM'],'IRQ':['LBN','IRN','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG','EGY','JOR'],'LAO':['THA'],'MHL':['TWN'],'TWN':['MHL','NZL'],'URY':['MEX'],'ARG':['MEX','USA'],'BRA':['MEX','USA','RUS','IND','CHN','ZAF'],'ECU':['MEX','CHE','IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','GAB','AGO','GNQ','COG'],'PRY':['MEX'],'FSM':['USA'],'MAR':['USA'],'EGY':['MAR','CHE','TUN','TUR','VNM','USA','IRQ','JOR'],'TUN':['TUR','GBR','VNM','USA'],'AFG':['PAK'],'OMN':['GBR'],'ALB':['TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','HRV','MNE','MKD','FIN'],'MKD':['GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MNE','FIN'],'SEN':['TUN','BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SLE','TGO'],'MRT':['TUN'],'XKS':['TUR','GBR'],'MNE':['TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','ROU','SVK','SVN','ALB','HRV','MKD','FIN'],'VEN':['TUR','IRN','IRQ','KWT','SAU','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'CMR':['GBR'],'GHA':['GBR','BEN','BFA','CPV','CIV','GMB','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'CIV':['GBR','BEN','BFA','CPV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'KEN':['GBR'],'ROU':['BEL','CAN','DNK','FRA','ISL','ITA','LUX','NOR','PRT','GBR','USA','GRC','TUR','DEU','ESP','CZE','HUN','POL','BGR','EST','LVA','LTU','SVK','SVN','ALB','HRV','MNE','MKD','FIN'],'QAT':['USA','IRN','IRQ','KWT','SAU','VEN','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'ZAF':['BRA','RUS','IND','CHN'],'SAU':['IRN','IRQ','KWT','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ','COG'],'NGA':['IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','ECU','GAB','AGO','GNQ','COG','BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','SEN','SLE','TGO'],'GAB':['IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','AGO','GNQ','COG'],'AGO':['IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','GNQ','COG'],'GNQ':['IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','COG'],'COG':['IRN','IRQ','KWT','SAU','VEN','QAT','IDN','LBY','ARE','DZA','NGA','ECU','GAB','AGO','GNQ'],'BEN':['BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'BFA':['BEN','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'CPV':['BEN','BFA','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'GMB':['BEN','BFA','CPV','CIV','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'GNB':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','LBR','MLI','NER','NGA','SEN','SLE','TGO'],'LBR':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','MLI','NER','NGA','SEN','SLE','TGO'],'MLI':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','NER','NGA','SEN','SLE','TGO'],'NER':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NGA','SEN','SLE','TGO'],'SLE':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','TGO'],'TGO':['BEN','BFA','CPV','CIV','GMB','GHA','GIN','GNB','LBR','MLI','NER','NGA','SEN','SLE']}


# # In[36]:


# allianceship =  pd.DataFrame(0, columns= sorted(list(countries_org)), index=sorted(list(countries_org)))


# # In[37]:


# # change dictionary format to dataframe, in adjacency matrix form.
# # Some countries are in trade-agreement data but not in UN countries. They are ignored.

# for (head, clist) in agree.items():
#     for c in clist:
#         try:
#             allianceship[head][c] = 1
#             allianceship[c][head] = 1
#         except KeyError:
#             print(head, c, "not found")


# # In[38]:


# # Inspect how many positive links are excluded this way?
# len(pre_friends)


# # In[39]:


# # filter pre friends
# total = len(pre_friends)
# kept = 0
# eliminated = 0
# for pair in pre_friends:
#     a, b = pair[0], pair[1]
#     if (allianceship[a][b] == 1) or (allianceship[b][a]==1) :
#         kept +=1 
#     else:
#         eliminated += 1
# print(eliminated, kept)


# # In[40]:


# # filter pre enemies
# total = len(pre_enemies)
# kept = 0
# eliminated = 0
# for pair in pre_enemies:
#     a, b = pair[0], pair[1]
#     if (allianceship[a][b] == 1) or (allianceship[b][a]==1) :
#         eliminated += 1
#     else:
#         kept += 1
# print(eliminated, saved)


# # In[ ]:


# friendshipgraph


# # In[ ]:


# # Inspect countries that don't end up having links to other countries. 

# (friendshipgraph.sum(axis=0)==0).to_numpy().nonzero()


# # In[ ]:


# # Remove those countries

# columns = friendshipgraph.columns
# to_drop = []
# for index in (friendshipgraph.sum(axis=0)==0).to_numpy().nonzero()[0]:
#     c = columns[index]
#     friendshipgraph.drop(c, axis=0, inplace=True)
#     friendshipgraph.drop(c, axis=1, inplace=True)


# # In[ ]:


# friendshipgraph


# # In[ ]:




