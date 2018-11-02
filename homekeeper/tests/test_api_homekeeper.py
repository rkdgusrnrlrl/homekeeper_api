import pytest
import datetime


@pytest.mark.django_db
@pytest.fixture()
def homekeeper(client):
    resp = client.post('/api/homekeepers/', data={
        'contents': '매일 생활비',
        'money': 10000,
        'inout': 'IN',
        'pay_date': '2018-10-15',
    })
    contents = resp.json()

    return contents


@pytest.mark.django_db
def test_create_homekeeper(client, homekeeper):
    resp = client.get('/api/homekeepers/')
    contents = resp.json()

    print(contents)


@pytest.mark.django_db
def test_create_many_homekeeper(client):
    save_homkeeper(client, '2018-10-29', 'IN', '매일 생활비', 10000)
    save_homkeeper(client, '2018-10-29', 'OUT', '왕치마', 4200)
    save_homkeeper(client, '2018-10-29', 'OUT', '팹시', 600)
    save_homkeeper(client, '2018-10-30', 'IN', '매일 생활비', 10000)
    save_homkeeper(client, '2018-10-29', 'OUT', '치킨', 8900)
    save_homkeeper(client, '2018-11-01', 'IN', '매일 생활비', 10000)
    save_homkeeper(client, '2018-11-01', 'OUT', 'KFC', 4900)

    resp = client.get('/api/homekeepers/')
    contents = resp.json()

    assert 'list' in contents


def save_homkeeper(client, pay_date, inout, contents, money):
    resp = client.post('/api/homekeepers/', data={
        'contents': contents,
        'money': money,
        'inout': inout,
        'pay_date': pay_date,
    })
    contents = resp.json()

    return contents
