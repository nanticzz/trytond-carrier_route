# This file is part of the carrier_route module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class CarrierRouteTestCase(unittest.TestCase):
    'Test CarrierRoute module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('carrier_route')

    def test0005views(self):
        'Test views'
        test_view('carrier_route')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CarrierRouteTestCase))
    return suite