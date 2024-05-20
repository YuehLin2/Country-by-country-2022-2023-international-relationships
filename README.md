# README: Country-by-country-2022-2023-international-relationships

The country-by-country international relationship data provided in this repository is a network data set, where each country represents a node. The edges are constructed by combining five sources of information:

(1) UN-General-Assembly 2022-2023 voting;
(2) Bilateral trade agreements ongoing by December 2023;
(3) Ongoing military alliences by December 2022;
(4) Ongoing moteraty unions by December 2022;
(5) Balanced international trade (averaged over 2017-2023);

The file trigraphs.txt contains the whole list of countries labeled by three letters. These are needed to provide a unique identifier for each node in the network.

# (1) UN-General-Assembly 2022-2023 voting (UN_resolutions folder)

For the first source of information we provide the Python code (in the src folder) used to collect the voting results from the digital library of united nation votes. This is based on two Python libraries: "request" and "BeautifulSoup". The selected topics are dated from 1 January 2022 to 1 June 2023 : 

https://digitallibrary.un.org/search?ln=en&cc=Voting%20Data&p=&f=&rm=&sf=year&so=d&rg=50&c=Voting%20Data&c=&of=hb&fti=0&fct__2=General%20Assembly&fti=0

There contains three types of resolutions: (i) resolutions where all of the 193 member countries are required to vote, (ii) resolutions where only some countries are required to vote, (iii) resolutions adopted without voting. Only case (i) is taken into account for the construction of our network data set. 
Hence, out of four hundreds resolutions, only 91 topics are kept. For each topic, there can be four possible decisions : either "yes", or "no", or "abstention", or "non-voting".

# (2) Bilateral trade agreements ongoing by December 2023 (alliance_data/trade_alliances.json)

There contains the collection of bilateral trade agreements ongoing by December 2023, based on the list reported in the Wikipedia web page: 

https://en.wikipedia.org/wiki/List_of_bilateral_free_trade_agreements.

# (3) Ongoing military alliances by December 2023 (alliance_data/military_alliances.json)

There contains the collection of military alliances (such as NATO, UK-Oman mutual defense agreement, etc.) ongoing by by December 2023, based on the list reported in the Wikipedia web page: 

[https://en.wikipedia.org/wiki/List_of_military_alliances](https://en.wikipedia.org/wiki/List_of_military_alliances#2000%E2%80%93Present)


# (4) Ongoing monetary alliances/unions by December 2023 (alliance_data/monetary_alliances.json)

There contains monetary alliances and strong monetary-based co-operations (such as the European Monetary Union, the OPEC, etc.) ongoing by December 2023. This list has been constructed by selecting all those organizations that have a supernational legislative system capable of enforcing monetary-based coordinations among the member states.


# (5) Balanced international trade (WTO_trade_data/balanced_export.csv)

This contains data from [stats.wto.org](https://stats.wto.org/). We selected the "Balanced international trade in services EBOPS" and the subsection "Services exports: balanced values (Million US dollar)". 


# Source file description (src/)

The folder src contains all the python codes needed to download and process the data sets mentioned in the previous sections.

- UN_resolution_downloader.ipynb
- network_construction.ipynb
- aka.py (This is to construct the python dictionary with information on the trigraph of countries and the list of alternative names.)


# Network sources (network_sources_data/)

This folder contains the four building blocks of our friendship and enemyship networks:

- covotes.csv (non-negative square matrix containing number of UN co-votes);- 
- alliances_network.csv (binary square matrix with 1 if two countries share an alliance);
- contravotes.csv (non-negative square matrix containing number of UN contra-votes);
- balanced_export.csv (non-negative square matrix containing the bilateral imports);

# Final network (final_network/)

This folder contains the final networks obtained by combining the UN voting data, the alliances data and the trade flow data described in the previous sections. These final tetworks are obtained by thefined the following binary matrices

- X1(P) = co-votes > q1(P),
- X2(P) = contra-votes > q2(P),
- X3(P) = alliances == 1,
- X4(P) = balanced_export_percentage > q4(P)
- X5(P) = balanced-import-percentage > q5(P)

  and

- Y1(P) = co-votes < q1(1-P),
- Y2(P) = contra-votes < q2(1-P),
- Y3(P) = alliances == 0,
- Y4(P) = balanced_export-percentage < q4(1-P),
- Y5(P) = balanced-import-percentage < q5(1-P),
  
where q1(P), q2(P), q4(P) and q5(P) are the P-quantile of co-votes, contra-votes and trade-flow, balanced-export-percentage, and balanced-import-percentage, respectively. 
By means of explanation, in matrix X3(P), two countries are regarded as connected if they share at least one of the bilateral trade agreements, or monetary alliances, or monetary co-operations reported in the previous sections. 
Contextually, in matrix X1(P), two countries are regarded as connected if their covote count is above P*100 percentile of UN resolution covotes among all country-pairs. In matrix X2(P) the (i, j) cell is equal to one if the number of contra-votes count between country i and country j is below P*100 percentile of UN resolution contra-votes among all country-pairs.  As a reminder, the covote (contravote resp.) number of a pair of countries is the number of times those two countries vote consistently (contrarily resp.) in the same resolution. 

Friendship and enemiship networks are obtained by Boolean trinomial combinations (majority rule, 3 our of 5 indicators):

Friendships:

X1(P) + X2(P) + X3(P) + X4(P) + X5(P) >= 3

Enemiships:

Y1(P) + Y2(P) + Y3(P) + Y4(P) + Y5(P) >= 3

Hence, 2 friendship networks and 2 enemyship networks are stored in the following files, based on two quantile values (P = 0.75 and P = 0.9): 

- friends_network_P80_Tri.json
- enemies_network_P80_Tri.json
- friends_network_P90_Tri.json
- enemies_network_P90_Tri.json

These networks are stored in form of adjacency matrices. 
