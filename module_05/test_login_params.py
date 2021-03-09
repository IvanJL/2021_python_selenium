import pytest

DATA = [
    ("Tester1", "pass1"),
    ("Tester2", "pass2"),
    ("Tester3", "pass3"),
]

@pytest.mark.parametrize('user, password', DATA)
def test_one(user, password):
    print(f'{user} - {password}')



if __name__ == '__main__':
    for data in DATA:
        #data ->  ("Tester1", "pass1")
        test_one(*data)