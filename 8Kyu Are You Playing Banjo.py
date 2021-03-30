def are_you_playing_banjo(name):
    
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"
print(are_you_playing_banjo("Mama"))
print(are_you_playing_banjo("Ria"))
print(are_you_playing_banjo("GeRal"))