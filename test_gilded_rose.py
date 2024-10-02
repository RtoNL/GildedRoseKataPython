# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    def test_aged_brie_quality_increases(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 5, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(brie) == [Item(brie, 1, 1), Item(brie, 4, 11)]

    def test_backstage_passes_increase_in_quality(self):
        pass_item = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_item, 15, 20), Item(pass_item, 10, 25), Item(pass_item, 5, 35)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(pass_item) == [Item(pass_item, 14, 21), Item(pass_item, 9, 27), Item(pass_item, 4, 38)]


if __name__ == '__main__':
    unittest.main()
