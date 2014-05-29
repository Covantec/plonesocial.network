import unittest2 as unittest
from zope.component import queryUtility

from plone import api

from plonesocial.network.testing import \
    PLONESOCIAL_NETWORK_INTEGRATION_TESTING

from plonesocial.network.interfaces import INetworkGraph
from plonesocial.network.interfaces import INetworkTool


class TestNetworkTool(unittest.TestCase):

    layer = PLONESOCIAL_NETWORK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_tool_available(self):
        tool = queryUtility(INetworkTool)
        self.assertTrue(INetworkGraph.providedBy(tool))

    def test_tool_uninstalled(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=['plonesocial.network'])
        self.assertNotIn('plonesocial_network', self.portal)
        tool = queryUtility(INetworkTool, None)
        self.assertIsNone(tool)
