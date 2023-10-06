# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_single_item(item)

    def update_single_item(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            # Legendary item, does nothing.
            pass
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif "Conjured" in item.name:
            self.update_conjured_item(item)
        else:
            self.update_normal_item(item)

    def update_normal_item(self, item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

        item.sell_in -= 1
        self.ensure_quality_limits(item)

    def update_aged_brie(self, item):
        if item.sell_in > 0:
            item.quality += 1
        else:
            item.quality += 2

        item.sell_in -= 1
        self.ensure_quality_limits(item)

    def update_backstage_pass(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0

        item.sell_in -= 1
        self.ensure_quality_limits(item)

    def update_conjured_item(self, item):
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

        item.sell_in -= 1
        self.ensure_quality_limits(item)

    def ensure_quality_limits(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = max(0, min(50, item.quality))
            
    def get_item_sell_in(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.sell_in
        return None  # Return None if the item isn't found

    def get_item_quality(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.quality
        return None  # Return None if the item isn't found
