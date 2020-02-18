"""You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:
    +91 xxxxx xxxxx
    The given mobile numbers may have +91,91  or 0
     written before the actual  digit number.
      Alternatively, there may not be any prefix at all."""


def wrapper(func):
    def fun(l):
        s = ["+91" + " " + i[-10:-5] + " " + i[-5:] for i in l]
        return func(s)
    return fun


@wrapper
def sorte(l):
    print(*sorted(l), sep="\n")


nos = [input() for _ in range(5)]
sorte(nos)
