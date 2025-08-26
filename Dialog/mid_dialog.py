import random

from Dialog import Dialog
from Utils.Functions.wait import wait
from Utils.Functions.dialog import dialog
import Utils.Data.collections
creds = Utils.Data.collections


class MidDialog(Dialog):

    @staticmethod
    def print_purpose(category, dia_options, fake_info, purpose):
        if category == purpose and not fake_info or fake_info == category:
            print(f"<< '{random.choice(dia_options)}'")

    def interrogate(self):
        wait(1.5, 2)

        if self.f_name == "Robert":
            dialog("inspector", "Purpose of visit?")
            wait(1.5, 0)
            dialog("applicant", "I was called for diplomatic purposes.")
            wait(1.5, 0)
            dialog("inspector", "Duration of stay?")
            wait(1.5, 0)
            dialog("applicant", "However long the discussions last.")

        # Ask for Name
        elif self.day <= 2 or self.planet == "Nexus Harbor":

            dialog("inspector", "Name?")
            wait(1, 0)

            # Print first name
            print(f"<< '{self.f_name} ", end="")

            # Print last name
            print(f"{self.l_name}'")


        # Ask for purpose and duration of stay
        else:

            # Ask for purpose.
            dialog("inspector", "Purpose of visit?")
            wait(1.5, 0)

            # Chance of Responding With a Fake Purpose
            fake_info = None
            if random.randint(1, 10) == 1:
                fake_info = self.purpose
                while fake_info == self.purpose:
                    fake_info = random.choice(creds.purposes)
                self.has_dis = "forgery"
                dialog("applicant", f"{random.choice(creds.dialog_purposes.get(fake_info))}")

            # Real purpose
            else:
                dialog("applicant", f"{random.choice(creds.dialog_purposes.get(self.purpose))}")
            wait(1.5, 0)



            # Ask for Duration of Stay
            dialog("inspector", "Duration of stay?")
            wait(1.5, 0)


            # Chance of Responding With a Fake Duration
            if random.randint(1, 10) == 1:
                fake_info = self.duration
                while fake_info == self.duration:
                    fake_info = random.choice(creds.durations.get(random.choice(creds.purposes)))  # Choose a random duration.
                if random.choice((True, False)) and (self.duration != "Forever" and self.duration != "Varies"):
                    dialog("applicant", f"{random.choice(creds.duration_prefixes)} {fake_info}")  # Has a duration prefix
                else:
                    dialog("applicant", fake_info)  # Has no duration prefix
                self.has_dis = "forgery"

            # Real Duration
            else:
                if random.choice((True, False)) and (self.duration != "Forever" and self.duration != "Varies"):
                    dialog("applicant", f"{random.choice(creds.duration_prefixes)} {self.duration}")  # Has a duration prefix
                else:
                    dialog("applicant", self.duration)  # Has no duration prefix

        return self.has_dis, self.event_occurred

    def event(self):

        # print("This is MidDialog in the event function!")
        # print(f"event_occurred = {self.event_occurred}")
        # print(f"has_dis = {self.has_dis}")

        match self.day:
            case 2:
                # Person begging to be let through
                if self.event_occurred == "go ahead" and self.has_dis:
                    wait(2, 1)
                    print(f"{"'There is a discrepancy here' >>":>70}")
                    wait(2, 0)
                    print("<< 'Look, I know my papers are out of order'")
                    wait(2, 0)
                    print("<< 'I couldn't update them in time'")
                    wait(2, 0)
                    print("<< 'But my son is alone across the border'")
                    wait(2, 0)
                    print("<< 'Please. I am begging you. I am not an android'")
                    wait(2, 0)
                    self.event_occurred = True

        return self.has_dis, self.event_occurred