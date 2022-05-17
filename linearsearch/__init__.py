import check50
import check50.c

filename = "linear.c"
@check50.check()
def linear_exists():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(linear_exists)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)

filename2 = "maxsearch.c"
@check50.check()
def maxsearch_exists():
    """%s exists.""" % filename2
    check50.exists(filename2)

@check50.check(maxsearch_exists)
def maxsearch_compiles():
    """%s compiles.""" % filename2
    check50.c.compile(filename2, lcs50=True)
