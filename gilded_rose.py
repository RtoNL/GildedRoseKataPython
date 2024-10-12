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
            updater = get_updater(item)
            updater.update_quality(item)
class QualityUpdater:
    def update_quality(self, item):
        self.update_item_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.update_expired_item_quality(item)

    # Default behavior for updating item quality
    def update_item_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 1)

    # Default behavior for expired items
    def update_expired_item_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 1)


class AgedBrieUpdater(QualityUpdater):
    def update_item_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def update_expired_item_quality(self, item):
        if item.quality < 50:
            item.quality += 1


class ConjuredUpdater(QualityUpdater):
    def update_item_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 2)

    def update_expired_item_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 2)


class SulfurasUpdater(QualityUpdater):
    def update_quality(self, item):
        # Sulfuras does not change in quality or sell_in
        pass


class BackstagePassUpdater(QualityUpdater):
    def update_item_quality(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif 5 < item.sell_in <= 10:
            item.quality += 2
        elif 0 < item.sell_in <= 5:
            item.quality += 3
        if item.quality > 50:
            item.quality = 50

    def update_expired_item_quality(self, item):
        item.quality = 0


class RegularUpdater(QualityUpdater):
    # No need to override anything, uses the default behavior
    pass


# Factory method to return the correct Updater based on item name
def get_updater(item):
    if item.name == "Aged Brie":
        return AgedBrieUpdater()
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassUpdater()
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater()
    elif "Conjured" in item.name:
        return ConjuredUpdater()
    else:
        return RegularUpdater()
