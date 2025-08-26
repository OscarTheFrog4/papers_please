import random
import string

import Utils.Data.collections
creds = Utils.Data.collections


class ApplicantInfo:
    def __init__(self, day, loop, event_occurred):

        self.day = day
        self.loop = loop
        self.event_occurred = event_occurred


        # Establishing Applicant Information
        self.planet = random.choice(creds.planets)
        self.l_name = random.choice(creds.l_names)
        self.sex = random.choice(["M", "F"])
        self.has_dis = False

        self.dob = f"{random.choice(creds.months)} {random.randint(1, 28)}, {random.randint(2910, 2970)}"
        self.exp = f"{random.choice(creds.months)} {random.randint(1, 28)}, {random.randint(2990, 3010)}"

        if self.sex == "M":
            self.f_name = random.choice(creds.b_names)
        else:
            self.f_name = random.choice(creds.g_names)

        self.pass_num = ""
        for char in range(11):
            self.pass_num += random.choice(list(string.ascii_uppercase + string.digits))
        self.pass_num = self.pass_num[0:5] + "-" + self.pass_num[6:11]

        self.purpose = random.choice(creds.purposes)

        self.duration = random.choice(creds.durations.get(self.purpose))

        match self.day:
            case 1:
                if random.random() < 0.5:
                    self.planet = random.choice(creds.planets)
                    if self.planet != "Nexus Harbor":
                        self.has_dis = True
                else:
                    self.planet = "Nexus Harbor"
                    print("Planet was just set to Nexus Harbor in make_applicant")

        match self.day:
            case 1:
                if loop > 1 and self.planet != "Nexus Harbor" and not self.event_occurred:
                    self.event_occurred = "go ahead"

            case 2:
                if self.loop > 2 and not self.event_occurred:
                    self.event_occurred = "go ahead"

            case 3:
                if self.loop > 1:
                    self.event_occurred = "go ahead"

            case 4:
                self.event_occurred = True

            case 5:
                if self.loop > 2 and not self.event_occurred:
                    self.f_name = "Robert"
                    self.l_name = "Grant"
                    self.sex = "F"
                    self.planet = "Melanor"
                    self.purpose = "Diplomacy"
                    self.duration = "Varies"

                    self.has_dis = "forgery"
                    self.event_occurred = "go ahead"

            case 6:
                if self.loop > 2 and not self.event_occurred:
                    self.event_occurred = "go ahead"

            case 7:
                if self.loop > 2 and not self.event_occurred:
                    self.event_occurred = "go ahead"

            case 8:
                self.event_occurred = True

            case 9:
                if self.loop > 2 and not self.event_occurred:
                    self.planet = "Android Citadel"
                    self.has_dis = True