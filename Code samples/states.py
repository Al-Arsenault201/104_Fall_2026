states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii","Idaho", "Indiana", "Illinois", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
"Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]

#check to see how many we have
print(len(states))

states.append("Maryland")
#print(states)
states.sort()
#print(states)

# what if I only want the first 10 states?

new_states = states[0:10]
print(new_states)

end_states = states[40:]
print(end_states)

another_list = states[:10]
print(another_list)

yet_another_list = states[:]
print(yet_another_list)