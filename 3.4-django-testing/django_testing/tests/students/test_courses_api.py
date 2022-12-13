import pytest
from rest_framework.test import APIClient

from students.models import Student, Course
from model_bakery import baker


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


# @pytest.fixture()
# def student():
#     return Student.objects.create(name='buzlova', birth_date='2000-01-03')


# data_ = [
#      (1, {"name": "test_name", "students": [1]}, 201),
#      (1, {"name": "test_name", "students": [1, 2]}, 400),
#  ]
#
# @pytest.mark.django_db
# @pytest.mark.parametrize('max_students, students, status_code', data_)
# def test_max_students_validate(max_students, students, status_code, client, settings, student_factory):
#     settings.MAX_STUDENTS_PER_COURSE = max_students
#     student_factory(_quantity=2)
#     response = client.post('/api/v1/courses/', data=students)
#     assert response.status_code == status_code


@pytest.mark.django_db
def test_create_course(client, student_factory):
    factory = student_factory(_quantity=2)
    response = client.post('/api/v1/courses/', data={'name': 'django', 'students': [i.pk for i in factory]})
    # print(response.data)
    assert response.status_code == 201


result = [
    (1, {"name": "test_name", "students": [5]}, 201),
    (1, {"name": "test_name", "students": [5, 6]}, 400),
]

# проверка на максимальное количество студентов на курсе:
# @pytest.mark.parametrize('max_students, students, status_code', result)
# @pytest.mark.django_db
# def test_max_students_validate(client, settings, student_factory, max_students, students, status_code):
#     settings.MAX_STUDENTS_PER_COURSE = max_students
#     factory = student_factory(_quantity=2)
#     if len(students['students']) == 1:
#         students['students'] = [factory[0].pk]
#     else:
#         students['students'] = [i.pk for i in factory]
#     response = client.post(path='/api/v1/courses/', data=students, format='json')
#     assert response.status_code == status_code

# пробный
@pytest.mark.parametrize('max_students, students, status_code', result)
@pytest.mark.django_db
def test_max_students_validate(client, settings, student_factory, max_students, students, status_code):
    settings.MAX_STUDENTS_PER_COURSE = max_students
    factory = student_factory(_quantity=2)
    print(factory[0].pk)
    response = client.post(path='/api/v1/courses/', data=students, format='json')
    # if len(students['students']) > max_students:
    #     students['students'] = [factory[0].pk]
    #     status_code = 400
    #     print('! ! !')
    #
    # else:
    #     students['students'] = [i.pk for i in factory]
    #     status_code = 201
    #     print('- - - ')
    print(status_code, '!==!', response.status_code)
    assert response.status_code == status_code


# проверка просмотра курсов:
@pytest.mark.django_db
def test_get_сourse(client, course_factory):
    courses = course_factory(_quantity=2)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert len(response.json()) == len(courses)


# проверка просмотра одного курса:
@pytest.mark.django_db
def test_detail_course(client, course_factory):
    courses = course_factory(_quantity=2)
    pk = courses[0].pk
    response = client.get(f'/api/v1/courses/{pk}/')
    assert response.status_code == 200
    assert response.data['name'] == courses[0].name
    assert response.data['id'] == pk


# проверка обновления курсов:
@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=2)
    pk = courses[1].pk
    name = courses[1].name
    response = client.patch(f'/api/v1/courses/{pk}/', data={'name': 'django'})
    assert response.status_code == 200
    assert response.data['name'] == 'django'


# проверка удаления курсов:
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=2)
    pk = courses[0].pk
    response = client.delete(f'/api/v1/courses/{pk}/')
    assert response.status_code == 204


# проверка создания курса:
@pytest.mark.django_db
def test_create_course(client, student_factory):
    student_factory(_quantity=4)
    response = client.post('/api/v1/courses/', data={'name': 'django', 'students': [1, 2,]})
    print(response.data)
    assert response.status_code == 201



# проверка фильтрации по id:
@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    courses = course_factory(_quantity=6)
    pk = courses[0].pk
    response = client.get(f'/api/v1/courses/?id={pk}')
    assert response.status_code == 200
    assert response.json()[0]['id'] == courses[0].pk
    assert response.json()[0]['name'] == courses[0].name


# проверка фильтрации по name:
@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    courses = course_factory(_quantity=6)
    pk = courses[0].pk
    name = courses[0].name
    response = client.get(f'/api/v1/courses/?name={name}')
    assert response.status_code == 200
    assert response.json()[0]['id'] == courses[0].pk
    assert response.json()[0]['name'] == courses[0].name