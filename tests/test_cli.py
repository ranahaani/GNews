import unittest
import csv
from typer.testing import CliRunner
from gnews.cli import app
import glob
import json
import os

class TestCli(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def remove_test_files(self, files: list[str]):
        for matching_file in files:
            os.remove(matching_file)

    def test_search(self):
        result = self.runner.invoke(app, ["search", "ai", "--limit", 1])

        matching_files = glob.glob("search_ai*.json");

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No articles found for the keyword \"ai\"" in result.output
        # glob.glob searches for files matching this format. 
        # If any files exist that start with search_ai and end with .json, it will find it.
        # Only 1 file should be made. If any others exist it will harm the test.
        assert len(matching_files) == 1
        # remove the new file made
        self.remove_test_files(matching_files)

    def test_trending(self):
        result = self.runner.invoke(app, ["trending", "--limit", 1])

        matching_files = glob.glob("trending_US*.json")

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No trending articles for the country \"US\"" in result.output
        assert len(matching_files) == 1

        self.remove_test_files(matching_files)

    def test_topic(self):
        result = self.runner.invoke(app, ["topic", "world", "--limit", 1])

        matching_files = glob.glob("topic_WORLD*.json")

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No articles found for the topic \"WORLD\"" in result.output
        assert len(matching_files) == 1

        self.remove_test_files(matching_files)

    def test_location(self):
        result = self.runner.invoke(app, ["location", "new york", "--limit", 1])

        matching_files = glob.glob("location_new york*.json")

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No articles found for the location \"new york\"" in result.output
        # glob.glob searches for files matching this format. 
        # If any files exist that start with search_ai and end with .json, it will find it.
        assert len(matching_files) == 1

        self.remove_test_files(matching_files)

    def test_json_output(self):
        result = self.runner.invoke(app, ["search", "ai", "--limit", 1, "--format", "json"])

        file_name = "search_ai.json"

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No articles found for the keyword \"ai\"" in result.output
        # assert that there is only this one file and no other files like it.
        assert os.path.exists(file_name) and len(glob.glob("search_ai*.json")) == 1

        f = open(os.path.abspath(file_name))
        assert json.load(f)
        self.remove_test_files(glob.glob("search_ai*.json"))

    def test_csv_output(self):
        result = self.runner.invoke(app, ["search", "ai", "--limit", 1, "--format", "csv"])
        file_name = "search_ai.csv"

        assert "Results saved to" in result.output
        assert "Total 1 articles." in result.output or "No articles found for the keyword \"ai\"" in result.output
        # assert that there is only this one file and no other files like it.
        assert os.path.exists(file_name) and len(glob.glob("search_ai*.csv")) == 1

        valid_csv = True

        # test for basic csv format
        with open(os.path.abspath(file_name), 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    valid_csv = False
        
        assert valid_csv == True
        self.remove_test_files(glob.glob("search_ai*.csv"))

    def test_table_output(self):
        result = self.runner.invoke(app, ["search", "ai", "--limit", 1, "--format", "table"])

        assert "Total 1 articles." in result.output or "No articles found for the keyword \"ai\"" in result.output