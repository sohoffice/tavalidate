import logging
from unittest import TestCase

from tavalidate.xmlv import assert_xml


class Test(TestCase):
    def test_assert_xml_root(self):
        resp = DummyResponse("""<test foo="bar">
            <child></child>
        </test>""")
        assert_xml(resp, expected="""
            <test  foo="bar">
                <child></child>
            </test> 
        """)

        # Different only in whitespaces
        assert_xml(resp, expected="""<test foo="bar"><child></child></test>""")
        assert_xml(DummyResponse("""<test></test>"""), expected="""<test>
        </test>""")

        # Expect extra child
        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar">
                <child></child>
                <child2></child2>
            </test>""")

        # Expect different root tag
        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test2>
                <child></child>
            </test2>
            """)

        # Expect less attribute
        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test>
                <child></child>
            </test>
            """, strict=True)

        # Expect extra attribute
        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar" bar="foo">
                <child></child>
            </test>
            """)

        # Expect different attribute value
        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="foobarbaz">
                <child></child>
            </test>
            """)

    def test_assert_xml_child(self):
        resp = DummyResponse("""<test foo="bar">
            <child>text</child>
        </test>""")
        assert_xml(resp, expected="""
        <test foo=" bar ">
            <child>text</child>
        </test>
        """)

        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar">
                <child foo="bar">text</child>
            </test>""")

        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar">
                <child>Different text</child>
            </test>""")

        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar">
                <child></child>
            </test>""")

        with self.assertRaises(AssertionError):
            assert_xml(resp, expected="""
            <test foo="bar">
                <child>
                    <child2></child2>
                </child>
            </test>""")

        assert_xml(resp, expected="""
        <test foo="!anystr">
            <child>!anything</child>
        </test>""")

        resp2 = DummyResponse("""<test int="1" float="1.1">
            <child>True</child>
        </test>""")
        assert_xml(resp2, expected="""
        <test int="!anyint" float="!anyfloat">
            <child>!anybool</child>
        </test>""")


class DummyResponse(object):
    def __init__(self, text):
        self.text = text
