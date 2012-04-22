#!/usr/bin/env python
# encoding: utf-8

import unittest
from gitube.lib import gitolite

class GroupTest(unittest.TestCase):

    def test_add_user(self):
        group = gitolite.Group('developer')
        group.add_user('harry')
        group.add_user('harryxu')

        self.assertEqual(str(group), 'developer = harry harryxu')

    def test_del_user(self):
        group = gitolite.Group('developer')
        group.add_user('harry')
        group.add_user('flash')

        self.assertEqual(str(group), 'developer = harry flash')

        group.del_user('harry')

        self.assertEqual(str(group), 'developer = flash')
        

class RepoTest(unittest.TestCase):

    def test_add_permision(self):
        repo = gitolite.Repo('gitube')
        repo.add_permission('RW', '', 'harry', 'harryxu')
        repo.add_permission('-', 'master', 'harry')
        repo_str = str(repo)

        self.assertRegexpMatches(repo_str, 'repo\sgitube');
        self.assertRegexpMatches(repo_str, 'RW\s+=\sharry');
        self.assertRegexpMatches(repo_str, 'RW\s+=\sharryxu');
        self.assertRegexpMatches(repo_str, '-\smaster\s+=\sharry');

    def test_del_permission(self):
        repo = gitolite.Repo('gitube')
        repo.add_permission('RW', '', 'harry')
        repo.add_permission('-', 'master', 'harry')
        repo_str = str(repo)

        self.assertRegexpMatches(repo_str, 'RW\s+=\sharry');
        self.assertRegexpMatches(repo_str, '-\smaster\s+=\sharry');

        repo.del_permission('harry')
        repo_str = str(repo)

        self.assertNotRegexpMatches(repo_str, 'RW\s+=\sharry')
        self.assertNotRegexpMatches(repo_str, '-\smaster\s+=\sharry');




if __name__ == '__main__':
    unittest.main()
