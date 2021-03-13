import unittest
import random
from scores import Scores


class TestJSON(unittest.TestCase):
    def test_best_score(self):
        scores = Scores()
        exp = ('STUYVESANT HIGH SCHOOL', 2096)
        actual = scores.best_score()
        self.assertEqual(
            exp, actual, 'best_score() did not return the school with the highest score')

    def test_best_score_small(self):
        scores = Scores()
        exp = ('URBAN ACADEMY LABORATORY HIGH SCHOOL', 1547)
        actual = scores.best_score_small()
        self.assertEqual(
            exp, actual, 'best_score_small() did not return the highest scoring school with no more than 50 students')

    def test_most_tests(self):
        scores = Scores()
        exp = ('BROOKLYN TECHNICAL HIGH SCHOOL', 1277)
        actual = scores.most_tests()
        self.assertEqual(
            exp, actual, 'most_tests() did not return the correct results')

    def test_x_most_tests(self):
        scores = Scores()
        counts = [5, 7, 13, 2, 9]
        exp = {
            5: [('BROOKLYN TECHNICAL HIGH SCHOOL', 1277),
                ('FRANCIS LEWIS HIGH SCHOOL', 934),
                ('BENJAMIN N. CARDOZO HIGH SCHOOL', 888),
                ('STUYVESANT HIGH SCHOOL', 832),
                ('MIDWOOD HIGH SCHOOL', 824)],
            7: [('BROOKLYN TECHNICAL HIGH SCHOOL', 1277),
                ('FRANCIS LEWIS HIGH SCHOOL', 934),
                ('BENJAMIN N. CARDOZO HIGH SCHOOL', 888),
                ('STUYVESANT HIGH SCHOOL', 832),
                ('MIDWOOD HIGH SCHOOL', 824),
                ('TOTTENVILLE HIGH SCHOOL', 807),
                ('FOREST HILLS HIGH SCHOOL', 762)],
            13: [('BROOKLYN TECHNICAL HIGH SCHOOL', 1277),
                 ('FRANCIS LEWIS HIGH SCHOOL', 934),
                 ('BENJAMIN N. CARDOZO HIGH SCHOOL', 888),
                 ('STUYVESANT HIGH SCHOOL', 832),
                 ('MIDWOOD HIGH SCHOOL', 824),
                 ('TOTTENVILLE HIGH SCHOOL', 807),
                 ('FOREST HILLS HIGH SCHOOL', 762),
                 ('BRONX HIGH SCHOOL OF SCIENCE', 731),
                 ('EDWARD R. MURROW HIGH SCHOOL', 727),
                 ('BAYSIDE HIGH SCHOOL', 708),
                 ('FORT HAMILTON HIGH SCHOOL', 694),
                 ('JOHN BOWNE HIGH SCHOOL', 558),
                 ('SUSAN E. WAGNER HIGH SCHOOL', 535)],
            2: [('BROOKLYN TECHNICAL HIGH SCHOOL', 1277), ('FRANCIS LEWIS HIGH SCHOOL', 934)],
            9: [('BROOKLYN TECHNICAL HIGH SCHOOL', 1277),
                ('FRANCIS LEWIS HIGH SCHOOL', 934),
                ('BENJAMIN N. CARDOZO HIGH SCHOOL', 888),
                ('STUYVESANT HIGH SCHOOL', 832),
                ('MIDWOOD HIGH SCHOOL', 824),
                ('TOTTENVILLE HIGH SCHOOL', 807),
                ('FOREST HILLS HIGH SCHOOL', 762),
                ('BRONX HIGH SCHOOL OF SCIENCE', 731),
                ('EDWARD R. MURROW HIGH SCHOOL', 727)]
        }
        for cnt in counts:
            actual = scores.x_most_tests(cnt)
            self.assertEqual(exp[cnt], actual, 'x_most_tests(' +
                             str(cnt) + ') did not return the correct result')

    def test_x_highest_scores(self):
        scores = Scores()
        counts = [2, 9, 5, 10]
        exp = {
            2: [('STUYVESANT HIGH SCHOOL', 2096), ('BRONX HIGH SCHOOL OF SCIENCE', 1969)],
            9: [('STUYVESANT HIGH SCHOOL', 2096),
                ('BRONX HIGH SCHOOL OF SCIENCE', 1969),
                ('STATEN ISLAND TECHNICAL HIGH SCHOOL', 1953),
                ('HIGH SCHOOL OF AMERICAN STUDIES AT LEHMAN COLLEGE', 1920),
                ('TOWNSEND HARRIS HIGH SCHOOL', 1910),
                ('QUEENS HIGH SCHOOL FOR THE SCIENCES AT YORK COLLEGE', 1868),
                ('BARD HIGH SCHOOL EARLY COLLEGE', 1856),
                ('HIGH SCHOOL FOR MATHEMATICS, SCIENCE AND ENGINEERING AT CITY COLLEGE', 1847),
                ('BROOKLYN TECHNICAL HIGH SCHOOL', 1833)],
            5: [('STUYVESANT HIGH SCHOOL', 2096),
                ('BRONX HIGH SCHOOL OF SCIENCE', 1969),
                ('STATEN ISLAND TECHNICAL HIGH SCHOOL', 1953),
                ('HIGH SCHOOL OF AMERICAN STUDIES AT LEHMAN COLLEGE', 1920),
                ('TOWNSEND HARRIS HIGH SCHOOL', 1910)],
            10: [('STUYVESANT HIGH SCHOOL', 2096),
                 ('BRONX HIGH SCHOOL OF SCIENCE', 1969),
                 ('STATEN ISLAND TECHNICAL HIGH SCHOOL', 1953),
                 ('HIGH SCHOOL OF AMERICAN STUDIES AT LEHMAN COLLEGE', 1920),
                 ('TOWNSEND HARRIS HIGH SCHOOL', 1910),
                 ('QUEENS HIGH SCHOOL FOR THE SCIENCES AT YORK COLLEGE', 1868),
                 ('BARD HIGH SCHOOL EARLY COLLEGE', 1856),
                 ('HIGH SCHOOL FOR MATHEMATICS, SCIENCE AND ENGINEERING AT CITY COLLEGE', 1847),
                 ('BROOKLYN TECHNICAL HIGH SCHOOL', 1833),
                 ('ELEANOR ROOSEVELT HIGH SCHOOL', 1758)]
        }
        for cnt in counts:
            actual = scores.x_highest_scores(cnt)
            self.assertEqual(exp[cnt], actual, 'x_highest_scores(' +
                             str(cnt) + ') did not return correct result')


if __name__ == '__main__':
    unittest.main()
