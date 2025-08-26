from Utils.Functions.wait import wait


class Decision:
    def __init__(self, has_dis, nexa, day, loop, planet, event_occurred, citations, accepted_grant):
        self.has_dis = has_dis
        self.nexa = nexa
        self.day = day
        self.loop = loop
        self.planet = planet
        self.event_occurred = event_occurred
        self.verdict = ""
        self.citations = citations
        self.accepted_grant = accepted_grant

    def decide(self):
        # Ask player to accept or deny applicant
        wait(1, 1)

        if self.day <= 7:
            self.verdict = input("Accept or deny applicant?: ").lower()
            while not self.verdict == "accept" and not self.verdict == "deny":
                self.verdict = input("Answer only with 'accept' or 'deny': ").lower()

        elif self.day >= 8:
            self.verdict = input("Accept, deny, or lace applicant?: ").lower()
            while not self.verdict == "accept" and not self.verdict == "deny" and not self.verdict == "lace":
                self.verdict = input("Answer only with 'accept', 'deny', or 'lace': ").lower()

        # Evaluate player verdict
        wait(1, 1)

        if (self.verdict == "accept" and not self.has_dis) or (self.verdict == "deny" and self.has_dis):
            self.nexa += 2
        elif self.verdict == "lace" and self.has_dis == "forgery":
            self.nexa += 3
        else:
            self.citations += 1
            print("┌────────────────────┐")
            print("│ ** | Citation | ** │")

            if self.citations == 1:
                print("│    First Warning   │")
                print("│      No Charge     │")

            elif self.citations == 2:
                print("│   Second Warning   │")
                print("│      No Charge     │")

            elif self.citations == 3:
                print("│       1 Charge     │")
                print("│       2 Nexas      │")
                self.nexa -= 2

            else:
                print(f"│       {self.citations} Charges     │")
                print(f"│      {self.citations * 2} Nexas     │")
                self.nexa -= self.citations * 2
            print("└────────────────────┘")
            input("(Enter anything to continue): ")

        if self.planet == "Melanor" and self.verdict == "accept":
            self.accepted_grant = True
            print("This is the decision module where accepted_grant was just set to True!")
        elif self.planet == "Melanor" and self.verdict == "deny":
            self.accepted_grant = False
            print("This is the decision module where accepted_grant was just set to False!")

        return self.nexa, self.verdict, self.citations, self.accepted_grant