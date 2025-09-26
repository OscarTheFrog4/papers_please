import random

from Biometrics import Biometrics
from Utils.Data.biometrics import dna
from Utils.Functions.wait import wait
from Utils.Functions.stutter import stutter
import Utils.Data.collections

creds = Utils.Data.collections

class DNA(Biometrics):
    def scan(self):
        for line in dna[0]:
            print(line)
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

