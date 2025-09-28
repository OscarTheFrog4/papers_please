import random

from Biometrics import Biometrics
from Utils.Functions.wait import wait
from Utils.Data.biometrics import h_fingerprints, a_fingerprints


class Fingerprint(Biometrics):
    def scan(self):
        self.id = random.randint(0, 1)
        if random.randint(1, 7) == 1:
            # Discrepancy
            wait(2, 0)
            print("Incoming Biometric Scan:")
            self.fake_info = random.randint(0, 1)
            while self.fake_info == self.id:
                self.fake_info = random.randint(0, 1)
            for line in a_fingerprints[self.fake_info]:
                print(line)
            self.has_dis = "forgery"
            wait(2, 2)
            print(f"Fingerprint on Record for {self.l_name}, {self.f_name}:")
            for line in random.choice(h_fingerprints):
                print(line)
        else:
            # Clean
            wait(1, 0)
            print("Incoming Biometric Scan:")
            wait(2)
            for line in h_fingerprints[self.id]:
                print(line)
            wait(1, 2)
            print(f"Fingerprint on Record for {self.l_name}, {self.f_name}:")
            for line in h_fingerprints[self.id]:
                print(line)

        return self.has_dis
