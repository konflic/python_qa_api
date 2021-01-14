import pytest
import random
import requests


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'),
                          (-1, '-1'),
                          (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_api_post_request(base_url, input_id, output_id, input_title, output_title):
    res = requests.post(
        base_url + "/posts",
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_id


# Param filtering users posts by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId', [-1, 0, 'a', 11])
def test_api_empty_response(base_url, userId):
    res = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    )
    # Проверяем что на таких данных ответ пустой
    assert res.json() == []


# Param filtering users by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (10, 10)])
def test_api_filtering(base_url, userId, userId_in_response):
    response = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    ).json()
    random_post_number = random.randint(1, 9)
    assert len(response) > 0
    assert response[random_post_number]['userId'] == userId_in_response
