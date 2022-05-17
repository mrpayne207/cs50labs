import check50
import check50.c

filename = "mystruct.c"
@check50.check()
def mystruct_exists():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(mystruct_exists)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)

filename2 = "struct1.c"
@check50.check()
def struct1_exists():
    """%s exists.""" % filename2
    check50.exists(filename2)

@check50.check(struct1_exists)
def struct1_compiles():
    """%s compiles.""" % filename2
    check50.c.compile(filename2, lcs50=True)
