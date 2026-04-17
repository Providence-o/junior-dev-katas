# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


@pytest.mark.parametrize(
    "item,expected_quality",
    [
        (Item("foo", 5, 7), 6),
        (Item("bar", -1, 7), 5),
        (Item("bar", 4, 0), 0),
        (Item("Aged Brie", 4, 0), 1),
        (Item("Aged Brie", 4, 50), 50),
        (Item("Backstage passes to a TAFKAL80ETC concert", 4, 50), 50),
        (Item("Backstage passes to a TAFKAL80ETC concert", 11, 20), 21),
        (Item("Backstage passes to a TAFKAL80ETC concert", 9, 10), 12),
        (Item("Backstage passes to a TAFKAL80ETC concert", 5, 10), 13),
        (Item("Backstage passes to a TAFKAL80ETC concert", -1, 10), 0),
        (Item("Sulfuras, Hand of Ragnaros", 5, 80), 80),
        pytest.param(Item("Conjured foo", 11, 20), 18, marks=pytest.mark.xfail),
    ],
)
def test_item_quality(item, expected_quality):
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == expected_quality


@pytest.mark.parametrize(
    "item,expected_sell_in",
    [
        (Item("Backstage passes to a TAFKAL80ETC concert", 5, 7), 4),
        (Item("Sulfuras, Hand of Ragnaros", 5, 80), 5),
    ],
)
def test_sell_in(item, expected_sell_in):
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == expected_sell_in
