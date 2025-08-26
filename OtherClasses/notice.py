from Utils.Functions.wait import wait
import Utils.Data.daily_notices
import Utils.Data.daily_tutorials


# from Utils.Data import daily_tutorial see if this == import Utils.Data.daily_tutorial

notices = Utils.Data.daily_notices.notices
tutorials = Utils.Data.daily_tutorials.tutorials


class Notice:
    def __init__(self, day, accepted_grant):
        self.day = day
        self.accepted_grant = accepted_grant

    def print(self):
        print("┌──────────────────────────────┐")
        print("│            NOTICE            │")
        print("│                              │")
        print("│ Planet Vespera               │")
        print("│ Nexus Harbor                 │")
        print(f"│ September {str(self.day + 5) + ", 2989":19}│")  # Account for varying day
        print("│                              │")
        print("│ Agent,                       │")

        # Print notice body and instructions based on day.
        if not self.accepted_grant and self.day == 6:
            print("│ I must admit I am very       │")
            print("│ dissapointed. Yesterday, you │")
            print("│ denied Robert Grant. He was  │")
            print("│ about to provide very        │")
            print("│ important information for    │")
            print("│ the Nexus Harbor planetary   │")
            print("│ government. Let this not     │")
            print("│ happen again, for there are  │")
            print("│ others waiting to take your  │")
            print("│ place.                       │")
            print("└──────────────────────────────┘")
        else:
            for line in notices.get(self.day):
                print(line)
            input("(Enter anything to continue): ")
            wait(1, 30)

        if tutorials.get(self.day):
            for line in tutorials.get(self.day):
                print(line)
            input("(Enter anything to continue): ")
            wait(1, 30)
        else:
            wait(1, 0)