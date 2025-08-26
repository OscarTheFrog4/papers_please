planets = ("Spectra Confederacy", "Cygnus", "Arkonia", "Velorum", "Chargona", "Nexus Harbor", "Nexus Harbor")
b_names = ("Lazarus", "Saitama")
g_names = ("Clarafina", "Aurora", "Ava")
l_names = ("Valtor", "Charius", "Dairox", "Lendrivax")
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


duration_prefixes = ("About ", "Around ", "Uh, like ")
purposes = ("Asylum", "Visiting Persons", "Immigration", "Tourism")
fake_durations = ("1 week", "2 weeks", "3 months", "6 months", "Forever")

durations = {
    "Asylum":("12 months", "Forever", "9 months"),
    "Visiting Persons":("1 week", "2 weeks", "3 weeks", "4 weeks"),
    "Immigration":("Forever",),
    "Tourism":("4 days", "1 week", "2 weeks", "3 weeks"),
    "Diplomacy":("Varies",)
}


dialog_purposes = {
    "Asylum":("Asylum", "Protection from the Khaosynths", "I am seeking asylum"),
    "Visiting Persons":("Visiting persons", "Visiting people", "Seeing relatives", "Visiting"),
    "Immigration":("Immigration", "I am immigrating", "I am moving here", "I plan on living here"),
    "Tourism":("Tourism", "I am a tourist", "Touring the Nexus Harbor by myself"),
    "Diplomacy":("Diplomacy", "Diplomatic discussions", "My diplomatic presence was called", "I am a diplomat")
}
