import pytest

from fixturedemo import book


@pytest.fixture(scope="module")
def book_dao(tmp_path_factory):
    path = tmp_path_factory.mktemp("books")
    dao = book.BookDao(path)
    yield dao
    dao.close()


@pytest.fixture(scope="function", autouse=True)
def empty_db(book_dao):
    yield
    book_dao.delete_all()


@pytest.mark.skip
def test__book_dao__is_empty_when_newly_created(book_dao):
    assert book_dao.count() == 0


@pytest.mark.integration
def test_book_dao__inserts_first_book_to_id_1(book_dao):
    id = book_dao.insert(book.Book(
        author="J.R.R. Tolkien",
        title="The Silmarillion",
        genre="Mythopoesis",
        read=True
    ))

    assert id == 1


@pytest.mark.integration
def test_book_dao__contains_one_book_when_one_book_is_inserted(book_dao):
    book_dao.insert(book.Book(
        author="J.R.R. Tolkien",
        title="The Silmarillion",
        genre="Mythopoesis",
        read=True
    ))

    assert book_dao.count() == 1
