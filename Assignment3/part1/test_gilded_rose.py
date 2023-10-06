""" This module contains the unit tests for the Gilded Rose kata. """
# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose(unittest.TestCase):
    """
    This class contains the unit tests for the Gilded Rose kata.
    """
    def test_normal_item(self):
        """
        Test that a normal item decreases in quality and sell_in by 1.
        """
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
        """
        This test checks that the quality of Aged Brie increases by 1.
        """
        # Arrange
        items = [Item("Aged Brie", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Aged Brie") == 4
        assert gr.get_item_quality("Aged Brie") == 11

    def test_sulfuras(self):
        """
        This test checks that the quality
        and sell_in of Sulfuras does not change.
        """
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Sulfuras, Hand of Ragnaros") == 5
        assert gr.get_item_quality("Sulfuras, Hand of Ragnaros") == 80

    def test_backstage_passes_11_days(self):
        """
        This test checks that the quality of Backstage passes increases by 1.
        """
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        print(f"[DEBUG 11 days] - Quality: {gr.get_item_quality('Backstage passes to a TAFKAL80ETC concert')}, Expected: 11")
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 10
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 11

    def test_backstage_passes_10_days(self):
        """
        This test checks that the quality of Backstage passes increases by 2.
        """
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        print(f"[DEBUG 10 days] - Quality: {gr.get_item_quality('Backstage passes to a TAFKAL80ETC concert')}, Expected: 12")
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 9
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 12

    def test_backstage_passes_5_days(self):
        """
        This test checks that the quality of Backstage passes increases by 3.
        """
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        print(f"[DEBUG 5 days] - Quality: {gr.get_item_quality('Backstage passes to a TAFKAL80ETC concert')}, Expected: 13")
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 4
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 13

    def test_backstage_passes_0_days(self):
        """
        This test checks that the quality of Backstage passes drops to 0.
        """
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        print(f"[DEBUG 0 days] - Quality: {gr.get_item_quality('Backstage passes to a TAFKAL80ETC concert')}, Expected: 0")
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == -1
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 0  # Drops to zero after the concert

    def test_conjured_item(self):
        """
        This test checks that the quality of Conjured items decreases by 2.
        """
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
