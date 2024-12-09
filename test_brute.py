import pytest
from brute import Brute
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

# testBrute = Brute("TDD")

# print(testBrute.hash("TDD"))

# randomG = testBrute.randomGuess()

# testBrute.bruteOnce("d", "a")


def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_Brute_init():


        def it_fails_when_given_a_nonstring():
            with pytest.raises(Exception):
                nonString = Brute(0)

        def it_fails_when_given_no_parameters():
            with pytest.raises(Exception):
                nonString = Brute()

        def it_fails_when_given_more_than_one_parameter():
            with pytest.raises(Exception):
                nonString = Brute("d", "a")

    def describe_Brute_Hash():

        def it_returns_a_string_hash_of_given_string():
            testB = Brute("TDD")
            hString = "00ab3eef51b8551de98a6cab9352898aed783a35995285659bbdd40162fda9505aebff62d7bf29fd7474d45f303f3cddd8d3aa0383f45a9f9facd6a8860f7938"
            assert testB.hash("TDD") == hString

        def it_fails_when_given_a_nonstring():
            with pytest.raises(Exception):
                testB = Brute("TDD")
                testB.hash(5)

    def describe_Brute_randomGuess():

        def it_is_hard_to_test_for_randomness():
            assert True == True

    #     def it_returns_a_random_length_string():
    #         testB = Brute("TDD")
    #         assert testB.randomGuess() is type(String)

    def describe_bruteOnce():
        # write your test cases here
        def it_fails_when_given_no_parameters():
            testB = Brute("TDD")
            with pytest.raises(Exception):
                testB.bruteOnce()

        def it_fails_when_given_more_than_one_parameter():
            testB = Brute("TDD")
            with pytest.raises(Exception):
                testB.bruteOnce("a","b")

        def it_fails_when_given_a_nonstring():
            testB = Brute("TDD")
            with pytest.raises(Exception):
                testB.bruteOnce(5)

        def it_returns_true_when_given_the_correct_string():
            testB = Brute("TDD")
            assert testB.bruteOnce("TDD") == True

        def it_returns_false_when_given_the_incorrect_string():
            testB = Brute("TDD")
            assert testB.bruteOnce("DDT") == False

    def describe_bruteMany():
        # write your test cases here

        # My failed attempts :(
        # def it_calls_guess_manyx():
        #     testB = Brute("TDD")
        #     mock_hash = Mock()
        #     mock_guess = Mock()
        #     mockB = Mock()

        #     mockB.bruteMany() = True

        #     mockB.bruteMany()
        #     testB.bruteOnce.assert_called_once()
        pass
        
        
