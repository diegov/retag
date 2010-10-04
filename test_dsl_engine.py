import unittest
from dsl_engine import DSLEngine

class FakeContext(object):
    def __init__(self):
        self._values = {}

    def set_tag_value(self, tag_name, tag_value):
        self._values[tag_name] = tag_value

    def get_tag_value(self, tag_name):
        if self._values.has_key(tag_name):
            return self._values[tag_name]
        else: return None

class DSLEngineTests(unittest.TestCase):
    """Unit tests for the DSLRuntime class."""

    def setUp(self):
        self._context = FakeContext()
        self._engine = DSLEngine(self._context)

    def test_when_executing_assignment_operator_it_should_set_the_value_of_a_tag_by_name(self):
        script = 'val=334'
        self._engine.execute(script)
        self.assertEqual(334, self._context.get_tag_value('val'))

    def test_when_executing_assignment_operator_it_should_set_the_value_of_a_tag_by_name2(self):
        script = 'valother=333'
        self._engine.execute(script)
        self.assertEqual(333, self._context.get_tag_value('valother'))

    def test_when_executing_an_arithmetric_operation_it_should_set_its_value_to_the_tag(self):
        script = 'valother_test34=(333+5)'
        self._engine.execute(script)
        self.assertEqual(338, self._context.get_tag_value('valother_test34'))

    def test_when_executing_a_nested_arithmetric_operation_it_should_set_its_value_to_the_tag(self):
        script = 'valother_test34=((20.2/2)+(5+(4/2)))'
        self._engine.execute(script)
        self.assertEqual(17.1, self._context.get_tag_value('valother_test34'))

    def test_when_setting_a_tag_to_the_value_of_another_tag_it_should_copy_the_value(self):
        self._context.set_tag_value('crap', 1000)
        script = 'new_val=crap'
        self._engine.execute(script)
        self.assertEqual(1000, self._context.get_tag_value('new_val'))

    def test_when_setting_a_tag_to_the_value_of_an_expression_including_another_tag_it_should_set_the_computed_value(self):
        self._context.set_tag_value('crap', 1000)
        script = 'new_val=(crap+3)'
        self._engine.execute(script)
        self.assertEqual(1003, self._context.get_tag_value('new_val'))

    def test_can_set_tag_to_literal_string(self):
        script = 'new_val="whats up"'
        self._engine.execute(script)
        self.assertEqual('whats up', self._context.get_tag_value('new_val'))

    def test_can_set_tag_to_concat_literal_string_and_tag_value(self):
        self._context.set_tag_value('crap', 'first')
        script = 'new_val=(crap + " second")'
        self._engine.execute(script)
        self.assertEqual('first second', self._context.get_tag_value('new_val'))

    def test_can_set_tag_to_concat_of_two_other_tags(self):
        self._context.set_tag_value('crap', 'first')
        self._context.set_tag_value('other', 'segundo')
        script = 'new_val=(crap + (" " + other))'
        self._engine.execute(script)
        self.assertEqual('first segundo', self._context.get_tag_value('new_val'))

if __name__ == "__main__":
    unittest.main()

