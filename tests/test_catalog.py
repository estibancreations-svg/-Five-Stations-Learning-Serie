import collections
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class CatalogContracts(unittest.TestCase):
    def setUp(self):
        self.episodes = json.loads((ROOT / 'projects/creative-ip/five-stations/episodes.json').read_text())

    def test_approved_season_inventory(self):
        self.assertEqual(len(self.episodes), 150)
        expected = {(series, season): 15 for series in ['momo', 'rocket', 'yeti', 'doodle', 'powerpals'] for season in [2, 3]}
        self.assertEqual(dict(collections.Counter((e['series'], e['season']) for e in self.episodes)), expected)

    def test_episode_identity_and_teaching_structure(self):
        ids = [(e['series'], e['season'], e['number']) for e in self.episodes]
        self.assertEqual(len(ids), len(set(ids)))
        for episode in self.episodes:
            self.assertIn(episode['number'], range(1, 16))
            for field in ['title', 'theme', 'logline']:
                self.assertTrue(isinstance(episode[field], str) and episode[field].strip())
            self.assertGreaterEqual(len(episode['beats']), 3)
            self.assertTrue(all(isinstance(b, str) and b.strip() for b in episode['beats']))

    def test_calibration_cannot_enable_autopilot(self):
        manifest = json.loads((ROOT / 'projects/creative-ip/five-stations/test-runs/character-continuity/test-run-manifest.json').read_text())
        self.assertEqual(manifest['pilot_gate'], 'not_enabled')
        self.assertEqual(manifest['mode'], 'supervised_calibration')
        self.assertTrue(manifest['not_tested'])
        for run in manifest['runs']:
            self.assertTrue(run['holds'])

if __name__ == '__main__':
    unittest.main()
