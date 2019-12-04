#!/usr/bin/env python
import re



class PasswordChecker(object):
    """ Object to check passwords conforming to puzzle """

    def __init__(self, pwrange: range) -> None:
        """ Initialize the range """
        self.pwrange = pwrange

    def check_samedigit(self, pw: str) -> bool:
        """ We check for repeating digits """
        res = re.compile(r'.*(\d)\1.*')
        res_4 = re.compile(r'.*(\d)\1\1\1.*')
        res_6 = re.compile(r'.*(\d)\1\1\1\1\1.*')
        if res.match(pw) is not None:
            # Check what digit it is:
            digit = res.match(pw).group(1)
            if res_4.match(pw) is None:
                # There isn't four of it, so let's check if there's three
                if f'{digit * 3}' in pw:
                    # There is not four, but there is three
                    return False
                else:
                    # There is in fact two
                    return True
            else:
                # There is four, but is there five?
                if f'{digit * 5}' in pw:
                    return False
                else:
                    return True

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


    def process(self):
        """ Process the range of passwords """

        matching = list()

        for pw in self.pwrange:
            # Check increase first
            s_pw = str(pw)
            if self.check_increase(s_pw) and self.check_samedigit(s_pw):
                matching.append(pw)

        return len(matching)




if __name__ == '__main__':
    pwrange = range(156218, 652527)
    pw = PasswordChecker(pwrange)

    print(pw.process())
