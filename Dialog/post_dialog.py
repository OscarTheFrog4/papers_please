from Utils.Functions.wait import wait
from Utils.Functions.dialog import dialog
from Dialog import Dialog


class PostDialog(Dialog):

    def remark(self):

        # print("This is PostDialog!")
        # print(f"self.event_occurred = {self.event_occurred}")
        # print(f"self.verdict = {self.verdict}")

        match self.day:
            case 1:
                # Foreign person angry about denial
                if self.event_occurred == "go ahead" and self.verdict == "deny":
                    wait(1, 1)
                    dialog("applicant", "Hey, what gives! Why deny?")
                    print("<< ''")
                    wait(2, 0)
                    dialog("inspector", "Entry is prohibited for Foreigners")
                    wait(3, 0)
                    self.event_occurred = True
                elif self.event_occurred == "go ahead" and self.verdict == "accept":
                    self.event_occurred = False

            case 3:
                # Android mocking agent
                if self.event_occurred == "go ahead" and self.verdict == "accept" and not self.has_dis:
                    wait(1, 1)
                    dialog("applicant", "Hehe")
                    wait(2, 1)
                    dialog("inspector", "???")
                    wait(2, 1)
                    dialog("applicant", "Foolish human, I can't believe that worked.")
                    wait(3, 1)
                    self.event_occurred = True
                elif self.event_occurred == "go ahead" and not self.verdict == "accept":
                    self.event_occurred = False

            case 5:
                if self.event_occurred == "go ahead":
                    if self.verdict == "accept":
                        wait(1, 1)
                        dialog("applicant", "Thanks, Agent. Have a few nexas.")
                        self.nexa += 3
                        wait(2, 1)
                    else:
                        wait(1, 1)
                        dialog("applicant", "...")
                        wait(2, 1)
                        dialog("applicant", "The Ministry will be hearing about this.")
                        wait(2, 1)
                        input("(Enter anything to continue): ")

                    self.event_occurred = True

        return self.event_occurred, self.nexa