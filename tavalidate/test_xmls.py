from unittest import TestCase

from tavalidate.test_xmlv import DummyResponse
from tavalidate.xmls import save_xml


class Test(TestCase):
    def test_save_xml(self):
        resp = DummyResponse("""
        <foo at1="1">
            <bar at2="2">str</bar>
        </foo>""")
        x = save_xml(resp, variables={
            'bar': '/foo/bar/text()',
            'at1': '/foo/@at1',
            'at2': '/foo/bar/@at2'
        })
        assert x['bar'] == 'str'
        assert x['at1'] == '1'
        assert x['at2'] == '2'

    def test_save_xml_with_encoding_declaration(self):
        resp = DummyResponse(
                """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <foo><statusCode>S</statusCode></foo>""")

        with self.assertRaises(AssertionError):
            save_xml(resp, variables={
                'notFound': '/not/found'
            })

        x = save_xml(resp, variables={
            'status': '/foo/statusCode/text()'
        })
        assert x['status'] == 'S'
