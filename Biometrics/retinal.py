import random
import string

from Documents import Documents
from Utils.Functions.wait import wait
import Utils.Data.collections
import Utils.Data.faces

creds = Utils.Data.collections
faces = Utils.Data.faces


class Passport(Documents):

    def print(self):

        wait(1.5, 0)

        print(f"(Current date: September {self.day + 5}, 2989)")

        # Header
        print("┌──────────────────────────────────┐ ")
        print("│            STELLAPASS            │ ")
        print("│                                  │ ")

        # Chance for Wrong First Name
        if random.randint(1, 10) == 1 and not self.f_name == "Robert":
            fake_info = self.f_name
            while fake_info == self.f_name:
                if self.f_name in creds.b_names:
                    fake_info = random.choice(creds.b_names)
                else:
                    fake_info = random.choice(creds.g_names)
            print(f"│ {self.l_name + ', ' + fake_info:32} │")
            self.has_dis = "forgery"

        # Chance for Wrong Last Name
        elif random.randint(1, 10) == 1 and not self.l_name == "Grant":
            fake_info = self.l_name
            while fake_info == self.l_name:
                fake_info = random.choice(creds.l_names)
            print(f"│ {fake_info + ', ' + self.f_name:32} │")
            self.has_dis = "forgery"

        # Correct Full Name
        else:
            print(f"│ {self.l_name + ', ' + self.f_name:32} │")

        print(f"│   _ _ _ _ _ _ _ _ _ _ _          │")

        # Portrait
        if random.randint(1, 10) == 1:
            portraits = faces.m_portraits if self.sex == "F" else faces.f_portraits
        else:
            portraits = faces.m_portraits if self.sex == "M" else faces.f_portraits
        for line in random.choice(portraits):
            print(f"│  | {line}{'|':9} │")

        # Other Passport Information
        print(f"│   ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾          │")
        print(f"│ [DOB] {self.dob:27}│")

        print(f"│ [EXP] {self.exp:27}│")
        if 2989 > int(self.exp[-4:]):
            self.has_dis = True

        print(f"│ [SEX] {self.sex:27}│")


        # Chance for wrong planet
        if random.randint(1, 10) == 1 and self.day >= 3:
            fake_info = self.planet
            while fake_info == self.planet:
                fake_info = random.choice(creds.planets)
            print(f"│ {fake_info:20} ", end="")
            self.has_dis = "forgery"

        # Correct planet
        else:
            print(f"│ {self.planet:20} ", end="")

        # Chance for wrong passport number
        if random.randint(1, 10) == 1 and self.planet == "Nexus Harbor" and self.day >= 4:
            self.fake_info = self.pass_num
            while self.fake_info == self.pass_num:
                self.fake_info = ""
                for char in range(11):
                    self.fake_info += random.choice(list(string.ascii_uppercase + string.digits))
                self.fake_info = self.fake_info[0:5] + "-" + self.fake_info[6:11]
            print(f"{self.fake_info:11} │")
            self.has_dis = "forgery"

        # Correct passport number
        else:
            print(f"{self.pass_num:11} │")

        print("└──────────────────────────────────┘ ")

        return self.has_dis