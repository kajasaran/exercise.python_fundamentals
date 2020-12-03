# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):

        return "Hello World"  # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        a=str(value_to_be_added_to) + str(value_to_add)
        return a  # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        f=string_to_fetch_from[starting_index:ending_index+1]
        return f  # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        h=string_to_fetch_from[starting_index+1:ending_index]
        return h # TODO - Implement solution

    def compare(self, first_value, second_value):
        b=(first_value,second_value)
        return b  # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        c=len(string_to_fetch_from)//2
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        d=string_to_fetch_from[0]
        return d # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        e=string_to_fetch_from.split[1]
        return e # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1] # TODO - Implement solution
