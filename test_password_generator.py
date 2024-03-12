import pytest
import password_generator
import string
import os ,io ,sys

@pytest.mark.parametrize("length,ch",[(9,1),(10,2),(8,3),(11,4),(9,5),(15,6)])
def test_password_generator(length,ch):

    password= password_generator.password_generator(length, ch)
    assert len(password)==length
    if ch in (1,3,6,5):
        assert any(chr.isdigit() for chr in password)
    if ch in (2,3,4,6):
        assert any(chr.isascii() for chr in password)
    if ch in (4,5,6):
        assert any(chr in string.punctuation for chr in password)

    assert all(ord(chr) < 128 for chr in password)


@pytest.mark.parametrize("file_type, name", [(1,'p.csv'),(2,'p.json'),(3,'p.txt')])
def test_exp(file_type,name):
    # passw="abc123"
    dir=os.path.join(os.getcwd(),name)
    captured_stdout = io.StringIO()
    sys.stdout = captured_stdout
    password_generator.exp(file_type,name,"abc123")
    captured_output = captured_stdout.getvalue()
    assert "output has been exported to" in captured_output
    assert os.path.isfile(dir)

