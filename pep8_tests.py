import pep8
from os import linesep


def test_pep8_standards():
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['project/'])
    if result.total_errors !=0:
        print("Found code style errors (and warnings):{0}{1}".format(linesep,
                                            str.join(linesep, result.get_statistics())))
    assert result.total_errors == 0

