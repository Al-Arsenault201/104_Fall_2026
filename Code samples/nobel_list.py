# Nobel Prize winners for the last 10 years (2017-2026).
# One dictionary per year, in chronological order.
# Keys are categories; values are lists of the winners in that category.
#
# Note: the 2018 Literature prize was postponed and announced in 2019
# (alongside the 2019 prize), but the Nobel Foundation files it under 2018.

nobel_winners = [
    {   # 2017
        "Physics": ["Rainer Weiss", "Barry C. Barish", "Kip S. Thorne"],
        "Chemistry": ["Jacques Dubochet", "Joachim Frank", "Richard Henderson"],
        "Physiology or Medicine": ["Jeffrey C. Hall", "Michael Rosbash", "Michael W. Young"],
        "Literature": ["Kazuo Ishiguro"],
        "Peace": ["International Campaign to Abolish Nuclear Weapons (ICAN)"],
        "Economic Sciences": ["Richard H. Thaler"],
    },
    {   # 2018
        "Physics": ["Arthur Ashkin", "Gérard Mourou", "Donna Strickland"],
        "Chemistry": ["Frances H. Arnold", "George P. Smith", "Gregory P. Winter"],
        "Physiology or Medicine": ["James P. Allison", "Tasuku Honjo"],
        "Literature": ["Olga Tokarczuk"],
        "Peace": ["Denis Mukwege", "Nadia Murad"],
        "Economic Sciences": ["William D. Nordhaus", "Paul M. Romer"],
    },
    {   # 2019
        "Physics": ["James Peebles", "Michel Mayor", "Didier Queloz"],
        "Chemistry": ["John B. Goodenough", "M. Stanley Whittingham", "Akira Yoshino"],
        "Physiology or Medicine": ["William G. Kaelin Jr.", "Peter J. Ratcliffe", "Gregg L. Semenza"],
        "Literature": ["Peter Handke"],
        "Peace": ["Abiy Ahmed Ali"],
        "Economic Sciences": ["Abhijit Banerjee", "Esther Duflo", "Michael Kremer"],
    },
    {   # 2020
        "Physics": ["Roger Penrose", "Reinhard Genzel", "Andrea Ghez"],
        "Chemistry": ["Emmanuelle Charpentier", "Jennifer A. Doudna"],
        "Physiology or Medicine": ["Harvey J. Alter", "Michael Houghton", "Charles M. Rice"],
        "Literature": ["Louise Glück"],
        "Peace": ["World Food Programme (WFP)"],
        "Economic Sciences": ["Paul R. Milgrom", "Robert B. Wilson"],
    },
    {   # 2021
        "Physics": ["Syukuro Manabe", "Klaus Hasselmann", "Giorgio Parisi"],
        "Chemistry": ["Benjamin List", "David W.C. MacMillan"],
        "Physiology or Medicine": ["David Julius", "Ardem Patapoutian"],
        "Literature": ["Abdulrazak Gurnah"],
        "Peace": ["Maria Ressa", "Dmitry Muratov"],
        "Economic Sciences": ["David Card", "Joshua D. Angrist", "Guido W. Imbens"],
    },
    {   # 2022
        "Physics": ["Alain Aspect", "John F. Clauser", "Anton Zeilinger"],
        "Chemistry": ["Carolyn R. Bertozzi", "Morten Meldal", "K. Barry Sharpless"],
        "Physiology or Medicine": ["Svante Pääbo"],
        "Literature": ["Annie Ernaux"],
        "Peace": ["Ales Bialiatski", "Memorial", "Center for Civil Liberties"],
        "Economic Sciences": ["Ben S. Bernanke", "Douglas W. Diamond", "Philip H. Dybvig"],
    },
    {   # 2023
        "Physics": ["Pierre Agostini", "Ferenc Krausz", "Anne L'Huillier"],
        "Chemistry": ["Moungi G. Bawendi", "Louis E. Brus", "Alexei I. Ekimov"],
        "Physiology or Medicine": ["Katalin Karikó", "Drew Weissman"],
        "Literature": ["Jon Fosse"],
        "Peace": ["Narges Mohammadi"],
        "Economic Sciences": ["Claudia Goldin"],
    },
    {   # 2024
        "Physics": ["John J. Hopfield", "Geoffrey E. Hinton"],
        "Chemistry": ["David Baker", "Demis Hassabis", "John M. Jumper"],
        "Physiology or Medicine": ["Victor Ambros", "Gary Ruvkun"],
        "Literature": ["Han Kang"],
        "Peace": ["Nihon Hidankyo"],
        "Economic Sciences": ["Daron Acemoglu", "Simon Johnson", "James A. Robinson"],
    },
    {   # 2025
        "Physics": ["John Clarke", "Michel H. Devoret", "John M. Martinis"],
        "Chemistry": ["Susumu Kitagawa", "Richard Robson", "Omar M. Yaghi"],
        "Physiology or Medicine": ["Mary E. Brunkow", "Fred Ramsdell", "Shimon Sakaguchi"],
        "Literature": ["László Krasznahorkai"],
        "Peace": ["María Corina Machado"],
        "Economic Sciences": ["Joel Mokyr", "Philippe Aghion", "Peter Howitt"],
    },
    {   # 2026
        "Physics": ["Francis Halzen"],
        "Chemistry": ["Henri B. Kagan", "Kenso Soai"],
        "Physiology or Medicine": ["Karl Deisseroth", "Peter Hegemann", "Georg Nagel"],
        "Literature": ["Anne Carson"],
        "Peace": ["Navanethem (Navi) Pillay"],
        "Economic Sciences": ["Robert E. Hall", "Michael Woodford"],
    }
]

#print(nobel_winners)

for i in range(len(nobel_winners)):
    print(nobel_winners[i])

#print physics winner for each year:
for i in range(len(nobel_winners)):
    print(nobel_winners[i]["Physics"])

for j in range(len(nobel_winners)):
    print(nobel_winners[j]["Peace"])







