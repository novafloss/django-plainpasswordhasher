# -*- coding: utf-8 -*-
"""Tests around project's distribution and packaging."""
import os
import unittest


tests_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(tests_dir)


class VersionTestCase(unittest.TestCase):
    """Various checks around project's version info."""
    def get_project_name(self):
        """Return project name."""
        return 'django-plainpasswordhasher'

    def get_package_name(self):
        """Return package name."""
        return self.get_project_name().replace('-', '_')

    def get_version(self, package):
        """Return project's version defined in package."""
        module = __import__(package, globals(), locals(), [], 0)
        return module.__version__

    def test_version_present(self):
        """:PEP:`396` - Project's package has __version__ attribute."""
        package_name = self.get_package_name()
        try:
            self.get_version(package_name)
        except ImportError:
            self.fail("{package}'s package has no __version__.".format(
                package=package_name))

    def test_version_match(self):
        """Package's __version__ matches pkg_resources info."""
        project_name = self.get_project_name()
        package_name = self.get_package_name()
        try:
            import pkg_resources
        except ImportError:
            self.fail('Cannot import pkg_resources module. It is part of '
                      'setuptools, which is a dependency of '
                      '{project}.'.format(project=project_name))
        distribution = pkg_resources.get_distribution(project_name)
        installed_version = self.get_version(package_name)
        registered_version = distribution.version
        self.assertEqual(registered_version, installed_version,
                         'Version mismatch: {package}.__version__ '
                         'is "{installed}" whereas pkg_resources tells '
                         '"{registered}". You may need to run ``make '
                         'develop`` to update the installed version in '
                         'development environment.'.format(
                             package=package_name,
                             installed=installed_version,
                             registered=registered_version))

    def test_version_file(self):
        """Project's __version__ matches VERSION file info."""
        package_name = self.get_package_name()
        version_file = os.path.join(project_dir, 'VERSION')
        installed_version = self.get_version(package_name)
        file_version = open(version_file).read().strip()
        self.assertEqual(file_version, installed_version,
                         'Version mismatch: {package}.__version__ '
                         'is "{installed}" whereas VERSION file tells '
                         '"{declared}". You may need to run ``make develop`` '
                         'to update the installed version in development '
                         'environment.'.format(
                             package=package_name,
                             installed=installed_version,
                             declared=file_version))
