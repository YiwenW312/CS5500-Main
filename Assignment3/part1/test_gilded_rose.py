# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose(unittest.TestCase):
        
    def test_normal_item(self):
        # Arrange
        items = [Item("Normal Item", 5, 10)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Normal Item")
        original_quality = gr.get_item_quality("Normal Item")

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Normal Item") == original_sell_in - 1
        assert gr.get_item_quality("Normal Item") == original_quality - 1

    def test_aged_brie(self):
        # Arrange
        items = [Item("Aged Brie", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Aged Brie") == 4
        assert gr.get_item_quality("Aged Brie") == 11

    def test_sulfuras(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Sulfuras, Hand of Ragnaros") == 5  # Never changes
        assert gr.get_item_quality("Sulfuras, Hand of Ragnaros") == 80  # Never changes

    def test_backstage_passes_11_days(self):
        # Arrange
        items = [Item("Backstage passes", 11, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Backstage passes") == 10
        assert gr.get_item_quality("Backstage passes") == 11

    def test_backstage_passes_10_days(self):
        # Arrange
        items = [Item("Backstage passes", 10, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Backstage passes") == 9
        assert gr.get_item_quality("Backstage passes") == 12

    def test_backstage_passes_5_days(self):
        # Arrange
        items = [Item("Backstage passes", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Backstage passes") == 4
        assert gr.get_item_quality("Backstage passes") == 13

    def test_backstage_passes_0_days(self):
        # Arrange
        items = [Item("Backstage passes", 0, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Backstage passes") == -1
        assert gr.get_item_quality("Backstage passes") == 0  # Drops to zero after the concert

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured")
        new_quality = gr.get_item_quality("Conjured")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2

    if __name__ == '__main__':
        unittest.main()
