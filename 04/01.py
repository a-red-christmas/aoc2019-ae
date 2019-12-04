#!/usr/bin/env python
import re


class PasswordChecker(object):
    """ Object to check passwords conforming to puzzle """

    def check_samedigit(self, pw: str) -> bool:
        """ We check for repeating digits """
        res = re.compile(r'.*(\d)\1.*')
        if res.match(pw) is not None:
            return True
        else:
            return False

    def check_increase(self, pw: str) -> bool:
        """ We check that digits do not decrease """
        parts = list(pw)

        decrease = False

        for i, x in enumerate(parts):
            if i > 0:
                if int(parts[i - 1]) > int(x):

                    decrease = True
                    break

        if decrease == True:
            return False

        else:
            return True

    def process(self, pwrange: range):
        """ Process the range of passwords """

        matching = list()

        for pw in pwrange:
            # Check increase first
            s_pw = str(pw)
            if self.check_increase(s_pw) and self.check_samedigit(s_pw):
                matching.append(pw)

        return len(matching)




if __name__ == '__main__':
    pwrange = range(156218, 652527)
    pw = PasswordChecker()

    print(pw.process(pwrange))
