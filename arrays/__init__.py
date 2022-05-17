import check50
import check50.c

filename = "array.c"
@check50.check()
def array_exists():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(array_exists)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)

filename2 = "string.c"
@check50.check()
def string_exists():
    """%s exists.""" % filename2
    check50.exists(filename2)

@check50.check(string_exists)
def string_compiles():
    """%s compiles.""" % filename2
    check50.c.compile(filename2, lcs50=True)
