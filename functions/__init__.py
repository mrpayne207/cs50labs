import check50
import check50.c

filename = "functions.c"
filename2 = "functions2.c"

@check50.check()
def exists():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(exists)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)

@check50.check()
def functions2_exists():
    """%s exists.""" % filename2
    check50.exists(filename2)

@check50.check(functions2_exists)
def functions2_compiles():
    """%s compiles.""" % filename2
    check50.c.compile(filename2, lcs50=True)
