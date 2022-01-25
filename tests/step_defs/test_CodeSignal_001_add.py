# FROM:
# https://pytest-bdd.readthedocs.io/en/stable/#test-setup

from pytest_bdd import scenario, given, when, then
import src.NOW.CodeSignal.c001add.add as add

class test_CodeSignal_001_add:

@scenario('CodeSignal_001.feature', 'CodeSignal basic kata add')
def test_add():
    pass


@given("two integers")
def two_integers():
    a = 5
    b = 1
    
@given("solution")
def get_solution():
    return add.solution

@when("the integers are passed to the solution")
def calculate(a, b):
    

@then("I should not see the error message")
def no_error_message(browser):
    with pytest.raises(ElementDoesNotExist):
        browser.find_by_css('.message.error').first


@then("the article should be published")
def article_is_published(article):
    article.refresh()  # Refresh the object in the SQLAlchemy session
    assert article.is_published