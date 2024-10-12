# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()
        # Check the first item's attributes after one day
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 1)

        # Check the second item's attributes after one day
        self.assertEqual(items[1].sell_in, 8)
        self.assertEqual(items[1].quality, 18)

        # Check the third item's attributes after one day
        self.assertEqual(items[2].sell_in, 3)
        self.assertEqual(items[2].quality, 5)

    def test_aged_brie_quality_increases(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 5, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        # Compare the first Aged Brie item's attributes
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

        # Compare the second Aged Brie item's attributes
        self.assertEqual(items[1].sell_in, 4)
        self.assertEqual(items[1].quality, 11)


    def test_backstage_passes_increase_in_quality(self):
        pass_item = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_item, 15, 20), Item(pass_item, 10, 25), Item(pass_item, 5, 35)]
        gr = GildedRose(items)

        gr.update_quality()

        # Compare the first Backstage passes item's attributes
        self.assertEqual(items[0].sell_in, 14)
        self.assertEqual(items[0].quality, 21)

        # Compare the second Backstage passes item's attributes
        self.assertEqual(items[1].sell_in, 9)
        self.assertEqual(items[1].quality, 27)

        # Compare the third Backstage passes item's attributes
        self.assertEqual(items[2].sell_in, 4)
        self.assertEqual(items[2].quality, 38)


if __name__ == '__main__':
    unittest.main()
