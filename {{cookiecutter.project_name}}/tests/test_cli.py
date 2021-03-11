#!/usr/bin/env python
# encoding: utf-8

from fire import testutils

from {{ cookiecutter.project_slug }} import __main__


class CoreTest(testutils.BaseTestCase):

    def test_version(self):
        with self.assertOutputMatches(stdout='.*'):
            __main__.fire.Fire(__main__.version, command=[])

    def test_version_help_info(self):
        with self.assertRaisesFireExit(0, regexp='显示当前版本'):
            __main__.fire.Fire({"version": __main__.version}, command=['version', '--help'])

    def test_help_info(self):
        with self.assertOutputMatches(stdout='.*'):
            __main__.entry_point()
