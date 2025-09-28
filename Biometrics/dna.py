import random

from Biometrics import Biometrics
from Utils.Data.biometrics import h_dna, a_dna
from Utils.Functions.wait import wait
import Utils.Data.collections

creds = Utils.Data.collections

class DNA(Biometrics):
    def scan(self):
        self.id = random.randint(0, 1)

        if random.randint(1, 7) == 1:
            # Discrepancy
            wait(2, 0)
            print("Incoming Biometric Scan:")
            self.fake_info = random.randint(0,1)
            while self.fake_info == self.id:
                self.fake_info = random.randint(0,1)
            for line in a_dna[self.fake_info]:
                print(line)
            self.has_dis = "forgery"
            wait(2, 2)
            print(f"DNA on Record for {self.l_name}, {self.f_name}:")
            for line in random.choice(h_dna):
                print(line)
        else:
            # Clean
            wait(1, 0)
            print("Incoming Biometric Scan:")
            wait(2)
            for line in h_dna[self.id]:
                print(line)
            wait(1, 2)
            print(f"DNA on Record for {self.l_name}, {self.f_name}:")
            for line in h_dna[self.id]:
                print(line)

        return self.has_dis

