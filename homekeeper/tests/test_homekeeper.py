import pytest
from homekeeper.models import Homekeeper
import datetime

@pytest.mark.django_db
def test_create_homekeeper():
    contents = '매일 생활비'
    money = 10000
    inout = 'IN'
    pay_date = '2018-10-15'
    Homekeeper.objects.create(pay_date=pay_date, inout=inout, money=money, contents=contents)

    # create 로 생성된 것을 받으면, pay_date이 str 임
    homekeeper = Homekeeper.objects.all().first()
    assert 1 == homekeeper.hk_id
    assert inout == homekeeper.inout
    assert money == homekeeper.money
    expect_date = datetime.date(2018, 10, 15)
    assert expect_date == homekeeper.pay_date