import time, random

from Dialog.mid_dialog import MidDialog
from Dialog.post_dialog import PostDialog
from Dialog.pre_dialog import PreDialog
from Documents.passport import Passport
from Documents.pda import PDA
from Documents.permit import Permit
from OtherClasses.make_applicant import ApplicantInfo
from OtherClasses.day import Day
from OtherClasses.decision import Decision
from OtherClasses.notice import Notice
from Utils.Functions.wait import wait
import pygame


def main():

    # Establish non-personal variables
    day = 7
    nexa = 0
    old_nexa = 0
    food = 3
    heat = 3
    loop = 1
    citations = 0
    is_running = True
    event_occurred = False
    verdict = None
    accepted_grant = None

    sound_file = "Golden.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    admin = input("Admin? Enter nothing for no, and what day you want to start at for yes: ")
    if admin:
        day = int(admin)

    # Print Daily Notice
    if not admin:
        Notice(day, accepted_grant).print()


    start_time = time.time()

    while is_running:


        # Establish Applicant Information
        get_info = ApplicantInfo(day, loop, event_occurred)
        f_name = get_info.f_name
        l_name = get_info.l_name
        planet = get_info.planet

        sex = get_info.sex
        dob = get_info.dob
        exp = get_info.exp
        pass_num = get_info.pass_num

        purpose = get_info.purpose
        duration = get_info.duration

        event_occurred = get_info.event_occurred

        has_dis = get_info.has_dis


        # Dialog before documents
        event_occurred = PreDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).event()

        if event_occurred == "dead":
            event_occurred = False

            # Daily Notice
            Notice(day, accepted_grant).print()
            start_time = time.time()
            nexa = old_nexa

            wait(0, 30)
            loop = 1
            continue

        # When event_occurred is "continue", it counts as the event and skips that applicant's document sequence.
        elif event_occurred == "continue":
            event_occurred = True
            print("event_occurred was set to True from continue")
            wait(0, 30)
            loop += 1
            continue

        # When event_occurred is "skip", it doesn't count as the event and skips that applicant's document sequence.
        elif event_occurred == "skip":
            event_occurred = False
            print("event_occurred was set to False from skip")
            wait(0, 30)
            loop += 1
            continue

        # Print passport
        has_dis = Passport(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Chance of applicant missing entry permit
        if day >= 3 and not planet == "Nexus Harbor":
            if random.randint(1, 10) == 1:
                has_dis = True
            else:
                has_dis = Permit(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Chance of applicant missing PDA
        if day >= 4 and planet == "Nexus Harbor":
            if random.randint(1, 10) == 1:
                has_dis = True
            else:
                has_dis = PDA(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Dialog after documents are presented, but before user enters a verdict

        has_dis, event_occurred = MidDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).interrogate()
        has_dis, event_occurred = MidDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).event()

        # Decision
        nexa, verdict, citations, accepted_grant = Decision(has_dis, nexa, day, loop, planet, event_occurred, citations, accepted_grant).decide()
        print(f"This is main.py right after the Decision function!")
        print(f"accepted_grant is {accepted_grant}")
        # Dialog after the player enters their verdict
        event_occurred, nexa = PostDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).remark()

        wait(1, 30)


        # Daily Evaluation
        loop += 1
        if time.time() - start_time > 1 and event_occurred == True:

            nexa, food, heat, is_running, event_occurred = Day(nexa, is_running, food, heat, event_occurred).evaluate_day()

            # Reset Day
            event_occurred = False
            day += 1
            old_nexa = nexa
            loop = 1

            # Daily Notice
            Notice(day, accepted_grant).print()

            start_time = time.time()

if __name__ == "__main__":

    main()